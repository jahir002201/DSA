import hashlib

class MerkleTree:
    def __init__(self, data_blocks):
        self.data_blocks = data_blocks
        self.tree = self.build_tree(data_blocks)

    def hash_function(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, data_blocks):
        # Create leaf nodes
        nodes = [self.hash_function(block) for block in data_blocks]

        # Build the tree from leaf nodes to root
        while len(nodes) > 1:
            nodes = [self.hash_function(nodes[i] + nodes[i + 1]) for i in range(0, len(nodes), 2)]
        
        return nodes[0]  # The root hash

    def get_root(self):
        return self.tree

    def get_leaf_hashes(self):
        # Returns the leaf hashes
        return [self.hash_function(block) for block in self.data_blocks]

# Example usage
if __name__ == "__main__":
    data_blocks = ['data1', 'data2', 'data3', 'data4']
    tree = MerkleTree(data_blocks)
    
    print("Leaf hashes:")
    for leaf in tree.get_leaf_hashes():
        print(leaf)

    print("\nRoot hash:")
    print(tree.get_root())
