from binarytree import BinaryTreeNode

# Preorder Traversal Function
def preOrderTraversalRecursive(root, result):
    if(not root):
        return
    result.append(root.getData())
    preOrderTraversalRecursive(root.getLeft(), result)
    preOrderTraversalRecursive(root.getRight(), result)

#Creating Binary Tree

root = BinaryTreeNode(1)
root.setLeft(BinaryTreeNode(2))
root.setRight(BinaryTreeNode(3))

root.getLeft().setLeft(BinaryTreeNode(4))
root.getLeft().setRight(BinaryTreeNode(5))

root.getRight().setLeft(BinaryTreeNode(6))
root.getRight().setRight(BinaryTreeNode(7))

preOrderTraversal=[]
preOrderTraversalRecursive(root, preOrderTraversal)

print "Preorder Traversal", preOrderTraversal