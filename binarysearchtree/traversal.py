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
    def maxValueNode(self,node):
        current = node
        while current.right != None:
            current = current.right
        return current
        

    def __deletion(self,root,data):
        if root == None:
            return root
            
        if root.left == None and root.right == None:
            if(root.data == data):
                return None
            return root

        if root.data > data:
            root.left = self.__deletion(root.left,data)
            
        elif root.data < data:
            root.right = self.__deletion(root.right,data)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            temp = self.maxValueNode(root.left)

            root.data = temp.data
            root.left = self.__deletion(root.left,temp.data)
    
        return root 

    def deletion(self,data):
        self.root = self.__deletion(self.root, data); 

    def __inorder(self, root):
        if(root == None):
            return
        self.__inorder(root.left)
        print(root.data, end=" ")
        self.__inorder(root.right)
    def inorder(self):
        head = self.root
        self.__inorder(head)
        print()
        
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
t.insert(30)
t.insert(20)
t.insert(10)
t.insert(40)
t.insert(25)
print('inorder')
t.inorder()
print('preorder')
t.preorder()
print('postorder')
t.postorder()
