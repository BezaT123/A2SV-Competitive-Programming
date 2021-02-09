class BSTNode:
    def __init__(self,data = None) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def __str__(self) -> str:
        return "" + str(self.data)

def insertNode(rootNode,nodeValue):
    while True:
        # print(rootNode)
        # if rootNode is None:
        #     rootNode = BSTNode(nodeValue)
        #     print(rootNode.datal)
        #     break
        if rootNode.data < nodeValue:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
                break
            else:
                rootNode = rootNode.rightChild
        elif rootNode.data > nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
                break
            rootNode = rootNode.leftChild
def preOrderTraversal(rootNode):
    # list =[]
    print(rootNode, end=" ")
    if rootNode.leftChild is not None:
        preOrderTraversal(rootNode.leftChild)
        # print(rootNode)
    if rootNode.rightChild is not None:
        preOrderTraversal(rootNode.rightChild)

def inOrder(rootNode):
    if rootNode.leftChild is not None:
        inOrder(rootNode.leftChild)
    print(rootNode, end =" ")
    if rootNode.rightChild is not None:
        inOrder(rootNode.rightChild)


a = BSTNode(7)
# print(a.leftChild,a.rightChild)
insertNode(a,5)
# print(a.leftChild,a.rightChild)

insertNode(a,9)
# print(a.leftChild,a.rightChild)

insertNode(a,10)
# print(a.leftChild,a.rightChild)
insertNode(a,6)
insertNode(a,3)
insertNode(a,8)
inOrder(a)
# print(a.leftChild.leftChild,a.rightChild.rightChild)
