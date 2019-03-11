class Node():
    """
    setting up node class
    """
    def __init__(self, data):
        self.data = data
        self.left = None   
        self.right = None  

    def insert(self, data):
        if data < self.data: #if value is less than root
            if self.left is None: #if there is currently nothing on the left
                self.left = Node(data) #left parent node is now value
            else:
                self.left.insert(data) #insert value on left
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self, value):
        if value < self.data: #go to the left sub-tree
            if self.left is None: #if left sub-tree is empty
                return False
            return self.left.search(value) #repeat
        if value > self.data: #go to the right sub-tree
            if self.right is None: #if right sub-tree is empty
                return False
            return self.right.search(value) #repeat
        return True

    def in_order_traversal(self, root):
        """
        # Traverse the left subtree, i.e., call Inorder(left-subtree)
        # Visit the root.
        # Traverse the right subtree, i.e., call Inorder(right-subtree)
        """
        tree = []
        if root is not None: #if root isn't empty then it can be traversed
            tree = self.in_order_traversal(root.left) #traverse the right sub-tree
            tree.append(root.data) #append the root after the left and before the right
            tree = tree + self.in_order_traversal(root.right) #traverse the right sub-tree
        return tree

    def pre_order_traversal(self, root):
        """
        # Visit the root
        # Traverse the left subtree, i.e., call Preorder(left-subtree)
        # Traverse the right subtree, i.e., call Preorder(right-subtree)
        """
        tree = []
        if root is not None: #if root isn't empty then it can be traversed
            tree.append(root.data) #append the root as this is visited first
            tree = tree + self.pre_order_traversal(root.left) #traverse the left sub-tree
            tree = tree + self.pre_order_traversal(root.right)#traverse the right sub-tree
        return tree

    def post_order_traversal(self, root):
        """
        # Traverse the left subtree, i.e., call Postorder(left-subtree)
        # Traverse the right subtree, i.e., call Postorder(right-subtree)
        # Visit the root.
        """
        tree = []
        if root is not None: #if root isn't empty then it can be traversed
            tree = self.post_order_traversal(root.left) #traverse the left sub-tree
            tree = tree + self.post_order_traversal(root.right) #traverse the right sub-tree
            tree.append(root.data) #append the root last as it is the last thing visited.
        return tree


new = Node(45) 
new.insert(13) 
new.insert(35) 
new.insert(16) 
new.insert(12) 
new.insert(49) 
new.insert(27) 
new.insert(53) 
new.insert(88)
new.insert(72)  
print("inOrder traversal")
print(new.in_order_traversal(new))
print("preOrder traversal")
print(new.pre_order_traversal(new))
print("postOrder traversal")
print(new.post_order_traversal(new))
print(new.search(27))
print(new.search(9))
print(new.search(88))
