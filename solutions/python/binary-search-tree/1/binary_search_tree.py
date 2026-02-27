from collections import deque


class TreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data: str = data
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data: list[str]):
        self.tree_data = tree_data
        self.root = TreeNode(tree_data[0])

    def __str__(self) -> str:
        return str([i.__str__() for i in self.tree_data])

    def insert(self, root: TreeNode | None, data: str):
        if root is None:
            return TreeNode(data)

        # Recur down the tree
        if int(data) <= int(root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Return the (unchanged) node pointer
        return root

    def data(self) -> TreeNode:
        prev_node = self.root

        for index, data in enumerate(self.tree_data):
            if index == 0:
                continue

            new_node = self.insert(prev_node, data)

            prev_node = new_node

        return self.root

    def sorted_data(self) -> list[str]:
        return sorted(self.tree_data)
