class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Trees:
    def __init__(self):
        self.root = None
    def insert(self,data):
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
    
    def __preorder(self,root):
        if (root == None):
            return
        print(root.data, end = ' ')
        self.__preorder(root.left)
        self.__preorder(root.right)
    def preorder(self):
        head = self.root
        self.__preorder(head)

    def __postorder(self,root):
        if root == None:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data,end = ' ')
    def postorder(self):
        head = self.root
        self.__postorder(head)

t = Trees()
t.insert(50)
t.insert(30)
t.insert(20)
t.insert(40)
t.insert(10)
print('inorder')
t.inorder()
print('preorder')
t.preorder()
print('postorder')
t.postorder()