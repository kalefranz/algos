
class Vertex:
    height = -1
    desc_count = 0

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def rotate_left(cls, vertex):
        assert vertex.right is not None
        new_parent = vertex.right
        old_left = new_parent.left
        new_parent.left = vertex
        vertex.right = old_left
        vertex.calculate_height()
        new_parent.calculate_height()
        return new_parent

    @classmethod
    def rotate_right(cls, vertex):
        assert vertex.left is not None
        new_parent = vertex.left
        old_right = new_parent.right
        new_parent.right = vertex
        vertex.left = old_right
        vertex.calculate_height()
        new_parent.calculate_height
        return new_parent

    def __str__(self):
        if not self.left and not self.right:
            return f"{self.val}"
        else:
            return f"{self.val}({self.left or ''}){self.right and f'({self.right})' or ''}"
    
    def calculate_height(self):
        height = max(self.left and self.left.height or 0, self.right and self.right.height or 0) + 1
        self.height = height
        self.desc_count = (self.left and (self.left.desc_count+1) or 0) + (self.right and (self.right.desc_count+1) or 0)
        return height
    
    @property
    def balance_factor(self):
        return (self.left and self.left.height or 0) - (self.right and self.right.height or 0)
    
    def find(self, val):
        if val == self.val:
            return self
        elif val < self.val:
            return self.left.find(val)
        else:
            return self.right.find(val)
    


def insert(vrtx, val):
    # Step 1. Do normal BST
    if not vrtx:
        vrtx = Vertex(val)
        vrtx.calculate_height()
        return vrtx
    elif vrtx.val == val:
        return vrtx
    elif val < vrtx.val:
        vrtx.left = insert(vrtx.left, val)
    else:
        vrtx.right = insert(vrtx.right, val)    
    vrtx.calculate_height()

    # Step 2. If node is not balanced, then run through four cases
    balance_factor = vrtx.balance_factor
    if balance_factor >= 2:
        bf = vrtx.left.balance_factor
        if bf == 1:
            return Vertex.rotate_right(vrtx)
        elif bf == -1:
            vrtx.left = Vertex.rotate_left(vrtx.left)
            return Vertex.rotate_right(vrtx)
    if balance_factor <= -2:
        bf = vrtx.right.balance_factor
        if bf == -1:
            return Vertex.rotate_left(vrtx)
        elif bf == 1:
            vrtx.right = Vertex.rotate_right(vrtx.right)
            return Vertex.rotate_left(vrtx)

    return vrtx
    

# root = insert(None, 50)
# root = insert(root, 40)
# root = insert(root, 30)
# print(root)

# root = Vertex(1)
# root.left = Vertex(2)
# root.right = Vertex(3)
# root.left.right = Vertex(4)
# print(root)

# nums = [5,2,6,1]
# root = None
# for x in nums:
#     root = insert(root, x)
# print(root)
# print([root.find(x).desc_count for x in nums])


# ## https://leetcode.com/problems/count-of-smaller-numbers-after-self/
nums = [7,8,3,4,5,2,6,1]
root = None
for x in reversed(nums):
    root = insert(root, x)
    print(x, root)
    target = root.find(x)

    # print(smaller_branch and smaller_branch.desc_count or 0)
