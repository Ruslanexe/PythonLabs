class BinaryTree:
    class Node:
        def __init__(self, content) -> None:
            self.content = content
            self.leftChild = None
            self.rightChild = None

    def __init__(self) -> None:
        self.root = None

    def insert(self, val) -> None:
        if self.root is None:
            self.root = self.Node(val)
            return
        node = self.root
        while node is not None:
            if node.content > val:
                if node.leftChild is None:
                    node.leftChild = self.Node(val)
                    break
                else:
                    node = node.leftChild
            else:
                if node.rightChild is None:
                    node.rightChild = self.Node(val)
                    break
                else:
                    node = node.rightChild

    def print_pos(self, node) -> None:
        if node is None:
            return
        self.print_pos(node.leftChild)
        self.print_pos(node.rightChild)
        if node.content.y > 0:
            print(node.content)

    def print_positive(self) -> None:
        self.print_pos(self.root)

    def print_(self, node) -> None:
        if node is None:
            return
        self.print_(node.leftChild)
        self.print_(node.rightChild)
        print(node.content)

    def print_tree(self) -> None:
        self.print_(self.root)

    def find_by_key(self, key) -> bool:
        if self.root is None:
            return False
        node = self.root
        while node is not None:
            if node.content == key:
                return True
            if node.content > key:
                node = node.leftChild
            else:
                node = node.rightChild
        return False

    def delete_node(self, node, key) -> Node or None:
        if node is None:
            return node
        if key < node.content:
            node.leftChild = self.delete_node(node.leftChild, key)
        elif key > node.content:
            node.rightChild = self.delete_node(node.rightChild, key)
        else:
            if node.leftChild is None:
                tmp = node.rightChild
                return tmp
            elif node.rightChild is None:
                tmp = node.leftChild
                return tmp

            tmp = node.rightChild
            while tmp.leftChild is not None:
                tmp = tmp.leftChild
            node.content = tmp.content
            node.rightChild = self.delete_node(node.rightChild, tmp.content)
        return node

    def delete_chel(self, node) -> None:
        if node is None:
            return
        self.delete_chel(node.leftChild)
        self.delete_chel(node.rightChild)
        node.leftChild = None
        node.rightChild = None

    def delete_tree(self) -> None:
        self.delete_chel(self.root)
        self.root = None

    def delete_negative(self) -> None:
        lst = [self.root]
        i = 0
        while i < len(lst):
            if lst[i].leftChild is not None:
                lst.append(lst[i].leftChild)
            if lst[i].rightChild is not None:
                lst.append(lst[i].rightChild)
            if lst[i].content.x < 0 and lst[i].content.y < 0:
                self.root = self.delete_node(self.root, lst[i].content)
            i += 1
