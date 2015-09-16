#!/usr/bin/env python

import unittest
from bst import *

class BSTTest(unittest.TestCase):
    def setUp(self):
        self.tree1 = BST()
        self.tree1.insert(23)
        self.tree1.insert(8)
        self.tree1.insert(4)
        self.tree1.insert(16)
        self.tree1.insert(15)
        self.tree1.insert(42)
    
    def testInsert(self):
        tree2 = BST()
        tree2.insert(5)
        tree2.check_ri()
        self.assertEqual(5, tree2.find(5).key)
        tree2.insert(3)
        tree2.check_ri()
        self.assertEqual(3, tree2.find(3).key)
        tree2.insert(4)
        tree2.check_ri()
        self.assertEqual(4, tree2.find(4).key)
        tree2.insert(4)
        tree2.check_ri()
        self.assertEqual(4, tree2.find(4).key)
    
    def testFind(self):
        tree2 = BST()
        self.assertIsNone(tree2.find(3))
        tree2.insert(4)
        self.assertIsNone(tree2.find(3))
    
    def testDeleteNodeWithoutChildren(self):
        d = self.tree1.delete(15)
        self.tree1.check_ri()
        self.assertEqual(15, d.key)
        self.assertIsNone(self.tree1.find(15))
    
    def testDeleteNodeWithOneChild(self):
        d = self.tree1.delete(16)
        self.tree1.check_ri()
        self.assertEqual(16, d.key)
        self.assertIsNone(self.tree1.find(16))
        
    def testDeleteNodeWithTwoChildren(self):
        d = self.tree1.delete(8)
        self.tree1.check_ri()
        self.assertEqual(8, d.key)
        self.assertIsNone(self.tree1.find(8))
        
    def testDeleteRoot(self):
        d = self.tree1.delete(23)
        self.tree1.check_ri()
        self.assertEqual(23, d.key)
        self.assertIsNone(self.tree1.find(23))
        self.assertEqual(42, self.tree1.find(42).key)
        
    def testDelateLastNode(self):
        tree2 = BST()
        tree2.insert(1)
        deleted = tree2.delete(1)
        self.assertEqual(1, deleted.key)
        tree2.check_ri()
        tree2.insert(2)
        tree2.check_ri()
    
    def testNextLarger(self):
        self.assertEqual(15, self.tree1.next_larger(8).key)
        self.assertEqual(23, self.tree1.next_larger(16).key)
        
    def testFindMin(self):
        tree2 = BST()
        self.assertIsNone(tree2.find_min())
        tree2.insert(5)
        self.assertEqual(5, tree2.find(5).key)
        self.assertEqual(5, tree2.find_min().key)
        self.assertEqual(4, self.tree1.find_min().key)

class MinBSTTest(unittest.TestCase):
    def setUp(self):
        self.tree1 = MinBST()
        self.tree1.insert(23)
        self.tree1.insert(8)
        self.tree1.insert(4)
        self.tree1.insert(16)
        self.tree1.insert(15)
        self.tree1.insert(42)
        
    def testInsert(self):
        tree2 = MinBST()
        tree2.insert(5)
        self.assertEqual(5, tree2.find(5).key)
        tree2.insert(3)
        self.assertEqual(3, tree2.find(3).key)
        tree2.insert(4)
        self.assertEqual(4, tree2.find(4).key)
        tree2.insert(4)
        self.assertEqual(4, tree2.find(4).key)
    
    def testDeleteNodeWithoutChildren(self):
        d = self.tree1.delete(15)
        self.assertEqual(15, d.key)
        self.assertIsNone(self.tree1.find(15))
        self.assertEqual(4, self.tree1.find_min().key)
    
    def testDeleteNodeWithOneChild(self):
        d = self.tree1.delete(16)
        self.assertEqual(16, d.key)
        self.assertIsNone(self.tree1.find(16))
        self.assertEqual(4, self.tree1.find_min().key)
        
    def testDeleteNodeWithTwoChildren(self):
        d = self.tree1.delete(8)
        self.assertEqual(8, d.key)
        self.assertIsNone(self.tree1.find(8))
        self.assertEqual(4, self.tree1.find_min().key)
        
    def testDeleteRoot(self):
        d = self.tree1.delete(23)
        self.assertEqual(23, d.key)
        self.assertIsNone(self.tree1.find(23))
        self.assertEqual(42, self.tree1.find(42).key)
        self.assertEqual(4, self.tree1.find_min().key)
        
    def testFindMin(self):
        self.assertEqual(4, self.tree1.find_min().key)
        self.tree1.delete(4)
        self.assertEqual(8, self.tree1.find_min().key)
        
if __name__ == '__main__':
    unittest.main()
        