# Example postfix expression.
# This corresponds to the infix expression: (3 + 4) * 2
expression = ["3", "4", "+", "2", "*"]


# Set of supported operators for this assignment.
OPS = {"+", "-", "*", "/"}


# Helper function to check whether a token is a valid operator.
# Only operators in OPS are considered valid.
def is_operator(tok: str) -> bool:
    return tok in OPS


# Helper function to check whether a token represents a valid number.
# This supports:
# - Positive integers (e.g., "3", "12")
# - Negative integers (e.g., "-5")
def is_number_token(tok: str) -> bool:
    if tok.startswith("-") and tok[1:].isdigit():
        return True
    return tok.isdigit()


# Node class used to represent each element of the expression tree.
# Each node stores:
# - value (either operand or operator)
# - left child
# - right child
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Stack class used during tree construction.
# It internally uses a Python list to store nodes.
class Stack:
    def __init__(self):
        self.stack = []

    # Utility function for debugging purposes.
    # Displays the current values stored in the stack.
    def display(self):
        print([node.value for node in self.stack])


# Global stack object used to construct the expression tree.
stackObj = Stack()


# Function to construct a binary expression tree from a postfix expression.
# Logic:
# - If token is a number → push it as a node onto the stack.
# - If token is an operator → pop two nodes, make them children
#   of a new operator node, then push the new node back.
# - At the end, exactly one node (the root) must remain in the stack.
def create_binary_tree_from_postfix_expression(expression):

    for ele in expression:
        node = Node(ele)

        # If token is a number, push as leaf node
        if is_number_token(ele):
            stackObj.stack.append(node)

        # If token is a valid operator, pop two operands
        elif is_operator(ele):
            ptr2 = stackObj.stack.pop()   # Right child
            ptr1 = stackObj.stack.pop()   # Left child

            node.left = ptr1
            node.right = ptr2

            stackObj.stack.append(node)

        # If token is neither operand nor operator, raise error
        else:
            raise ValueError(f"Invalid token: {ele}")
        
    # After processing entire expression,
    # the stack must contain exactly one element (the root).
    if len(stackObj.stack) != 1:
        raise ValueError("Malformed postfix: too many operands")

    return node


# Build the expression tree and obtain the root node
root = create_binary_tree_from_postfix_expression(expression=expression)


# Helper function to display stack values (if needed)
def display_stack(stack):
    print([node.value for node in stack])


# Preorder traversal (Prefix notation).
# Order: root → left → right
# Values are appended into the provided output list.
def preorder_traversal(node, out):

    if node != None:
        out.append(node.value)
        preorder_traversal(node.left, out)
        if node.right != None:
            preorder_traversal(node.right, out)


def inorder_traversal(node, out):
    if node is None:
        return

    # If this is a leaf (operand), just append the value
    if node.left is None and node.right is None:
        out.append(node.value)
        return

    # Otherwise, it's an operator expression: wrap in parentheses
    out.append("(")
    inorder_traversal(node.left, out)
    out.append(node.value)
    inorder_traversal(node.right, out)
    out.append(")")


# Postorder traversal (Postfix notation).
# Order: left → right → root
def postorder_traversal(node, out):
    if node != None:
        postorder_traversal(node.left, out)
        postorder_traversal(node.right, out)
        out.append(node.value)
        

# Lists to store traversal outputs
preorder_traversal_output = []
inorder_traversal_output = []
postorder_traversal_output = []

# Perform traversals
preorder_traversal(root, preorder_traversal_output)
inorder_traversal(root, inorder_traversal_output)
postorder_traversal(root, postorder_traversal_output)

# Print traversal results
print(preorder_traversal_output)   # Expected: ['*', '+', '3', '4', '2']
print(inorder_traversal_output)    # Expected: ['3', '+', '4', '*', '2']
print(postorder_traversal_output)  # Expected: ['3', '4', '+', '2', '*']