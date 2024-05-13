from sys import stdin

left_stack = list(stdin.readline().strip())
right_stack = []

M = int(stdin.readline().strip())

for _ in range(M):
    command = stdin.readline().split()

    if command[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif command[0] == 'B' and left_stack:
        left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

print(''.join(left_stack + right_stack[::-1]))