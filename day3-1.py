task_file = open('taskfiles/task3.txt', 'r')
santa_pos=[0,0]
rsanta_pos=[0,0]
hice_list = []


def deliver(position):
    if not (position in hice_list):
        hice_list.append(position)

def move(start, movement):
    x = start[0]
    y = start[1]
    if movement == "^":
        x += 1
    elif movement == ">":
        y += 1
    elif movement == "v":
        x -= 1
    else:
        y -= 1
    return([x,y])

# initial delivery
deliver(santa_pos)

for line in task_file:
    for count, direction in enumerate(line, 0):
        # print(count)
        if (count %2 == 0):
            santa_pos=move(santa_pos, direction)
            deliver(santa_pos)
        else:
            rsanta_pos=move(rsanta_pos, direction)
            deliver(rsanta_pos)

print("Santa has been to {0} unique locations".format(len(hice_list)))
