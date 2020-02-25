class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def printVal(self):
    print(self.val, sep='', end=' ') 

# added for my sake to print out the tree in a way I can view it
def preOrder(root):
  # print root, left, right
  if root:
    root.printVal()
    preOrder(root.left)
    preOrder(root.right)

def insertIter(root, val):

  current = root
  parent = None

  if root == None:
    root = Node(val)
    return root
  
  while current != None:
    parent = current

    if val == current.val:
      return root
    elif val < current.val:
      current = current.left
    else:
      current = current.right

  if val < parent.val:
    parent.left = Node(val)
  else:
    parent.right = Node(val)

  return root

def deleteIter(root, val):

  current = root
  parent = None
  
  if root == None:
    return None

  if parent == None and root.left == None and root.right == None and val == root.val:
    root.val = None
    return root

  while val != current.val:
    parent = current
    if val > current.val:
      if current.right != None:
        current = current.right
      else:
        return None
    elif val < current.val:
      if current.left != None:
        current = current.left
      else:
        return None
  
  if current.left == None and current.right == None:
    if parent.left == current:
      parent.left = None
    else:
      parent.right = None
  elif current.left == None:
    if parent != None:
      if parent.left == current:
        parent.left = current.right
      else:
        parent.right = current.right
      return root
    else:
      #root = current.right
      current.val = current.right.val
      leftSubtree = current.right.left
      rightSubtree = current.right.right
      current.left = leftSubtree
      current.right = rightSubtree
      return current
  elif current.right == None:
    if parent != None:
      if parent.left == current:
        parent.left = current.left
      else:
        parent.right = current.left
      return root
    else:
      current.val = current.left.val
      leftSubtree = current.left.left
      rightSubtree = current.left.right
      current.left = leftSubtree
      current.right = rightSubtree
      return current
  else:
    parent = current
    nextNode = current.left
    if nextNode.right == None and nextNode.left != None:
      current.val = current.left.val
      leftSubtree = current.left.left
      current.left = leftSubtree
      return current
    
    while nextNode.right != None:
      parent = nextNode
      nextNode = nextNode.right
    current.val = nextNode.val
    if parent.right == nextNode:
      parent.right = None
    else:
      parent.left = None
    return parent
  return root

def findNextIter(root, val):
  nextNode = None
  curr = root

  if root == None:
    return None
  
  while curr != None and curr.val != val:
    if curr.val > val:
      nextNode = curr
      curr = curr.left
    else:
      curr = curr.right

  if curr != None and curr.right != None:
    nextNode = findMinIter(curr.right)
  
  return nextNode

def findPrevIter(root, val):
  prevNode = None
  curr = root

  if root == None:
    return None
  
  while curr != None and curr.val != val:
    if curr.val < val:
      prevNode = curr
      curr = curr.right
    else:
      curr = curr.left

  if curr != None and curr.left != None:
    prevNode = findMaxIter(curr.left)
  
  return prevNode

def findMinIter(root):
  parent = None
  while root != None:
    parent = root
    root = root.left
  return parent

def findMaxIter(root):
  parent = None
  while root != None:
    parent = root
    root = root.right
  return parent

#TEST INPUT: Given to make your life easy and see how I #intend for the methods to be used. Feel free to add more #cases on your own! :)

root = insertIter(None, 60)
insertIter(root, 40)
insertIter(root, 40)
insertIter(root, 20)
insertIter(root, 50)
insertIter(root, 10)
insertIter(root, 30)
insertIter(root, 80)
insertIter(root, 70)
insertIter(root, 90)
insertIter(root, 100)
insertIter(root, 110)

print("Preorder traversal:")
preOrder(root)
print()

print("Min: {}".format(findMinIter(root).val))

nextVal = findNextIter(root, 5)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

nextVal = findNextIter(root, 110)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

nextVal = findNextIter(root, -100)
if nextVal == None:
  print("nextVal is higher than max element in tree")
else:
  print("nextVal: {}".format(nextVal.val))

prevVal = findPrevIter(root, 30)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

prevVal = findPrevIter(root, -80)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

prevVal = findPrevIter(root, 120)
if prevVal == None:
  print("prevVal is less than min element in tree")
else:
  print("prevVal: {}".format(prevVal.val))

deleteIter(root, 45)

print("Preorder traversal:")
preOrder(root)

print()

deleteIter(root, 60)

print("Preorder traversal:")
preOrder(root)

print()

print("Max: {}".format(findMaxIter(root).val))

deleteIter(root, 20)

print("Preorder traversal:")
preOrder(root)

print()
