import hashlib

class MerkleNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MerkleTree:
    def __init__(self, data_list):
        self.root = self.build_tree(data_list)

    def build_tree(self, data_list):
        if len(data_list) == 0:
            return None
        if len(data_list) == 1:
            return MerkleNode(data_list[0])

        mid = len(data_list) // 2
        left_subtree = self.build_tree(data_list[:mid])
        right_subtree = self.build_tree(data_list[mid:])
        return self.create_merkle_node(left_subtree, right_subtree)

    def create_merkle_node(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        combined_data = left.data + right.data
        node = MerkleNode(hashlib.sha256(combined_data).digest())
        node.left = left
        node.right = right
        return node

    def get_root(self):
        return self.root

    def __str__(self):
        return self.print_tree(self.root)

    def print_tree(self, node):
        if node is None:
            return ''
        if node.left is None and node.right is None:
            return node.data.hex()
        left_hash = self.print_tree(node.left)
        right_hash = self.print_tree(node.right)
        combined_hash = left_hash + right_hash
        return hashlib.sha256(combined_hash.encode()).digest().hex()

# Example usage:
if __name__ == "__main__":
    data_list = [b"Data1", b"Data2", b"Data3", b"Data4"]
    merkle_tree = MerkleTree(data_list)
    print("Merkle Root:", merkle_tree.get_root().data.hex())
    print("Merkle Tree:")
    print(merkle_tree)
