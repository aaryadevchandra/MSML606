# Example postfix expression.
# This corresponds to:
# 5 + ((1 + 2) * 4) - 3
expression = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]

# Set of supported operators
OPS = {"+", "-", "*", "/"}


# Helper function to determine whether a token is a single-digit operand.
# It checks whether the ASCII value of the character lies between '0' and '9'.
def is_operand(ele):
    if 48 <= ord(ele) <= 57:
        return True
    return False


# Node class used during evaluation.
# Each node stores:
# - value (operand or intermediate result)
# - left child
# - right child
# Even though this is evaluation-only, nodes are used to maintain
# consistency with the tree-based approach.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Stack class implemented using a list.
# This follows the Stack ADT concept:
# - push() adds element to top
# - pop() removes element from top
# - top index is manually maintained
class Stack:

    def display(self):
        print([node.value for node in self.data])

    def __init__(self):
        self.data = []
        self.top = -1  # manually track the top position

    # Push element onto stack and update top pointer
    def push(self, x):
        self.data.append(x)
        self.top += 1

    # Pop element from stack with underflow protection
    def pop(self):
        if self.top < 0:
            raise IndexError("Pop from empty stack")
        x = self.data[self.top]
        self.data.pop()
        self.top -= 1
        return x

    # Returns current number of elements in stack
    def size(self):
        return self.top + 1


# Helper function to classify operators.
# Returns a short code for easier branching during evaluation.
def op_code(operator: str):
    if operator == "+":
        return "a"
    elif operator == "-":
        return "s"
    elif operator == "*":
        return "m"
    else:
        return "d"


# Stack object used for evaluation
stackObj = Stack()


# Function to evaluate a postfix expression using a stack.
# Requirements satisfied:
# - Accepts postfix expression as list
# - Validates tokens
# - Uses stack logic
# - Handles division by zero
# - Raises appropriate errors for malformed input
def evaluate_postfix_expression(expression, stackObj):

    # Edge case: expression is None
    if expression is None:
        raise ValueError("Expression is None")

    # Ensure expression is a list
    if not isinstance(expression, list):
        raise TypeError("Expression must be a list of elements")

    # Edge case: empty expression
    if len(expression) == 0:
        raise ValueError("Empty postfix expression")
    
    # Process each token in postfix order
    for ele in expression:

        # Validate token type
        if not isinstance(ele, str):
            raise ValueError(f"Invalid element type: {type(ele).__name__}")

        # Reject empty string tokens
        if ele == "":
            raise ValueError("Invalid element: empty string")

        # Only single-character tokens supported
        if len(ele) != 1:
            raise ValueError(f"Invalid element (must be single character): {ele}")

        # Ensure token is either operand or supported operator
        if ele not in OPS and not is_operand(ele):
            raise ValueError(f"Invalid element: {ele}")

        node = Node(ele)

        # If operand, push directly onto stack
        if is_operand(ele):
            stackObj.data.append(node)

        # If operator, pop two operands and apply operation
        else:
            ptr2 = stackObj.data.pop()  # second operand
            ptr1 = stackObj.data.pop()  # first operand

            node.left = ptr1
            node.right = ptr2

            # Perform operation based on operator type
            if op_code(ele) == "a":
                stackObj.data.append(Node(int(ptr1.value) + int(ptr2.value)))

            elif op_code(ele) == "s":
                stackObj.data.append(Node(int(ptr1.value) - int(ptr2.value)))

            elif op_code(ele) == "m":
                stackObj.data.append(Node(int(ptr1.value) * int(ptr2.value)))

            else:
                # Division operation with zero check
                if int(ptr2.value) == 0:
                    raise ZeroDivisionError
                stackObj.data.append(Node(int(ptr1.value) / int(ptr2.value)))

    # After processing entire expression,
    # exactly one result should remain in stack.
    return stackObj.data[0].value


# Evaluate and print result
print(evaluate_postfix_expression(expression, stackObj))