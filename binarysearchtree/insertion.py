class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Trees:
    def __init__(self) -> None:
        self.root = None
    def insert(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            head = self.root
            temp = head
            while True:
                if temp.data >data:
                    if temp.left == None:
                        temp.left = node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = node
                        return
                    else:
                        temp = temp.right

    def __inorder(self, root):
        if(root == None):
            return
        self.__inorder(root.left)
        print(root.data, end=" ")
        self.__inorder(root.right)

    def inorder(self):
        head = self.root
        self.__inorder(head)
        
t = Trees()
t.insert(30)
t.insert(20)
t.insert(10)
t.insert(40)
t.insert(25)
t.inorder()
