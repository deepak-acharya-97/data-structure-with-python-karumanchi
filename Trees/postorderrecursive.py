from sampletree import root

#post order function
def postOrderRecursive(root, result):
    if(not root):
        return
    postOrderRecursive(root.getLeft(), result)
    postOrderRecursive(root.getRight(), result)
    result.append(root.getData())

postorder=[]
postOrderRecursive(root, postorder)
print "Postorder Traversal", postorder