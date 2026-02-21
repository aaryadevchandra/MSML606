# Example postfix expression represented as a list of string tokens
# This corresponds to: (3 + 4) * 2
expression = ["3", "4", "+", "2", "*"]


# Helper function to check whether a token is a single digit operand.
# We use ASCII range comparison to determine if the character
# is between '0' and '9'.
def is_operand(ele):
    if 48 <= ord(ele) <= 57:
        return True
    return False


# Node class for building the binary expression tree.
# Each node stores:
# - value (operator or operand)
# - left child
# - right child
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Stack class used during tree construction.
# Internally uses a Python list to store nodes.
class Stack:
    def __init__(self):
        self.stack = []

    # Utility method to print stack contents (for debugging)
    def display(self):
        print([node.value for node in self.stack])


# Global stack object used while constructing the tree
stackObj = Stack()


# Supported operators for this assignment
OPS = {"+", "-", "*", "/"}


# Reset function to clear the stack before building a new tree.
# This prevents leftover values from previous calls.
def _reset_tree_stack():
    stackObj.stack = []


# Validates whether a token is a proper operand.
# According to the current implementation, only single digit operands
# are supported.
def _is_valid_operand_token(tok: str) -> bool:
    return isinstance(tok, str) and len(tok) == 1 and is_operand(tok)


# Validates whether a token is a supported operator.
def _is_valid_operator_token(tok: str) -> bool:
    return isinstance(tok, str) and tok in OPS


# Validation function for postfix expression.
# This ensures:
# - Expression is not None
# - Expression is a list
# - Expression is not empty
# - Tokens are either valid operands or supported operators
# - The postfix structure is valid (correct operand/operator balance)
def _validate_postfix_for_tree(expression):

    # Check for None input
    if expression is None:
        raise ValueError("Expression is None")

    # Ensure input is a list
    if not isinstance(expression, list):
        raise TypeError("Expression must be a list of strings")

    # Check empty input
    if len(expression) == 0:
        raise ValueError("Empty postfix expression")

    # Validate each token
    for tok in expression:
        if not isinstance(tok, str):
            raise ValueError("Invalid token type")
        if _is_valid_operand_token(tok):
            continue
        if _is_valid_operator_token(tok):
            continue
        raise ValueError(f"Invalid token: {tok}")

    # Structural validation of postfix expression
    # We simulate stack depth to ensure correctness.
    depth = 0
    for tok in expression:
        if _is_valid_operand_token(tok):
            depth += 1
        else:
            # An operator requires two operands available
            if depth < 2:
                raise ValueError("Malformed postfix: insufficient operands")
            depth -= 1

    # After processing entire expression, exactly one result should remain
    if depth != 1:
        raise ValueError("Malformed postfix: too many operands")


# Safe wrapper for tree creation.
# This function:
# 1) Validates the expression
# 2) Resets the stack
# 3) Calls the original tree-building function
# 4) Ensures exactly one root remains in stack
def safe_create_binary_tree_from_postfix_expression(expression):

    _validate_postfix_for_tree(expression)
    _reset_tree_stack()

    # Build the tree using the original implementation
    root = create_binary_tree_from_postfix_expression(expression)

    # Ensure stack contains exactly one element (the root)
    if len(stackObj.stack) != 1:
        raise ValueError("Malformed postfix: stack did not end with one root")

    return stackObj.stack[0]


# Original function that constructs the binary expression tree.
# Logic:
# - If token is operand → push as node onto stack
# - If token is operator → pop two nodes,
#   make them children of new operator node,
#   push new node back to stack
def create_binary_tree_from_postfix_expression(expression):

    for ele in expression:
        node = Node(ele)

        if is_operand(ele):
            stackObj.stack.append(node)
        else:
            # Pop right and left operands
            ptr2 = stackObj.stack.pop()
            ptr1 = stackObj.stack.pop()

            # Attach operands to operator node
            node.left = ptr1
            node.right = ptr2

            # Push new subtree back to stack
            stackObj.stack.append(node)

    # The last created node is the root
    return node


# Build tree safely
root = safe_create_binary_tree_from_postfix_expression(expression)