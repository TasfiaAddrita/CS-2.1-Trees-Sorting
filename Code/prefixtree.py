#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    # look at how to use _find_node to complete this method
    def contains(self, string):
        """
        Return True if this prefix tree contains the given string.
        
        Time complexity: 
            let M = length of given string
            Best: O(1), if first char of string is not a child of the root node
            # Average: O(M)
            Worst: O(M) 
        
        Space complexity: O(1), no extra memory is utilized
        """

        node, depth = self._find_node(string)
        # if string is 'ABC' then node = ('C'), depth = 3

        return depth == len(string) and node.is_terminal()

        # if depth == len(string):
        #     return node.is_terminal()
        # return False
    
        # old implementation;
        # node = self.root
        # for char in string: # O(n)
        #     if not node.has_child(char): # O(1)
        #         return False
        #     node = node.get_child(char) # O(1)
        # return node.is_terminal() # O(1)

    def insert(self, string):
        """
        Insert the given string into this prefix tree.
        
        Time complexity: 
            let M = length of string
            Best: O(M), even if the string exists in the tree, still have to traverse through all characters
            Average: O(M)
            Worst: O(M)
        
        Space complexity: 
            Best: O(1), if the string already exists in the tree, no need to make a new child node
            Worst: O(M), adding a single child node every iteration (M child nodes)
        """
        node, depth = self._find_node(string)
        for char in string[depth:]:
            # if not node.has_child(char): # O(1) # always true when inserting a new node
            node.add_child(char, PrefixTreeNode(char)) # O(1) 
            node = node.get_child(char) # O(1)
        if not node.is_terminal(): # O(1)
            node.terminal = True
            self.size += 1

        # node = self.root
        # for char in string: # O(n)
        #     if not node.has_child(char): # O(1)
        #         node.add_child(char, PrefixTreeNode(char)) # O(1)
        #     node = node.get_child(char) # O(1)
        # if not node.is_terminal(): # O(1)
        #     node.terminal = True
        #     self.size += 1

    def _find_node(self, string):
        """
        Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node.
        
        Time complexity: 
            let M = length of string
            Best: O(M)
            Average: O(M)
            Worst: O(M)
        
        Space complexity: O(1)
        """
        # Match the empty string
        # Start with the root node
        node = self.root
        depth = 0
        for char in string:
            if node.has_child(char):
                node = node.get_child(char)
                depth += 1
            else:
                # print(string, 'break loop')
                break
        return node, depth

        # 1st iteration: char: 'A', node: root -> ('A'), depth: 0 -> 1
        # 2nd iteration: char: 'J', node: ('A') -> break, depth: 1
        # skips 3rd iteration: char: 'B', node: ('A') -> ('B'), depth: 1 -> 2
        # returns ('A'), 1
        
    def complete(self, prefix):
        """
        Return a list of all strings stored in this prefix tree that start
        with the given prefix string.
        
        Time complexity: 
            let M = length of string
            Best: 
            Average: 
            Worst: 
        
        Space complexity:
        """
        # Create a list of completions in prefix tree
        completions = []
        node, depth = self._find_node(prefix) # a partial string can be found but still fail
        # print(node, depth)
        if depth == 0: 
            return []
        self._traverse(node, prefix, completions.append)
        return completions

    def strings(self):
        """
        Return a list of all strings stored in this prefix tree.
        
        Time complexity: 
            let N = number of nodes in the tree
            Best: O()
            Average: 
            Worst: 
        
        Space complexity:
        """
        # Create a list of all strings in prefix tree
        all_strings = []
        self._traverse(self.root, "", all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """
        Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        
        Time complexity: 
            let ...
            Best: 
            Average: 
            Worst: 
        
        Space complexity:
        """
        if node.is_terminal():
            visit(prefix)
        
        for char in node.children:
            child = node.get_child(char)
            self._traverse(child, prefix + char, visit)
    
    def delete(self, string):
        # node = self._find_node()
        pass


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
