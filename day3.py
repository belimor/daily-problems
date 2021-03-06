#!/usr/bin/python3
#
# https://en.wikipedia.org/wiki/Binary_tree
# Given the root to a binary tree, 
# implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
#  
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        #node = Node(int(val))
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('1', Node('2', Node('2.2')), Node('3'))
print(serialize(node))
print(deserialize(serialize(node)).left.left.val)
assert deserialize(serialize(node)).left.left.val == '2.2'
