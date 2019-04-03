def flatten(root: TreeNode) -> None:
    if root is None or root.left is None and root.right is None:
        return

    if root.left is not None:
        self.flatten(root.left)

    temp = root.right
    root.right, root.left = root.left, None

    end = root.right
    while end.right is not None:
        end = end.right
    end.right = temp
