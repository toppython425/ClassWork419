def push(stack, item):
    if item is None:
        print("Попытка добавить None")
        return None
    stack.append(item)


def pop(stack):
    if stack:
        popped_item = stack.pop()
        return popped_item
    else:
        print('Stack is empty')
        return None


def peek(stack):
    top = stack[-1]
    return top


if __name__ == '__main__':
    my_stack_1 = []
    my_stack_2 = []
    push(my_stack_1, 'item_3')
    push(my_stack_1, 'item_2')
    push(my_stack_1, 'item_1')
    print(my_stack_1)

    push(my_stack_2, pop(my_stack_1))
    push(my_stack_2, pop(my_stack_1))
    push(my_stack_2, pop(my_stack_1))
    push(my_stack_2, pop(my_stack_1))
    push(my_stack_2, pop(my_stack_1))
    push(my_stack_2, pop(my_stack_1))
    print(my_stack_2)
