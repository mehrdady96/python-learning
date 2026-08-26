"""
this module helps calculate simple ohms law
"""


class OhmLaw:
    """
    defining methods
    """

    def validate_resistance(self, resistance):
        """
        checks if resistance is greater than Zero
        """
        if resistance <= 0:
            raise ValueError("Resistance must be greater than Zero")
    
    def voltage(self , current , resistance):
        """
        calculates V from I * R
        """
        self.validate_resistance(resistance)
        return current * resistance

    def current(self, voltage, resistance):
        """
        calculates I from V / R
        """

        self.validate_resistance(resistance)
        return voltage / resistance

    def resistance(self, voltage, current):
        """
        calculates R from V / I
        """
        
        if current == 0 :
            raise ValueError("I cannot be Zero")
        
        return voltage / current

    def power(self , voltage = None , current = None , resistance = None):
        if voltage is None :
            return resistance * current * current
        if current is None :
            return  voltage * voltage / resistance
        if resistance is None :
            return voltage * current
        if voltage is not None and current is not None and resistance is not None :
            return voltage * current
        