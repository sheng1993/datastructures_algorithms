class Node:
    def __init__(self, key, parent=None):
        self.parent = parent    # type: Node
        self.left = None        # type: Node
        self.right = None       # type: Node
        self.key = key          # type: any
        self.height = 1


def is_leaf(node: Node):
    return node.right is None and node.left is None


def is_balanced(node: Node):
    return abs(node.left.height - node.right.height) <= 1


def adjust_height(node: Node):
    node.height = 1 + max(node.left.height, node.right.height)

def find(key, root: Node) -> Node:
    if root.key == key:
        return root
    elif root.key > key:
        if root.left is not None:
            return find(key, root.left)
    else:
        if root.right is not None:
            return find(key, root.right)
    return root


def left_descendant(root: Node) -> Node:
    if root.left is None:
        return root
    else:
        return left_descendant(root.left)


def right_ancestor(root: Node) -> Node:
    if root.key < root.parent.key:
        return root.parent
    else:
        return right_ancestor(root.parent)


def next_node(root: Node) -> Node:
    if root.right is not None:
        return left_descendant(root.right)
    else:
        return right_ancestor(root)


def range_search(x, y, root: Node) -> list:
    l = list()
    n = find(x, root)
    while n.key <= y:
        if n.key >= x:
            l.append(n)
        n = next_node(n)
    return l


def insert(key, root):
    n = find(key, root)
    if key < n.key:
        if n.left is None:
            n.left = Node(key=key, parent=n)
    elif key > n.key:
        if n.right is None:
            n.right = Node(key=key, parent=n)

    x = n
    adjust_height(x)
    while x.parent is not None:
        x = x.parent
        adjust_height(x)


def delete(node: Node):
    if node.right is None:
        if node.key < node.parent.key:
            node.parent.left = node.left
        elif node.key > node.parent.key:
            node.parent.right = node.left
    else:
        x = next_node(node)
        node.parent.left = x.right
        x.right = node.right
        x.left = node.left
        x.parent = node.parent

        node.parent = None
        node.right = None
        node.left = None


def rotate_right(node: Node):
    p = node.parent
    y = node.left
    b = node.right
    y.parent = p
    if p.key > y.key:
        p.left = y
    else:
        p.right = y
    node.parent = y
    y.right = node
    b.parent = node
    node.left = b

