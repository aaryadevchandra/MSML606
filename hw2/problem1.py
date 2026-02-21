expression = ["3", "4", "+", "2", "*"]

def is_operand(ele):
    if 48 <= ord(ele) <= 57:
        return True
    return False


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Stack:
    def __init__(self):
        self.stack = []

    def display(self):
        print([node.value for node in self.stack])


stackObj = Stack()

OPS = {"+", "-", "*", "/"}


def _reset_tree_stack():
    stackObj.stack = []


def _is_valid_operand_token(tok: str) -> bool:
    return isinstance(tok, str) and len(tok) == 1 and is_operand(tok)


def _is_valid_operator_token(tok: str) -> bool:
    return isinstance(tok, str) and tok in OPS


def _validate_postfix_for_tree(expression):
    if expression is None:
        raise ValueError("Expression is None")
    if not isinstance(expression, list):
        raise TypeError("Expression must be a list of strings")
    if len(expression) == 0:
        raise ValueError("Empty postfix expression")

    for tok in expression:
        if not isinstance(tok, str):
            raise ValueError("Invalid token type")
        if _is_valid_operand_token(tok):
            continue
        if _is_valid_operator_token(tok):
            continue
        raise ValueError(f"Invalid token: {tok}")

    depth = 0
    for tok in expression:
        if _is_valid_operand_token(tok):
            depth += 1
        else:
            if depth < 2:
                raise ValueError("Malformed postfix: insufficient operands")
            depth -= 1

    if depth != 1:
        raise ValueError("Malformed postfix: too many operands")


def safe_create_binary_tree_from_postfix_expression(expression):
    _validate_postfix_for_tree(expression)
    _reset_tree_stack()
    root = create_binary_tree_from_postfix_expression(expression)
    if len(stackObj.stack) != 1:
        raise ValueError("Malformed postfix: stack did not end with one root")
    return stackObj.stack[0]


def create_binary_tree_from_postfix_expression(expression):

    for ele in expression:
        node = Node(ele)
        if is_operand(ele):
            stackObj.stack.append(node)
            # stackObj.display()
        else:
            ptr2 = stackObj.stack.pop()
            ptr1 = stackObj.stack.pop()
            node.left = ptr1
            node.right = ptr2

            stackObj.stack.append(node)
            # stackObj.display()

    return node


root = safe_create_binary_tree_from_postfix_expression(expression)



