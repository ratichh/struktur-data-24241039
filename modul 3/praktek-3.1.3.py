def buat_node(data):
    return {'data': data, 'next': None}

def push(head, data):
    new_node = buat_node(data)
    new_node['next'] = head
    return new_node

def pop(head):
    if head is None:
        print("Stack kosong.")
        return None, None
    popped = head['data']
    head = head['next']
    return head, popped

def peek(head):
    if head is None:
        return None
    return head['data']

def is_empty(head):
    return head is None

# Uji coba
stack = None  # Stack awal kosong

stack = push(stack, 10)
stack = push(stack, 20)
stack = push(stack, 30)

print("Top stack:", peek(stack))  # Harusnya 30

stack, val = pop(stack)
print("Pop:", val)               # Harusnya 30

stack, val = pop(stack)
print("Pop:", val)               # Harusnya 20

print("Top stack sekarang:", peek(stack))  # Harusnya 10