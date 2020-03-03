# AVL tree
import random

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

    y = node.right 
    x = y.left 

    y.left = node 
    node.right = x 

    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
    y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 

    return y 

  def rightRotate(self, node): 

    y = node.left 
    x = y.right 

    y.right = node 
    node.left = x 

    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
    y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 

    return y 

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


# Test Input 

myTree = AVL_Tree() 
root = None

nums = getRandomArray(10000)

for num in nums: 
  root = myTree.insertIter(root, num) 

myTree.preOrder(root)
print()
