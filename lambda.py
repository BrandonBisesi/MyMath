"""
  Calculates Standard Deviation.
"""

import json

def average(nums):
  """
    Calculates average of list of numbers.
  """
  sum = 0
  for num in nums:
    sum += num
  return sum / len(nums)


def std_dev(event, context):
  """
    Calculates standard deviation using a list of numbers.
  """
  nums = event["nums"]
  avg = average(nums)
  value = 0
  for num in nums:
    value += (num - avg) ** 2
  result = (value / (len(nums) - 1)) ** 0.5
  return {"StatusCode": 200,
          "nums": nums,
          "std_dev": result}



