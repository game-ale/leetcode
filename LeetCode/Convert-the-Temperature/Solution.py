class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        degre_Kelvin = celsius + 273.15
        degre_Fahrenheit = celsius * 1.80 + 32.00
        return [degre_Kelvin,degre_Fahrenheit]