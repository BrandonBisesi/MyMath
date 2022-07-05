"""Contains MyMath class that has average and standard deviation calculations."""

class MyMath:
    """MyMath class with average and standard deviation calcuations."""
    def __init__(self, num_list):
        try:
            self.num_list = num_list
        except Exception as e:
            print("Exception: "  + str(e.__class__) + " Error occured in init")


    def average(self):
        """Calculates average using a list of numbers."""
        try:
            addition = 0
            for number in self.num_list:
                try:
                    addition += number
                except Exception as e:
                    print("Exception: " + str(e.__class__) + " Error occured in average method loop")
            return addition / len(self.num_list)
        except ZeroDivisionError:
            print("Exception: " + str(e.__class__) + " Error occured in average method - Number list is empty")
        except Exception as e:
            print("Exception: " + str(e.__class__) + " Error occured in average method")


    def standard_dev(self):
        """Calculates standard deviation using a list of numbers."""
        try:
            avg = self.average()
            value = 0
            for number in self.num_list:
                try:
                    value += (number - avg) ** 2
                except Exception as e:
                    print("Exception: " + str(e.__class__) + " Error occured in standard_dev method loop")

            result = value / (len(self.num_list) - 1)
            return result ** 0.5
        except ZeroDivisionError:
            print("Exception: " + str(e.__class__) + " Error occured in standard_dev method - Number list must contain 2 or more numbers")
        except Exception as e:
            print("Exception: " + str(e.__class__) + " Error occured in standard_dev method")


try:
    num_list = []
    while True:
        try:
            num = input("Enter number or leave blank to exit: ")
            if num:
                try:
                    num_list.append(float(num))
                except ValueError:
                    print("Exception: Please enter a number.")
                except Exception as e :
                    print("Exception: " + str(e.__class__))
            else:
                break
        except Exception as e:
            print("Exception: " + str(e.__class__) + " Error occured ")

    number_list = MyMath(num_list)

    print("Average:", number_list.average())
    print("Standard Deviation:", number_list.standard_dev())
except Exception as e:
    print("Exception: " + str(e.__class__) + " Error occured ")