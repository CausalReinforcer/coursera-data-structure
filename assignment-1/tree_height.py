# python3
import sys
import threading
from collections import defaultdict
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def inverse_dict(d):
    """
        Inverse a dictionary to its inverse mapping of value to set of keys.
        Example:
            d = {a: c, b: c}
            inverse_dict(d) = {c: {a, b}}.
    """
    d_inverse = defaultdict(set)
    for key, value in d.items():
        d_inverse[value].add(key)
    return d_inverse


def get_parent_to_children(parent_array):
    """Get parent node to children set representation of a tree, from the parent array representation."""
    dict_child_to_parent = {
        i: parent_array[i] for i in range(len(parent_array))
    }
    return inverse_dict(dict_child_to_parent)


def get_height_via_breath_first_traverse(map_parent_to_children, current_node, current_height):
    max_height = current_height
    children = map_parent_to_children.get(current_node)
    if children:
        child_height = current_height + 1
        for child in children:
            max_height_sub_tree = get_height_via_breath_first_traverse(
                map_parent_to_children,
                child,
                child_height
            )
            max_height = max(max_height, max_height_sub_tree)
    return max_height


class TreeHeight(object):
    def __init__(self):
        self.count_nodes = int(
            sys.stdin.readline()
        )
        self.parent_array = list(
            map(int, sys.stdin.readline().split())
        )

    def compute_height(self):
        # Replace this code with a faster implementation
        map_parent_to_children = get_parent_to_children(self.parent_array)
        root = min(map_parent_to_children[-1])  # there is only one root node, whose parent node is -1
        return get_height_via_breath_first_traverse(
            map_parent_to_children,
            current_node=root,
            current_height=1
        )


def main():
    tree = TreeHeight()
    print(tree.compute_height())


threading.Thread(target=main).start()

