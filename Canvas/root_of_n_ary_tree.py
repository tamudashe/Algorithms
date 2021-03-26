"""
Given all the nodes of an N-ary tree as an array Node[]
tree where each node has a unique value.

Find and return the root of the N-ary tree.
"""


class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []


"""
Time complexity: O(n)
Space complexity: O(n)
"""
def find_root(tree):
    children = set()
    for node in tree:
        for child in node.children:
            children.add(child)

    for node in tree:
        if node not in children:
            return node

    return Node()


"""
Time complexity: O(n)
Space complexity: O(1)
"""
def find_root_improved(tree):
    total = 0
    for node in tree:
        total += node.value

        for child in node.children:
            total -= child.value

    for node in tree:
        if node.value == total:
            return node

    return Node()


def main():
    node5 = Node(5)
    node6 = Node(6)
    node2 = Node(2, [node5, node6])
    node3 = Node(3)
    node4 = Node(4)
    node1 = Node(1, [node2, node3, node4])

    tree = [node1, node2, node3, node4, node5, node6]

    print(find_root(tree).value)
    print(find_root_improved(tree).value)


if __name__ == '__main__':
    main()
