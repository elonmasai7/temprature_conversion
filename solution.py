class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [round(kelvin, 5), round(fahrenheit, 5)]


solution = Solution()

celsius1 = 36.50
output1 = solution.convertTemperature(celsius1)
print("Input: {}".format(celsius1))
print("Output: {}".format(output1))

celsius2 = 122.11
output2 = solution.convertTemperature(celsius2)
print("Input: {}".format(celsius2))
print("Output: {}".format(output2))
