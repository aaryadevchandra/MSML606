expression = ["3", "4", "+", "2", "*"]


OPS = {"+", "-", "*", "/"}

def is_operator(tok: str) -> bool:
    return tok in OPS

def is_number_token(tok: str) -> bool:
    if tok.startswith("-") and tok[1:].isdigit():
        return True
    return tok.isdigit()

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


def create_binary_tree_from_postfix_expression(expression):

    for ele in expression:
        node = Node(ele)
        if is_number_token(ele):
            stackObj.stack.append(node)
            # stackObj.display()
        elif is_operator(ele):
            ptr2 = stackObj.stack.pop()
            ptr1 = stackObj.stack.pop()
            node.left = ptr1
            node.right = ptr2

            stackObj.stack.append(node)
            # stackObj.display()
        else:
            raise ValueError(f"Invalid token: {ele}")
        
    if len(stackObj.stack) != 1:
        raise ValueError("Malformed postfix: too many operands")

    return node


root = create_binary_tree_from_postfix_expression(expression=expression)


def display_stack(stack):
    print([node.value for node in stack])


def preorder_traversal(node, out):

    if node != None:
        out.append(node.value)
        preorder_traversal(node.left, out)
        if node.right != None:
            preorder_traversal(node.right, out)


def inorder_traversal(node, out):
    if node != None:
        inorder_traversal(node.left, out)
        out.append(node.value)
        inorder_traversal(node.right, out)
        

def postorder_traversal(node, out):
    if node != None:
        postorder_traversal(node.left, out)
        postorder_traversal(node.right, out)
        out.append(node.value)
        

preorder_traversal_output = []
inorder_traversal_output = []
postorder_traversal_output = []

preorder_traversal(root, preorder_traversal_output)
inorder_traversal(root, inorder_traversal_output)
postorder_traversal(root, postorder_traversal_output)

print(preorder_traversal_output)
print(inorder_traversal_output)
print(postorder_traversal_output)