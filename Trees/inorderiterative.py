from sampletree import root

#inorder iterative function
def inOrderIterative(root, result):
    if(not root):
        return
    stack=[]
    currentNode=root
    while stack or currentNode:
        if(currentNode):
            stack.append(currentNode)
            currentNode=currentNode.getLeft()
        else:
            currentNode=stack.pop()
            result.append(currentNode.getData())
            currentNode = currentNode.getRight()

inorder=[]
inOrderIterative(root, inorder)
print "Inorder Traversal ",inorder
