import Engine


def welcome():
 print("")
 print("============================")
 print(" Welcome to Solar Calculator ")
 print(" Here you can calculate Incidence Angle ")
 print(" You have to enter Latitude , Solar Time , nth day , Azimuth angle and Slope ")


def calculator():
 hour = int(input(" [1] Hourly Angle (hour) : "))
 minute = int(input(" [1] Hourly Angle (minute) : "))
 time = ( hour , minute )
 month = (input(" [2] Date (Month name) : "))
 day = int(input( " [2] Date (Day) : "))
 date = (month , day)
 azimuth = float(input(" [3] Azimuth Angle (degree) : "))
 latitude = (input(" [4] Latitude (if empty, it will be 43) : "))
 if latitude == '':
  latitude = 43
 else:
  latitude = float(latitude)
 slope = float(input(" [5] Slope (degree) : "))
 return time , date , azimuth , latitude , slope


def finding_incidence(hourly_angle , date , azimuth , latitude , slope):
 h = Engine.hourly_angle(hourly_angle)
 nth_day = Engine.b_day(date)
 d = Engine.declination_angle(nth_day)
 a = azimuth
 l = latitude
 s = slope
 incidence = Engine.incidence_angle(d , l , s , a , h)
 return incidence 


def result(incidence):
 return(f" Your Incidence Angle is {incidence:.2f} ")





if __name__ == "__main__":
 welcome()
 hourly_angle , date , azimuth , latitude , slope = calculator()
 print(result(finding_incidence(hourly_angle , date , azimuth , latitude , slope)))
