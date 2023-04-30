class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Trees:
    def __init__(self):
        self.root = None
    def insertion(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            head = self.root
            que = []
            que.append(head)
            while len(que)>0:
                temp = que.pop(0)
                if temp.left == None:
                    temp.left = node
                    return
                elif temp.right == None:
                    temp.right = node
                    return
                else:
                    que.append(temp.left)                    
                    que.append(temp.right)

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
t.insertion(50)
t.insertion(30)
t.insertion(20)
t.insertion(40)
t.insertion(10)
t.insertion(70)
t.insertion(80)
t.inorder()