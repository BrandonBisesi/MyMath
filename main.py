"""
  Calculates Standard Deviation.
"""

def average(nums):
  """
    Calculates average of list of numbers.
  """
  sum = 0
  for num in nums:
    sum += num
  return sum / len(nums)


def standard_dev(nums):
  """
    Calculates standard deviation using a list of numbers.
  """
  avg = average(nums)
  sum = 0
  for num in nums:
    sum += (num - avg) ** 2
  result = sum / (len(nums) - 1)
  return result ** 0.5


nums = [1,2,3,4,5,6,7,8,9,10]

std_dev = standard_dev(nums)

print("result:",std_dev)



