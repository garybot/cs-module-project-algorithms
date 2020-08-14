#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  solution = {"Value": 0, "Chosen": []}
  weight = 0    
  # items.sort(key = lambda x : x.value / x.size)
  # for i in range(len(items)-1, -1, -1):    
  items.sort(key = lambda x : x.size / x.value)
  for i in range(len(items)):
    if items[i].size + weight <= capacity:
      weight += items[i].size
      solution["Value"] += items[i].value
      solution["Chosen"].append(items[i].index)
  solution["Chosen"].sort() # tests expect chosen items to be ordered
  return solution


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')