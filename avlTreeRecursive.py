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

  def insertRec(self, root, val):
    #check to see if the tree is empty and if so, set the value as a new node
    if root == None:
      root = avlNode(val)
      return root

    #do not allow duplicate numbers to be inserted
    if val == root.val:
      return root
    #check to see if the value is less than the root's value
    #if so, recursively call insert on the left child 
    elif (val < root.val):
      root.left = self.insertRec(root.left, val)

    #check to see if the value is greater than the root's value
    #if so, recursively call insert on the right child 
    else:
      root.right = self.insertRec(root.right, val)
    
    balanceFactor = self.getBalance(root) 

    if balanceFactor > 1:
      if val < root.left.val:
        return self.rightRotate(root)
      else:
        root.left = self.leftRotate(root.left) 
        return self.rightRotate(root)

    if balanceFactor < -1:
      if val > root.right.val:
        return self.leftRotate(root)
      else:
        root.right = self.rightRotate(root.right) 
        return self.leftRotate(root)

    #return the root
    return root

  def deleteRec(self, root, val):
    if root == None:
      return root
    elif root.val > val:
      root.left = self.deleteRec(root.left, val)
    elif root.val < val:
      root.right = self.deleteRec(root.right, val)
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
        maxInLeft = self.findMaxRec(root.left)
        root.val = maxInLeft.val
        root.left = self.deleteRec(root.left, maxInLeft.val)
    
    if root == None:
      return root

    root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    balanceFactor = self.getBalance(root) 
    
    if balanceFactor > 1:
      if self.getBalance(root.left) >= 0:
        return self.rightRotate(root)
      else:
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)
    if balanceFactor < -1:
      if self.getBalance(root.right) <= 0:
        return self.leftRotate(root)
      else:
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)

    return root

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

  def findNextRec(self, root, nextNode, val):

    if root == None:
      return None
    minVal = self.findMinRec(root)
    
    if val < minVal.val:
      return minVal
    if val == root.val:
      if root.right != None:
        return self.findMinRec(root.right)
    elif val > root.val:
      if root.left == None:
        return nextNode
      return self.findNextRec(root.right, nextNode, val)
    else:
      nextNode = root
      return self.findNextRec(root.left, nextNode, val)
    
    return nextNode

  def findPrevRec(self, root, prevNode, val):

    if root == None:
      return None
    maxVal = self.findMaxRec(root)

    if val > maxVal.val:
      return maxVal
    if val == root.val:
      if root.left != None:
        return self.findMaxRec(root.left)
    elif val < root.val:
      if root.right == None:
        return prevNode
      return self.findPrevRec(root.left, prevNode, val)
    else:
      prevNode = root
      return self.findPrevRec(root.right, prevNode, val)
    
    return prevNode

  def findMinRec(self, root):
    if root.left != None:
      return self.findMinRec(root.left)
    return root

  def findMaxRec(self, root):
    if root.right != None:
      return self.findMaxRec(root.right)
    return root

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

myTree = AVL_Tree() 
root = None

nums = getRandomArray(10000)

for num in nums: 
  root = myTree.insertRec(root, num) 

myTree.preOrder(root)
print()

for num in nums: 
  root = myTree.deleteRec(root, num) 

myTree.preOrder(root)
print()

