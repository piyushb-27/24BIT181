'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 7. Weather parameter checking with overloaded in operator
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

# Example usage
weather = Weather(["temperature", "humidity", "pressure", "wind_speed"])
print("Weather parameters:", weather.parameters)
print("Is 'temperature' present?", "temperature" in weather)
print("Is 'precipitation' present?", "precipitation" in weather)
