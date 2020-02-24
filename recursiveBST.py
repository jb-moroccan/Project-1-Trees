class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def printVal(self):
    print(self.val, sep='', end=' ') 

def insertRec(root, val):
  #check to see if the tree is empty and if so, set the value as a new node
  if root == None:
    return Node(val)

  #do not allow duplicate numbers to be inserted
  if val == root.val:
    return root
  #check to see if the value is less than the root's value
  #if so, recursively call insert on the left child 
  elif (val < root.val):
    root.left = insertRec(root.left, val)

  #check to see if the value is greater than the root's value
  #if so, recursively call insert on the right child 
  else:
    root.right = insertRec(root.right, val)
  
  #return the node with the value that was inserted
  return root

def deleteRec(root, val):
  if root == None:
    return root
  elif root.val > val:
    root.left = deleteRec(root.left, val)
    return root
  elif root.val < val:
    root.right = deleteRec(root.right, val)
    return root
  elif val == root.val:
    if root.left == None and root.right == None:
      root = None
      return root
    elif root.left == None:
      curr = root
      root = root.right
      curr = None
      return root
    elif root.right == None:
      curr = root
      root = root.left
      curr = None
      return root
    else:
      maxInLeft = findMaxRec(root.left)
      root.val = maxInLeft.val
      root.left = deleteRec(root.left, maxInLeft.val)
      return root

def findNextRec(root, nextNode, val):

  if root == None:
    return None
  minVal = findMinRec(root)
  
  if val < minVal.val:
    return minVal
  if val == root.val:
    if root.right != None:
      return findMinRec(root.right)
  elif val > root.val:
    if root.left == None:
      return nextNode
    return findNextRec(root.right, nextNode, val)
  else:
    nextNode = root
    return findNextRec(root.left, nextNode, val)
  
  return nextNode

def findPrevRec(root, prevNode, val):

  if root == None:
    return None
  maxVal = findMaxRec(root)

  if val > maxVal.val:
    return maxVal
  if val == root.val:
    if root.left != None:
      return findMaxRec(root.left)
  elif val < root.val:
    if root.right == None:
      return prevNode
    return findPrevRec(root.left, prevNode, val)
  else:
    prevNode = root
    return findPrevRec(root.right, prevNode, val)
  
  return prevNode

def findMinRec(root):
  if root.left != None:
    return findMinRec(root.left)
  return root

def findMaxRec(root):
  if root.right != None:
    return findMaxRec(root.right)
  return root

'''
Given that a BST left children are always less than the parent and a BST right children are always more than the parent:
1) Create an empty array
2) Pass the sort method the root of the tree and empty array
3) If the root is not None
  a)  Recursively call sort on the left subtree
  b)  Append the node's value to the array
  c)  Recursively call sort on the right subtree
4) Return the array
'''
def sort(root, arr):
  if root:
    sort(root.left, arr)
    arr.append(root.val)
    sort(root.right, arr)
  return arr

# added for my sake to print out the tree in a way I can view it
def preOrder(root):
  # print root, left, right
  if root:
    root.printVal()
    preOrder(root.left)
    preOrder(root.right)

#TEST INPUT: Given to make your life easy and see how I #intend for the methods to be used. Feel free to add more #cases on your own! :)

root = insertRec(None, 60)
insertRec(root, 40)
insertRec(root, 40)
insertRec(root, 20)
insertRec(root, 50)
insertRec(root, 10)
insertRec(root, 30)
insertRec(root, -80)
insertRec(root, 70)
insertRec(root, 90)
insertRec(root, 100)

print("Preorder traversal:")
preOrder(root)
print()

print("Min: {}".format(findMinRec(root).val))

nextVal = findNextRec(root, None, 5)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

nextVal = findNextRec(root, None, 100)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

nextVal = findNextRec(root, None, -100)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

prevVal = findPrevRec(root, None, 30)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

prevVal = findPrevRec(root, None, -80)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

prevVal = findPrevRec(root, None, 120)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

deleteRec(root, 45)

print("Preorder traversal:")
preOrder(root)

print()

deleteRec(root, 60)

print("Preorder traversal:")
preOrder(root)

print()

print("Max: {}".format(findMaxRec(root).val))

deleteRec(root, 20)

print("Preorder traversal:")
preOrder(root)

print()

arr = []
sortedBST = sort(root, arr)
print("Sorted BST: {}".format(sortedBST))

