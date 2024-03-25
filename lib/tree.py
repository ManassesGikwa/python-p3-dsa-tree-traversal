class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None

        # Define a helper function for depth-first traversal
        def dfs(node):
            if node['id'] == id:
                return node
            for child in node['children']:
                result = dfs(child)
                if result:
                    return result
            return None

        # Start depth-first traversal from the root node
        return dfs(self.root)
