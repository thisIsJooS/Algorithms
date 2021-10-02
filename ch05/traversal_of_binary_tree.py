def preorder(node):
  if node is not None:
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)
    
    
def inorder(node):
  if node is not None:
    inorder(node.left)
    print(node.data, end = ' ')
    inorder(node.right)

    
def postorder(node):
  if node is not None:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = ' ')
    
    
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


# 알고리즘 테스트
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()


####################
# 결과
#
# A B D E C F
# D B E A F C
# D E B F C A
####################