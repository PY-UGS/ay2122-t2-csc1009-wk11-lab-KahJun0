class Calculator:

    def __init__(self):
        self.result = 0
        self.x = input('Please enter first value: ')
        self.x = float(self.x)
        self.y = input('Please enter second value: ')
        self.y = float(self.y)

    def add(self):
        self.result = self.x + self.y
        print(f'{self.x} + {self.y} = {self.result}')

    def subtract(self):
        self.result = self.x - self.y
        print(f'{self.x} - {self.y} = {self.result}')

    def multiplier(self):
        self.result = self.x * self.y
        print(f'{self.x} * {self.y} = {self.result}')

    def divider(self):
        self.result = self.x / self.y
        print(f'{self.x} / {self.y} = {self.result}')

    def clear(self):
        self.result = 0


calc = Calculator()
calc.add()
calc.subtract()
calc.multiplier()
calc.divider()
calc.clear()

