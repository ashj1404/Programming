roof_height = 5

body_height = 3
body_width = 9

for i in range(roof_height):
    for j in range(roof_height - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print("*", end="")
    print()


for k in range(body_height):
    for l in range(body_width):
        print('*', end='')
    print()