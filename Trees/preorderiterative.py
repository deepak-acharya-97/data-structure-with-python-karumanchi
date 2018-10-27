from sampletree import root

#preorder function iterative way
def preOrderIterative(root, result):
    if(not root):
        return
    stack = []
    stack.append(root)

    while(stack):
        currentNode=stack.pop()
        result.append(currentNode.getData())
        if(currentNode.getRight()):
            stack.append(currentNode.getRight())
        if(currentNode.getLeft()):
            stack.append(currentNode.getLeft())    #just to make sure that order is data->left->right and we are using stack, that's why pushing right first to left

preOrder=[]
preOrderIterative(root, preOrder)
print "Preorder Iterative ", preOrder