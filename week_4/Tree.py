class Node:
    def __init__(self,data = None, list = []):
        self.data = data
        self.list = list
    
    # def __str__(self,level =0) -> str:
    #     s=" "* level + str(self.data) + "\n"
    #     for i in self.list:
    #         s += i.__str__(level+1)
    #     return s

    def addChild(self,treeNode):
        self.list.append(treeNode)

class Tree:
    def __init__(self,rootNode = None):
        self.root = rootNode

    

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
tree = Tree(a)
a.addChild(b)
a.addChild(c)
b.addChild(d)
b.addChild(e)


# print(a)