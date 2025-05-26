from tree_node import Node

def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = Node(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree_pre_in(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_pre_in(preorder[mid+1:], inorder[mid+1:])
    return root
