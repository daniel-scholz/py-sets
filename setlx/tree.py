from setlx.node import BinaryNode


class Tree():
    def __init__(self, node=None):
        self.root = None
        self.total = 0
        if node != None:
            self.insert(node)  # ensures that total count is correct
    """Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.(https://www.programiz.com/python-programming/iterator)"""

    def __iter__(self):
        """
        returns the iterator object
        """
        # self.prev_index = None if self.index == None else self.index
        self.index = 0
        # minimum of the tree
        return self

    def __next__(self):
        if self.index < self.total:
            old_i = self.index
            self.index += 1
            return self[old_i]
        else:
            # self.index = self.prev_index
            raise StopIteration

    def __getitem__(self, index):
        if index < 0:
            index = self.total - abs(index)
        return self.root[index]

    def insert(self, node):
        if not isinstance(node, BinaryNode):
            node = BinaryNode(node)
        if self.root == None:
            self.root = node
            self.total += 1
        else:
            self.total += self.root.insert(node)

    def _find(self, key):
        if self.root != None:
            return self.root._find(key)

    # extracts key from node
    def find(self, key):
        result = self._find(key)
        if result != None:
            return result.key
        return result

    def delete(self, key):
        tree = self
        if tree.root != None:
            root = tree.root
            if root.key == key:
                # check if right subtree i  s minimum
                if root.right == None:
                    tree.root = root.left
                elif root.left == None:
                    tree.root = root.right
                else:
                    root_right = root.right
                    if root_right.left == None:
                        root.right = root_right.right
                        root.key= root_right.key
                    else:
                        # parent.key = current.del_min()
                        root.key= root_right.del_min()
            else:
                tree.root.delete(key)
            self.total -= 1

        else:
            raise ValueError(f"tree is empty")

    # def min(self):
    #     """ returns node with min key"""
    #     if self.root != None:
    #         if self.root.left == None:
    #             return self.root
    #         else:
    #             return self.root.min()
    #     raise ValueError(f"tree is empty")

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"

    def __eq__(self, other):
        if self.root != None or other.root != None:
            return self.root == other.root
        else:  # elif other == None:
            if self.root == None and other.root == None:
                return True
            return False

    def _traverse(self):
        # https://stackoverflow.com/questions/8991840/recursion-using-yield
        # yield self.root
        yield from self.root._traverse()

    def __le__(self, other):  # a.k.a. is_subset
        """
        corresponds to self <= other
        implements check for subset, NOT real less or equal
        other is subset of self; all elements of self are in other
        """
        if self.root == None:  # left set is empty
            return True
        if other.root == None:  # right set is empty
            return False
        if other.root != None and self.root != None:
            # root_eq = other.find(self.root.key)
            for node in self:
                if not other.find(node.key):
                    return False
            return True

    def __lt__(self, other):
        """
        implements check for real subset, NOT real less
        """
        return self != other and self <= other

    def __gt__(self, other):
        """
        returns self > other 
        """
        return other < self

    def __ge__(self, other):
        """
        returns self >= other  
        """
        return other <= self
