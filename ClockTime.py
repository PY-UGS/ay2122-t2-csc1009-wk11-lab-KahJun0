class ClockTime:

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self):
        hourInput = input('Please enter hour value (Value should be between 0 to 23): ')
        hourInput = int(hourInput)
        if 0 < hourInput < 24:
            self.hours = hourInput
        else:
            print('Invalid hour value')

    def setMinutes(self):
        minuteInput = input('Please enter minute value (Value should be between 0 to 59): ')
        minuteInput = int(minuteInput)
        if 0 <= minuteInput < 60:
            self.minutes = minuteInput
        else:
            print('Invalid minute value')

    def setSeconds(self):
        secondInput = input('Please enter second value (Value should be between 0 to 59): ')
        secondInput = int(secondInput)
        if 0 <= secondInput < 60:
            self.seconds = secondInput
        else:
            print('Invalid second value')

    def setTime(self):
        combinedInput = input('Please enter time value (Value should be in format HH MM SS): ')
        combinedInputArr = combinedInput.split(' ')
        self.hours = int(combinedInputArr[0])
        self.minutes = int(combinedInputArr[1])
        self.seconds = int(combinedInputArr[2])

    def showTime(self):
        print(f'Time is {self.hours}:{self.minutes}:{self.seconds}')


clock = ClockTime()
clock.showTime()
clock.setTime()
clock.showTime()
clock.setHours()
clock.setMinutes()
clock.setSeconds()
clock.showTime()
