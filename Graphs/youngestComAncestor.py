# Medium graph problem

# You're given 3 inputs, all of which are instances of a class that
# have an "ancestor" property pointing to their youngest ancestor. The first
# input is the top ancestor in an ancestral tree (the only instance)
# that has no ancestor), and the other 2 inputs are descendants in the
# ancestral tree. Write a function that returns the youngest common ancestor
# to the 2 descendants.

# Sample input:
#       A
#      /  \
#     B    C
#    / \  / \
#   D   E F  G
#  / \
# H   I

# Sample output: B


def getYoungestComminAncestor(topAncestor, descendantOne, descendantTwo):
    return 0