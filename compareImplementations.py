# AVL tree
import random

levels = 0
totalLevels = 0
class avlNode: 
  def __init__(self, val): 
    self.val = val 
    self.left = None
    self.right = None
    self.height = 1
  def printVal(self):
    print(self.val, sep='', end=' ') 

class AVL_Tree: 
  def insertIter(self, root, val): 
    global levels
    global totalLevels
    if not root: 
      return avlNode(val)

    current = root
    parent = None
    path = []

    while current != None:
      path.append(current)
      parent = current
      if val == current.val:
        return root
      elif val < current.val:
        current = current.left
      else:
        current = current.right
      
    if val < parent.val:
      parent.left = avlNode(val)
    else:
      parent.right = avlNode(val)
    
    prevNode = root
    levels += len(path)
    totalLevels += len(path)
    while len(path) > 0:
      nextPop = path.pop()
      nextPop.height = 1 + max(self.getHeight(nextPop.left), self.getHeight(nextPop.right)) 
  
      balanceFactor = self.getBalance(nextPop) 

      if balanceFactor > 1:
        if val < nextPop.left.val:
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.rightRotate(nextPop)
            else:
              peekPop.left = self.rightRotate(nextPop)
          else:
            return self.rightRotate(nextPop)
        else:
          nextPop.left = self.leftRotate(nextPop.left) 

          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.rightRotate(nextPop)
            else:
              peekPop.left = self.rightRotate(nextPop)
          else:
            return self.rightRotate(nextPop)

      if balanceFactor < -1:
        if val > nextPop.right.val:
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.leftRotate(nextPop)
            else:
              peekPop.left = self.leftRotate(nextPop)
          else:
            return self.leftRotate(nextPop)
          #self.leftRotate(nextPop)
        else:
          nextPop.right = self.rightRotate(nextPop.right) 
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.leftRotate(nextPop)
            else:
              peekPop.left = self.leftRotate(nextPop)
          else:
            return self.leftRotate(nextPop)

      prevNode = nextPop
            
    return prevNode

  def deleteIter(self, root, val): 

    if root == None:
      return root 

    current = root
    parent = None
    path = []
    foundVal = False

    while current != None:
      if val < current.val:
        path.append(current)
        parent = current
        current = current.left
      elif val > current.val:
        path.append(current)
        parent = current
        current = current.right
      else:
        foundVal = True
        break

    if foundVal == False:
      return root

    if current.val == root.val and root.left == None and root.right == None:
      return None
    # delete node based on 3 cases 
  
    # leaf node (no children)
    if current.left == None and current.right == None:
      if parent.left == current:
        parent.left = None
      else:
        parent.right = None
    # 1 Child
    elif current.left == None:
      if parent != None:
        if parent.left == current:
          parent.left = current.right
        else:
          parent.right = current.right
      else:
        current.val = current.right.val
        leftSubtree = current.right.left
        rightSubtree = current.right.right
        current.left = leftSubtree
        current.right = rightSubtree
    elif current.right == None:
      if parent != None:
        if parent.left == current:
          parent.left = current.left
        else:
          parent.right = current.left
      else:
        current.val = current.left.val
        leftSubtree = current.left.left
        rightSubtree = current.left.right
        current.left = leftSubtree
        current.right = rightSubtree
    # two children
    else:
      parent = current
      nextNode = current.left
      if nextNode.right == None and nextNode.left != None:
        current.val = current.left.val
        leftSubtree = current.left.left
        current.left = leftSubtree
      else:
        while nextNode.right != None:
          parent = nextNode
          nextNode = nextNode.right
        current.val = nextNode.val
        if parent.right == nextNode:
          parent.right = None
        else:
          parent.left = None

    prevNode = root
    
    while len(path) > 0:
      nextPop = path.pop()
      nextPop.height = 1 + max(self.getHeight(nextPop.left), self.getHeight(nextPop.right)) 
  
      balanceFactor = self.getBalance(nextPop) 

      if balanceFactor > 1:
        if self.getBalance(nextPop.left) >= 0:
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.rightRotate(nextPop)
            else:
              peekPop.left = self.rightRotate(nextPop)
          else:
            return self.rightRotate(nextPop)
        else:
          nextPop.left = self.leftRotate(nextPop.left)
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.rightRotate(nextPop)
            else:
              peekPop.left = self.rightRotate(nextPop)
          else:
            return self.rightRotate(nextPop)

      if balanceFactor < -1:
        if self.getBalance(nextPop.right) <= 0:
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.leftRotate(nextPop)
            else:
              peekPop.left = self.leftRotate(nextPop)
          else:
            return self.leftRotate(nextPop)
        else:
          nextPop.right = self.rightRotate(nextPop.right) 
          if len(path) > 0:
            peekPop = self.pathPeek(path)
            if peekPop.right == nextPop:
              peekPop.right = self.leftRotate(nextPop)
            else:
              peekPop.left = self.leftRotate(nextPop)
          else:
            return self.leftRotate(nextPop)

      prevNode = nextPop

    return prevNode

  def leftRotate(self, node): 

    rightSub = node.right 
    leftRightSub = rightSub.left 
    rightSub.left = node 
    node.right = leftRightSub

    #update heights after rotation
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
    rightSub.height = 1 + max(self.getHeight(rightSub.left), self.getHeight(rightSub.right)) 

    return rightSub

  def rightRotate(self, node): 

    leftSub = node.left 
    rightLeftSub = leftSub.right 
    leftSub.right = node 
    node.left = rightLeftSub

    #update heights after rotation
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
    leftSub.height = 1 + max(self.getHeight(leftSub.left), self.getHeight(leftSub.right)) 

    return leftSub

  def getHeight(self, root): 
    if root: 
      return root.height 
    return 0

  def getBalance(self, root): 
    if root: 
      return self.getHeight(root.left) - self.getHeight(root.right)
    return 0
  
  def pathPeek(self, path):
    prevNode = path.pop()
    path.append(prevNode)
    return prevNode

  def findNextIter(self, root, val):
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
      nextNode = self.findMinIter(curr.right)
    
    return nextNode

  def findPrevIter(self, root, val):
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
      prevNode = self.findMaxIter(curr.left)
    
    return prevNode

  def findMinIter(self, root):
    parent = None
    while root != None:
      parent = root
      root = root.left
    return parent
  
  def findMaxIter(self, root):
    parent = None
    while root != None:
      parent = root
      root = root.right
    return parent

  def preOrder(self, root): 
      if root: 
        root.printVal()
        self.preOrder(root.left) 
        self.preOrder(root.right) 

#iterative BST

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def printVal(self):
    print(self.val, sep='', end=' ') 

def insertIter(root, val):
  global levelsBST
  global totalLevelsBST
  current = root
  parent = None

  if root == None:
    root = Node(val)
    return root
  
  while current != None:
    levelsBST += 1
    totalLevelsBST += 1
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

def preOrder(root):
  # print root, left, right
  if root:
    root.printVal()
    preOrder(root.left)
    preOrder(root.right)

# Question 6 b

print("Question 6 b")
print()
myTree = AVL_Tree() 
root = None 
nums = getRandomArray(10000)

for num in nums: 
  levels = 0
  root = myTree.insertIter(root, num) 
  #print("Levels Traversed to insert {} in AVL: {}".format(num, levels))


print()
print("Iterative AVL Tree")
#myTree.preOrder(root)
print()
print("Total levels traversed (all inserts): ", totalLevels)

levelsBST = 0
totalLevelsBST = 0
bstIterRoot = None

first = True
for num in nums:
  levelsBST = 0
  if first:
    bstIterRoot = insertIter(bstIterRoot, num)
  else:
    insertIter(bstIterRoot, num)
  #print("Levels Traversed to insert {} in BST: {}".format(num, levelsBST))

print()
print("Iterative BST")
#preOrder(bstIterRoot)
print()
print("Total levels traversed (all inserts): ", totalLevelsBST)

# Question 6 c
print()
print("Question 6 c")
print()
myTree2 = AVL_Tree() 
root2 = None 
nums2 = getRandomArray(10000)
sortedNums = getSortedArray(nums2)

for num in sortedNums: 
  levels = 0
  root2 = myTree2.insertIter(root2, num) 
  #print("Levels Traversed to insert {} in AVL: {}".format(num, levels))

print()
print("Iterative AVL Tree")
#myTree.preOrder(root)
print()
print("Total levels traversed (all inserts): ", totalLevels)
print()

levelsBST = 0
totalLevelsBST = 0
bstIterRoot = None

first = True
for num in sortedNums:
  levelsBST = 0
  if first:
    bstIterRoot = insertIter(bstIterRoot, num)
  else:
    insertIter(bstIterRoot, num)
  #print("Levels Traversed to insert {} in BST: {}".format(num, levelsBST))


print("Iterative BST")
#preOrder(bstIterRoot)
print()
print("Total levels traversed (all inserts): ", totalLevelsBST)
