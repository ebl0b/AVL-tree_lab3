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

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.is_empty():
            return self
        height_dif = self.get_lc().height() - self.get_rc().height()
        if height_dif >= 2:
            if self.get_lc().get_rc().is_empty():
                new_root = self.srr()
            else:
                new_root = self.dlr()
        elif height_dif <= -2:
            if self.get_rc().get_lc().is_empty():
                new_root = self.slr()
            else:
                new_root = self.drr()
        else:
            new_root = self
        return new_root.cons(new_root.get_lc().balance(), new_root.get_rc().balance())

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        new_root = self.get_rc()
        new_root.set_lc(self)
        self.set_rc(AVL())
        return new_root

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        new_root = self.get_lc()
        new_root.set_rc(self)
        self.set_lc(AVL())
        return new_root

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        new_root = self.get_lc().slr()
        self.set_lc(new_root)
        return self.srr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        new_root = self.get_rc().srr()
        self.set_rc(new_root)
        return self.slr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
