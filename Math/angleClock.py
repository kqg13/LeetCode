# Math problem 1344: Angle Between Hands of a Clock

# Given two numbers, hour and minutes. Return the smaller angle (in degrees)
# formed between the hour and the minute hand.

# Examples:
# Input1: hour1 = 12, minutes1 = 30 ---> 165
# Input2: hour2 = 3,  minutes2 = 30 ---> 75
# Input3: hour3 = 3,  minutes3 = 15 ---> 7.5
# Input4: hour4 = 4,  minutes4 = 50 ---> 155
# Input5: hour5 = 12, minutes5 = 0 ---> 0
# Input5: hour6 = 1,  minutes6 = 57 ---> 76.5


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        MINUTE_TICKS, MINUTE_DEGREES = 5, 6
        minuteHand = minutes / MINUTE_TICKS
        hourHandIndex = ((hour % 12) * MINUTE_TICKS) + ((minuteHand / 12) * MINUTE_TICKS)
        minuteHandIndex = minuteHand * MINUTE_TICKS
        degrees = (max(hourHandIndex, minuteHandIndex) - min(hourHandIndex,  minuteHandIndex)) * MINUTE_DEGREES
        smallerAngle = min(degrees, 360 - degrees)
        return smallerAngle
