from tree_node import Node
from traversals import preorder, inorder, postorder, level_order
from constructors import build_tree_pre_in

# Manually creating the tree:
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F

a = Node('A')
a.left = Node('B')
a.right = Node('C')
a.left.left = Node('D')
a.left.right = Node('E')
a.right.right = Node('F')

print("Preorder:", preorder(a))      # ['A', 'B', 'D', 'E', 'C', 'F']
print("Inorder:", inorder(a))        # ['D', 'B', 'E', 'A', 'C', 'F']
print("Postorder:", postorder(a))    # ['D', 'E', 'B', 'F', 'C', 'A']
print("Level Order:", level_order(a))# ['A', 'B', 'C', 'D', 'E', 'F']

# Reconstructing from traversals
pre = ['A', 'B', 'D', 'E', 'C', 'F']
ino = ['D', 'B', 'E', 'A', 'C', 'F']
reconstructed = build_tree_pre_in(pre, ino)
print("Reconstructed Preorder:", preorder(reconstructed))  # Should match original
