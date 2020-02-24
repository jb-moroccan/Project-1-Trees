import random
def getRandomArray(n):
  arr = []
  while len(arr) < n:
    val = random.randint(1,n)
    if val not in arr:
      arr.append(val)
  return arr

def getSortedArray(arr):
  newArr = sorted(arr,reverse=True)
  return newArr

vals = getRandomArray(10)
print(vals)
print(getSortedArray(vals))