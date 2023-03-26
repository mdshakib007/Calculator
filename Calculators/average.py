class Average:
    def __init__(self):
        self.sum = 0
        self.count = 0
    
    @classmethod    
    def from_input(cls):
        values = input("Enter a list of values separated by commas: ").split(",")
        values = [float(value) for value in values]
        instance = cls()
        instance.add(values)
        return instance

    def add(self, values):
        for value in values:
            self.sum += value
            self.count += 1
            
    def calculate(self):
        if self.count == 0:
            return 0
        else:
            avg = self.sum / self.count
            return f"The average value is: {avg:.2f}"


if __name__ == "__main__":
	avg = Average.from_input()
	print(avg.calculate())
