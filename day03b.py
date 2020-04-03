task_file = open('taskfiles/task3.txt', 'r')
# task_file = "^v"
santa_pos=[0,0]
robosanta_pos=[0,0]
hice_list = []


def deliver(position):
    # print(position)
    stringPos = str(position[0]) + "x" + str(position[1]) + "y"
    # print(stringPos)
    if not (stringPos in hice_list):
        print("Santa has not been to {0} before".format(position))
        hice_list.append(stringPos)
    # print("Santa is delivering present at position {0}".format(position))
    # print(hice_list)


# initial delivery
deliver(santa_pos)

for task_line in task_file:
    for count, direction in enumerate(task_line, 0):
        print(count, direction)
        if (count % 2) == 0:
            if direction == "^":
               santa_pos[1]+=1
            elif direction == ">":
               santa_pos[0]+=1
            elif direction == "v":
               santa_pos[1]-=1
            else:
               santa_pos[0]-=1
            deliver(santa_pos)
        else:
            if direction == "^":
                robosanta_pos[1] += 1
            elif direction == ">":
                robosanta_pos[0] += 1
            elif direction == "v":
                robosanta_pos[1] -= 1
            else:
                robosanta_pos[0] -= 1
            deliver(robosanta_pos)
    print("The santas have been to {0} unique locations".format(len(hice_list)))
