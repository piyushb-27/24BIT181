'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 5. Time arithmetic operations (addition, subtraction)
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def __add__(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other):
        total_seconds1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff_seconds = total_seconds1 - total_seconds2
        if diff_seconds < 0:
            return Time(0, 0, 0)
        hours = diff_seconds // 3600
        diff_seconds %= 3600
        minutes = diff_seconds // 60
        seconds = diff_seconds % 60
        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Example usage
t1 = Time(5, 45, 30)
t2 = Time(2, 30, 45)
print(f"Time 1: {t1}")
print(f"Time 2: {t2}")
print(f"Addition: {t1 + t2}")
print(f"Subtraction: {t1 - t2}")
