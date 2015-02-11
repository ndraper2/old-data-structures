class Node(object):
    def __init__(self, val, parent=None, left_child=None, right_child=None):
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class Heap(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val)
            return
        placed_node = self.find_open_spot(None, self.head, val)
        print placed_node.val
        holder = placed_node.val
        try:
            while holder > placed_node.parent.val:
                placed_node.val = placed_node.parent.val
                placed_node.parent.val = holder
                placed_node = placed_node.parent
        except AttributeError:
            pass

    def pop(self):
        self.head.val = self.find_and_destroy_last_node(self.head)
        self.check_values(self.head, self.head.val)
        pass

    def check_values(self, iter_node, val):
        try:
            if iter_node.left_child.val > val:
                iter_node.val = iter_node.left_child.val
                iter_node.left_child.val = val
                self.check_values(iter_node.left_child, iter_node.left_child.val)

            if iter_node.right_child.val > val:
                iter_node.val = iter_node.right_child.val
                iter_node.right_child.val = val
                self.check_values(iter_node.right_child, iter_node.right_child.val)
        except AttributeError:
            return

    def has_right_sibling(self, iter_node):
        try:
            return iter_node.parent.left_child
        except AttributeError:
            return False

    def find_and_destroy_last_node(self, iter_node):
        try:
            self.find_and_destroy_last_node(iter_node.left_child)
            self.find_and_destroy_last_node(iter_node.right_child)
            self.find_and_destroy_last_node(self.has_right_sibling(iter_node))
            iter_val = iter_node.val
            iter_node = None
            return iter_val
        except AttributeError:
            return

    def find_open_spot(self, iter_parent, iter_node, val):
        try:
            if not iter_node.left_child:
                iter_node.left_child = self.find_open_spot(iter_node, iter_node.left_child, val)
                return iter_node.left_child
            if not iter_node.right_child:
                iter_node.right_child = self.find_open_spot(iter_node, iter_node.right_child, val)
                return iter_node.right_child
            if self.has_right_sibling(iter_node):
                self.find_open_spot(iter_node.parent, self.has_right_sibling(iter_node), val)
            self.find_open_spot(iter_node, iter_node.left_child, val)
        except AttributeError:
            return Node(val, iter_parent)

        # try:
        #     if iter_node.left_child:
        #         if iter_node.right_child:
        #             if self.has_right_sibling(iter_node):
        #                 return self.find_open_spot(iter_node.parent, iter_node.parent.right_child, val)
        #         else:
        #             return self.find_open_spot(iter_node, iter_node.right_child, val)
        #     else:
        #         return self.find_open_spot(iter_node, iter_node.left_child, val)
        # except AttributeError:
        #     iter_node = Node(val, iter_parent)
        #     return iter_node