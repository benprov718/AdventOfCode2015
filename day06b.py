task_file = open('taskfiles/task6.txt', 'r')
# task_line="turn on 0,0 through 9,9"

light_dict = {}


def lights(cmd, coords):
    # print("lights({0},{1})".format(cmd, coords))
    # print(coords[0])
    startX = int(coords[0].split(',')[0])
    startY = int(coords[0].split(',')[1])
    stopX = int(coords[1].split(',')[0])
    stopY = int(coords[1].split(',')[1])
    # print("I want to do {0} with lights starting at {1},{2} ending at {3},{4}".format(cmd,startX, startY, stopX, stopY))
    for xax in range(startX, stopX + 1):
        for yax in range(startY, stopY + 1):
            light = str(xax) + "x" + str(yax)
            strength = light_dict.get(light, "FILL-ME")
            if cmd == 'on':
                if strength == "FILL-ME":
                    light_dict[light] = 1
                else:
                    light_dict[light] = strength + 1
            elif cmd == 'off':
                if (strength == "FILL-ME") or (strength == 0):
                    pass
                else:
                    light_dict[light] = strength - 1
            elif cmd == 'flip':
                if strength == "FILL-ME":
                    light_dict[light] = 2
                else:
                    light_dict[light] = strength + 2
            else:
                print("You musta taken a wrong turn at Albuquerque")
    pass


for command in task_file:
    coordStart = command.split()[-3]
    coordStop = command.split()[-1]
    coords = [coordStart, coordStop]
    if command.startswith('turn on'):
        cmd = "on"
        lights(cmd, coords)
    elif command.startswith('toggle'):
        cmd = "flip"
        lights(cmd, coords)
    elif command.startswith('turn off'):
        cmd = "off"
        lights(cmd, coords)
    else:
        print("Panic! At the christmas lights!: {0}".format(command))
# print("{0} lights are on:".format(len(light_dict)))
print("Total light strength in grid: {0}".format(sum(light_dict.values())))
# print(light_set)
