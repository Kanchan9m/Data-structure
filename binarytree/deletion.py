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
    
    def deletion(self,data):

        if self.root == None:
            return None
        if self.root.left == None and self.root.right == None:
            if self.root.data == data:
                return None
            else:
                return self.root
        
        key_node = None
        head = self.root
        q = []
        q.append(head)
        temp = None
        while (len(q)):
            temp = q.pop(0)
            if temp.data == data:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.data
            self.deletedeepest(temp)
            key_node.data = x
        return self.root

    def deletedeepest(self,d_node):
        head = self.root
        q = []
        q.append(head)
        while len(q):
            temp = q.pop(0)
            if temp == d_node:
                temp = None
                return
            if temp.right:
                if temp.right == d_node:
                    temp.right = None
                    return 
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left == d_node:
                    temp.left = None
                    return 
                else:
                    q.append(temp.left)

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
t.insert(10)
t.insert(20)
t.insert(30)
t.insert(40)
t.insert(50)
t.insert(45)
t.insert(35)
t.inorder()
print('after deletion')
t.deletion(50)
t.deletion(20)
t.deletion(40)
t.inorder()