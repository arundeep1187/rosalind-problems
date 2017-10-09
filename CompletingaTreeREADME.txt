This program solves the Completing a Tree problem in two ways. It
will first find every disconnected node through a series of tests on
every node to find where it exists on this graph. First, the program
will calculate the number of degrees of each node. If the node is not
connected to any other node (or has a degree of 0), it will be added
to the list of disconnected nodes. If a node is a leaf (or has a
degree of 1), the program will find the node it connects to, add one
and eliminate the other from the list. If a node is an internal node
(or has a degree of 2 or greater), the program will find its path and
treat the full path as one disconnected node while eliminating the
other nodes in path from the list. The length of the list of
disconnected nodes will then be the answer. Since, however, the rule
to find edges on a graph is number of nodes - 1, the "easy solution"
is written as number of nodes - 1 - length of the list of given
edges. Both will arrive at the correct answer.
(Note: Testing this program requires the rosalind_tree.txt file,
also located in this repository)
