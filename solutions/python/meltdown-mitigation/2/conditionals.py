"""
A simple module checking the reactor performance
"""

def is_criticality_balanced(temp , neu_sec):
    """  
     Checking criticality
     temp (int) : tempreture of reactor in kelvin _ should be lower than 800
     neu_sec (int) : neutrons emitted per second 
     """
    situation = temp * neu_sec
    # situation (int) : multipile of tempreture and neutrons emitted per second 
    # should be lower than 500 thousand
    return temp < 800 and neu_sec > 500 and situation < 500000


def reactor_efficiency(voltage , current , theoretical_max_power):
    """
    Rating status of reactor
    voltage (int) : meausered reactor voltage 
    currunt (int) : meausered reactor current
    theoretical_max_power (int) : maximum power of reactor _ should not pass this value
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    satus = False
    if efficiency >= 80 :
        status = "green"

    elif 60 <= efficiency < 80 :
        status = "orange"

    elif 30 <= efficiency < 60 :
        status = "red"

    elif efficiency < 30 :
        status = "black"

    return status


def fail_safe(temp , neu_sec , threshold):
    """
    Checking safety of reactor
    
    temp (int) : tempreture of reactor in kelvin
    neu_sec (int) : neutrons produced per_second per thousand
    thershold (int) : the maximum of output power
    """
    output = (temp * neu_sec)
    if output < threshold * 0.9 :
        status = "LOW"
    elif output <= threshold * 1.1:
        status = "NORMAL"
    else:
        status = "DANGER"
    return status

