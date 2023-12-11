#!/usr/bin/env python3

import bt
import sys
import logging
from collections import deque

log = logging.getLogger(__name__)


class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        # Returns true if the value `v` is a member of the tree.
        return (False if self.is_empty() else
                self.get_lc().is_member(v) if v < self.get_value() else
                self.get_rc().is_member(v) if v > self.get_value() else
                True)

    def size(self):
        # Returns the number of nodes in the tree.
        l_size = self.get_lc().size() if self.get_lc() else 0
        r_size = self.get_rc().size() if self.get_rc() else 0
        return (0 if self.is_empty() else
                1 + l_size + r_size)

    def height(self):
        # Returns the height of the tree.
        l_height = self.get_lc().height() if self.get_lc() else -1
        r_height = self.get_rc().height() if self.get_rc() else -1
        return (0 if self.is_empty() else
                1 + max(l_height, r_height))

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().postorder() + self.get_rc().postorder() + [self.get_value()]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by None.
        '''
        if self.is_empty():
            return []
        queue = deque([self])
        results = [None for x in range((2**self.height())-1)]
        for i in range(len(results)):
            curr = queue.popleft()
            if curr:
                results[i] = curr.get_value()
                queue.append(curr.get_lc() if curr.get_lc() else None)
                queue.append(curr.get_rc() if curr.get_rc() else None)
            else:
                queue.append(None)
                queue.append(None)
        return results

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self

    def smallest(self):
        return (None if self.is_empty() else
                self.get_lc().smallest() if not self.get_lc().is_empty() else
                self)

    def biggest(self):
        return (None if self.is_empty() else
                self.get_rc().biggest() if not self.get_rc().is_empty() else
                self)

    def empty(self):
        self.set_value(None)
        self.set_lc(None)
        self.set_rc(None)
        return self

    def relocate(self, leaf):
        retval = self.set_value(leaf.get_value())
        (leaf.empty() if leaf.get_lc().is_empty() and leaf.get_rc().is_empty() else
         leaf.rem())
        return retval

    def rem(self):
        left_node = self.get_lc().biggest()
        right_node = self.get_rc().smallest()
        return (self.empty() if self.get_lc().is_empty() and self.get_rc().is_empty() else
                self.relocate(left_node) if right_node is None else
                self.relocate(right_node) if left_node is None else
                self.relocate(left_node) if self.get_lc().height() >= self.get_rc().height() else
                self.relocate(right_node))

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        return (self if self.is_empty() else
                self.cons(self.get_lc().delete(v), self.get_rc()) if v < self.get_value() else
                self.cons(self.get_lc(), self.get_rc().delete(v)) if v > self.get_value() else
                self.rem())

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
