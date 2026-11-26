import openpyxl


def age_avg(excel):
    """
    sums the age in file and returns the avrage
    """
    count = 0
    age_ttl = 0
    wb = openpyxl.load_workbook(excel)
    ws = wb.active  
    for row in range(2 , ws.max_row + 1):
        age = ws[f"F{row}"].value
        age_ttl += (age)
        count += 1

    avg = age_ttl / count
    return count , avg

my_file = input(" Enter your file location : ")
total , avrage = age_avg(my_file)
print(f"there is {total} people in this file and avrage age is {round(avrage , 2)}")

