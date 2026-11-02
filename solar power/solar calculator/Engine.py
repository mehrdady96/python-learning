import math
sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
acos = lambda x : math.degrees(math.acos(x))


def latitude_angle(angle = 43):
    return angle  


def hourly_angle(time):
    # Takes the time from user and calculates how far is from 12:00
    user_hour , user_minute = time
    hour = user_hour * 60
    diffrence = (hour + user_minute) - (12 * 60)
    angle = (diffrence/60) * 15 # Every one hour is 15 degrees
    return angle


def declination_angle(nth_day):
    # Calculates Declination Angle
    declination = 23.45 * sin(360 * (284 + nth_day) / 365)
    return declination


def b_day(date):
    # Takes Month and Day from user and finds which day of year it is / nth day of year
    dates = {
      'January' : 31 , 
      'February' : 28 ,
      'March' : 31 , 
      'April' : 30 ,
      'May' : 31 ,
      'June' : 30 ,
      'July' : 31 ,
      'August' : 31 , 
      'September' : 30 , 
      'October' : 31 , 
      'November' : 30 , 
      'December' : 31
    }
    user_month , user_day = date
    counted = 0
    for month in dates:
        if month != user_month :
            counted = counted + dates[month]
        else : 
            counted = counted +  user_day
            break
    return counted

def incidence_angle(d , l , s , a , h):
    # Calculates Incidence Angle
    cos_theta = (
    sin(d) * sin(l) * cos(s)
    - sin(d) * cos(l) * sin(s) * cos(a)
    + cos(d) * cos(l) * cos(s) * cos(h)
    + cos(d) * sin(l) * sin(s) * cos(a) * cos(h)
    + cos(d) * sin(s) * sin(a) * sin(h)
)
    theta = acos(cos_theta)
    return theta
