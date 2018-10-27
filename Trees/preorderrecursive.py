from sampletree import root

# Preorder Traversal Function
def preOrderTraversalRecursive(root, result):
    if(not root):
        return
    result.append(root.getData())
    preOrderTraversalRecursive(root.getLeft(), result)
    preOrderTraversalRecursive(root.getRight(), result)

preOrderTraversal=[]
preOrderTraversalRecursive(root, preOrderTraversal)

print "Preorder Traversal", preOrderTraversal