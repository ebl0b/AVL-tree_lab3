#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        return super().add(v).balance()

    def delete(self, v):
        return super().delete(v).balance()

    def get_diff(self):
        return 0 if self.is_empty() else self.get_lc().height() - self.get_rc().height()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        root = (self.drr() if self.get_diff() == 2 and self.get_lc().get_diff() == -1 else
                self.srr() if self.get_diff() == 2 else
                self.dlr() if self.get_diff() == -2 and self.get_rc().get_diff() == 1 else
                self.slr() if self.get_diff() == -2 else
                self)
        return root.cons(root.get_lc().balance(), root.get_rc().balance()) if not root.is_empty() else root

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        new_root = self.get_rc()
        self.set_rc(new_root.get_lc())
        new_root.set_lc(self)
        return new_root

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        new_root = self.get_lc()
        self.set_lc(new_root.get_rc())
        new_root.set_rc(self)
        return new_root

    def drr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_lc(self.get_lc().slr())
        return self.srr()

    def dlr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_rc(self.get_rc().srr())
        return self.slr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
