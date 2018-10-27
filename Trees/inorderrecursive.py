from sampletree import root

#inorder function
def inOrderRecursive(root, result):
    if(not root):
        return
    inOrderRecursive(root.getLeft(), result)
    result.append(root.getData())
    inOrderRecursive(root.getRight(), result)

inorder=[]
inOrderRecursive(root, inorder)

print "Inorder Traversal ", inorder