class BinaryNode():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.key},{self.left},{self.right}]"

    def insert(self, node):
        if node.key > self.key:
            if self.right != None:
                return self.right.insert(node)
            self.right = node
        else:
            if self.left != None:
                return self.left.insert(node)
            self.left = node

    def find(self, key):
        if key == self.key:
            return self.key
        if key < self.key and self.left != None:
            return self.left.find(key)
        if key > self.key and self.right != None:
            return self.right.find(key)

    def delete(self, key):
        """
        Deletes the parameter key from the set
        """
        parent = self
        if parent.left and key < parent.key:
            to_delete = parent.left
            if to_delete.key == key:
                if to_delete.right == None:
                    parent.left = to_delete.left
                elif to_delete.left == None:
                    parent.left = to_delete.right
                else:
                    to_delete_child = to_delete.right
                    if to_delete_child.left == None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
                    # current.key = parent.del_min()
            else:
                to_delete.delete(key)
        elif parent.right and key > parent.key:
            to_delete = parent.right
            if to_delete.key == key:
                if to_delete.right == None:
                    parent.right = to_delete.left
                elif to_delete.left == None:
                    parent.right = to_delete.right
                else:
                    to_delete_child = to_delete.right
                    if to_delete_child.left == None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
                    # current.key = parent.del_min()
            else:
                to_delete.delete(key)
        else:
            raise ValueError(f"could not delete {key}")

    def del_min(self):
        """
            Returns value of minimum of subtree self
            Deletes node of minimum value
        """
        start_node = self
        potential_min = start_node.left
        if potential_min.left == None:
            k = potential_min.key
            start_node.left = potential_min.right
            return k
        else:
            return potential_min.del_min()