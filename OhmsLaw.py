"""
this module helps calculate simple ohms law
"""


class OhmLaw:
    """
    defining methods
    """

    def voltage(self , current , resistance):
        """
        calculates V from I * R
        """

        return current * resistance

    def current(self, voltage, resistance):
        """
        calculates I from V / R
        """
        if resistance == 0:
            raise ValueError("R cannot be Zero")
        
        return voltage / resistance

    def resistance(self, voltage, current):
        """
        calculates R from V / I
        """
        if current == 0 :
            raise ValueError("I cannot be Zero")
        
        return voltage / current



ohm = OhmLaw()
print(f" Voltage :{ohm.voltage(20, 5)}")
print(f" Current : {ohm.current(100 , 0)}")
print(f" Resistance : {ohm.resistance(100 , 20)}")