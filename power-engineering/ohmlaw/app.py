"""
get's the input from user and sends to ohmlaw modulde for calculation
"""
from OhmsLaw import OhmLaw


def get_message(message):
    """
    checks if user has entered a valid input
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(" invalid input . enter a valid number")


def get_input(user):
    """
    having inouts in one function to avoid reaption
    """  
    if user == "v":
        current = get_message(" enter current : ")
        resistance = get_message(" enter resistance : ")
        return current , resistance
    
    if user == "r":
        current = get_message(" enter current : ")
        voltage = get_message(" enter voltage : ")
        return current , voltage
    
    if user == "c" :
        resistance = get_message(" enter resistance : ")
        voltage = get_message(" enter voltage : ")
        return resistance , voltage



def welcome():
    """
    saluts the user
    """
    print(" ========================")
    print("  OhmLaw Calculator ")
    print(" ========================")


def tools_selector():
    """
    user can select tools
    """
    print(" "
    "[V] Calculate Voltage " \
    "\n [I] Calculate Current " \
    "\n [R] Calculate Resistance " \
    "\n [Q] Quit")
    user = input(" enter here : ")
    return user

def tools(user):
    """
    selects the correct tool for user
    """
   
    if user == "v":
        current , resistance = get_input(user)
        voltage = ohm.voltage(current , resistance)
        return (f"\n voltage is {voltage} V")
    
    if user == "r":
        current , voltage = get_input(user)
        resistance = ohm.resistance(voltage , current)
        return (f"\n resistance is {resistance} KΩ")
    
    if user == "c":
        resistance , voltage = get_input(user)
        current = ohm.current(voltage , resistance)
        return (f"\n current is {current} mA")   
     
    if user == "p":
        power = ohm.power(current , resistance , voltage)
        return (f"\n power is {power} KW")

ohm = OhmLaw()
welcome()
running = True
while running:
    print(tools(tools_selector()))
    user = input("\n if you want to quit type 'q' or 'c' to continue : \n")
    if user == "q":
        running = False
    if user == "c":
        running = True
