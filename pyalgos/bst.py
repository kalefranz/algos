class Node:
    height = 0

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    # @property
    # def has_child(self):
    #     return bool(self.left or self.right)

    # @property
    # def has_both_children(self):
    #     return bool(self.left and self.right)

    # @property
    # def has_grandchild(self):
    #     return self.has_child and (self.left.has_child or self.right.has_child)
    
    # @property
    # def is_balanced(self):
    #     if not self.has_child or self.has_both_children:
    #         return True
    #     if self.left is None:
    #         pass
    #     else:
    #         assert self.right is None
        


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        
        def _attach_node(node):
            if value == node.value:
                return None
            elif value < node.value:
                if node.left is None:
                    node.left = new_node
                    return node
                else:
                    return _attach_node(node.left)
            else:
                if node.right is None:
                    # attach here
                    node.right = new_node
                    return node
                else:
                    return _attach_node(node.right)

        _attach_node(self.root)

        return self
    
    def find(self, value):
        if not self.root:
            return None

        def _find(node):
            if node.value == value:
                return node
            elif value < node.value:
                if node.left is None:
                    return None
                else:
                    return _find(node.left)
            else:
                if node.right is None:
                    return None
                else:
                    return _find(node.right)
        
        return _find(self.root)

            



bst = BinarySearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(10)
bst.insert(9)
bst.insert(11)
bst.insert(14)

print(bst.find(10))
print(bst.find(8))
print(bst.find(2))
