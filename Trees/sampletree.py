from binarytree import BinaryTreeNode

#Creating Binary Tree

root = BinaryTreeNode(1)
root.setLeft(BinaryTreeNode(2))
root.setRight(BinaryTreeNode(3))

root.getLeft().setLeft(BinaryTreeNode(4))
root.getLeft().setRight(BinaryTreeNode(5))

root.getRight().setLeft(BinaryTreeNode(6))
root.getRight().setRight(BinaryTreeNode(7))