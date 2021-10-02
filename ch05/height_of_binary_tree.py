class TNode:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

    
d = TNode('D', None, None)
e = TNode('E', None, None)
f = TNode('F', None, None)
b = TNode('B', d, e)
c = TNode('C', f, None)
root = TNode('A', b, c)


def getHeight(root):
  if root is None:
    return 0

  hLeft = getHeight(root.left)
  hRight = getHeight(root.right)

  return max(hLeft, hRight) + 1

getHeight(root)


##########
# 결과
#
# 3
##########