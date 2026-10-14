"""Tkinter graphical interface for the solar incidence angle calculator."""

import tkinter as tk
from tkinter import messagebox, ttk

import app


MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December",
]

DAYS_IN_MONTH = {
    "January": 31, "February": 28, "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31,
}


def run():
    """Create the window and use the calculation function provided by app.py."""
    root = tk.Tk()
    root.title("Solar Calculator")
    root.resizable(False, False)
    root.configure(padx=20, pady=16)

    hour_var = tk.StringVar(value="12")
    minute_var = tk.StringVar(value="00")
    month_var = tk.StringVar(value="January")
    day_var = tk.StringVar(value="1")
    azimuth_var = tk.StringVar(value="0")
    latitude_var = tk.StringVar(value="43")
    slope_var = tk.StringVar(value="0")
    result_var = tk.StringVar(value="Enter the values and calculate.")

    def calculate():
        try:
            hour = int(hour_var.get())
            minute = int(minute_var.get())
            day = int(day_var.get())
            azimuth = float(azimuth_var.get())
            latitude = float(latitude_var.get() or "43")
            slope = float(slope_var.get())

            if not 0 <= hour <= 23:
                raise ValueError("Hour must be between 0 and 23.")
            if not 0 <= minute <= 59:
                raise ValueError("Minute must be between 0 and 59.")
            if slope < 0:
                raise ValueError("Slope cannot be negative.")

            month = month_var.get()
            if not month:
                raise ValueError("Please select a month.")
            if not 1 <= day <= DAYS_IN_MONTH[month]:
                raise ValueError(f"{month} has {DAYS_IN_MONTH[month]} days.")

            angle = app.finding_incidence(
                (hour, minute),
                (month, day),
                azimuth,
                latitude,
                slope,
            )
            result_var.set(f"Incidence angle: {angle:.2f}°")
        except ValueError as error:
            messagebox.showerror("Invalid input", str(error), parent=root)
        except Exception as error:
            messagebox.showerror("Calculation error", str(error), parent=root)

    ttk.Label(root, text="Solar Calculator", font=("Times New Roman", 16, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 14)
    )

    ttk.Label(root, text="Solar time").grid(row=1, column=0, sticky="w", pady=5)
    time_frame = ttk.Frame(root)
    time_frame.grid(row=1, column=1, sticky="w")
    ttk.Spinbox(time_frame, from_=0, to=23, width=5, textvariable=hour_var).pack(side="left")
    ttk.Label(time_frame, text=":").pack(side="left", padx=3)
    ttk.Spinbox(time_frame, from_=0, to=59, width=5, textvariable=minute_var).pack(side="left")

    ttk.Label(root, text="Month").grid(row=2, column=0, sticky="w", pady=5)
    ttk.Combobox(
        root, textvariable=month_var, values=MONTHS, state="readonly", width=20
    ).grid(row=2, column=1, sticky="ew")

    ttk.Label(root, text="Day").grid(row=3, column=0, sticky="w", pady=5)
    ttk.Spinbox(root, from_=1, to=31, width=8, textvariable=day_var).grid(
        row=3, column=1, sticky="w"
    )

    ttk.Label(root, text="Azimuth angle (°)").grid(row=4, column=0, sticky="w", pady=5)
    ttk.Entry(root, textvariable=azimuth_var).grid(row=4, column=1, sticky="ew")

    ttk.Label(root, text="Latitude (°)").grid(row=5, column=0, sticky="w", pady=5)
    ttk.Entry(root, textvariable=latitude_var).grid(row=5, column=1, sticky="ew")

    ttk.Label(root, text="Slope (°)").grid(row=6, column=0, sticky="w", pady=5)
    ttk.Entry(root, textvariable=slope_var).grid(row=6, column=1, sticky="ew")

    ttk.Button(root, text="Calculate", command=calculate).grid(
        row=7, column=0, columnspan=2, sticky="ew", pady=(14, 10)
    )
    ttk.Label(root, textvariable=result_var, font=("Times New Roman", 11, "bold")).grid(
        row=8, column=0, columnspan=2, pady=(4, 0)
    )

    root.mainloop()


if __name__ == "__main__":
    run()
