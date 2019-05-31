class SearchTreeNode:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.children = [left, right]
        self.deleted = False

    def __str__(self):
        return str("Node with item " + str(self.item))

    def get_child_for_key(self, key):
        return self.children[int(key > self.key)]

    def set_child_for_key(self, key, child):
        self.children[int(key > self.key)] = child

class BinarySearchTree:
    def __init__(self):
        """
        Constructor to initialize the value
        """
        self.root = None
        self.probe_total = 0
        self.probe_max = 0
    def __setitem__(self, key, item):
        self.probe = 0
        self.root = self._setitem_aux(self.root, key, item)
        if self.probe > self.probe_max:
            self.probe_max = self.probe
        self.probe_total += self.probe

    def _setitem_aux(self, node, key, item):
        """
        Precondtion: It is an recusive call for the base function
        :param node: The SearchTreeNode with having value
        :param key: A string
        :param item: The assigning value for the key
        :return: The SearchedTreeNode
        @complexity: The Best Case would be the O(h) and the worst case would be the O(n)
                     where h and n are depth of binary tree and number of the nodes respectively.
        """


        if node is None:
            node = SearchTreeNode(key, item)
        else:

            if node.key == key:
                #we replace
                node.item = item
            else:
                self.probe += 1
                node.set_child_for_key(key,
                self._setitem_aux(node.get_child_for_key(key), key, item))
        return node

    def __getitem__(self, key):
        """
         It gets the item according to the assigned key
        :param key: A string
        :return: The assigned value for the key
        """

        return self._getitem_aux(self.root, key)

    def _getitem_aux(self, node, key):
        """
       It is recurssive call function for the get item
        :param node: The SearchTreeNode with having value
        :param key: A string
        :param item: The assigned value for the key
        @complexity: The Best Case would be the O(h) and the worst case would be the O(n)
                     where h and n are depth of binary tree and number of the nodes respectively.
        """
        if node is None or node.deleted is True:
            raise KeyError("key not found")
        if key == node.key:
            return node.item
        else:
            return self._getitem_aux(node.get_child_for_key(key), key)

    def __contains__(self, key):
        """
        Tt checks the key return the value boolean value according to that
        :param key: A string to assigned the value
        :return: Return the boolean Value depends upon the key
        @complexity:he Best Case would be the O(h) and the worst case would be the O(n)
                     where h and n are depth of binary tree and number of the nodes respectively
        """
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def  __delitem__(self, key):
        """We only implement a lazy deletion.
           See slides for "classic" deletion."""
        self._delitem_aux(self.root, key)

    def _delitem_aux(self, node, key):
        """

        :param node: The SearchTreeNode with having value
        :param key: A string which assigned the value
        :return: No return Value
        @complexity:he Best Case would be the O(h) and the worst case would be the O(n)
                     where h and n are depth of binary tree and number of the nodes respectively
        """
        if node is None:
            raise KeyError("key not found")
        if key == node.key:
            node.deleted = True
        else:
            self._delitem_aux(node.get_child_for_key(key), key)
    def getProbe(self):
        return [self.probe_total, self.probe_max]