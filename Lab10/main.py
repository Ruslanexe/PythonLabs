from binary_tree import *
from point import *

tree = BinaryTree()
tree.insert(Point(1, 1))
tree.insert(Point(1, -1))
tree.insert(Point(-1, 1))
tree.insert(Point(2, -2))
tree.insert(Point(2, 2))
tree.insert(Point(3, -1.5))
tree.insert(Point(-2, 3))

tree.print_positive()
