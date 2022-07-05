"""
    Math class that has average and standard deviation calculations.
"""

class MyMath:

    def __init__(self):
        self.num_list = []
        self.avg = 0
        self.std_dev = 0
        self.maximum = 0

    def add_to_list(self, num):
        """
            adds number to list
        """
        self.num_list.append(int(num))

    def calc(self):
        """
            calculates average, max and standard deviation
        """
        self.avg = self.average()
        self.std_dev = self.standard_dev()
        self.maximum = max(self.num_list)

    def clear(self):
        """
            Clears all values to 0 or empty
        """
        self.num_list = []
        self.avg = 0
        self.std_dev = 0
        self.maximum = 0

    def average(self):
        """
            Calculates average using a list of numbers.
        """
        sum = 0
        for num in self.num_list:
            sum += num
        return sum / len(self.num_list)


    def standard_dev(self):
        """
            Calculates standard deviation using a list of numbers.
        """
        avg = self.average()
        sum = 0
        for num in self.num_list:
            sum += (num - avg) ** 2
        result = sum / (len(self.num_list) - 1)
        return result ** 0.5


