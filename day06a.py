task_file=open('taskfiles/task6.txt', 'r')
# task_line="turn on 0,0 through 9,9"

light_set=set()


def lights(cmd, coords):
    # print("lights({0},{1})".format(cmd, coords))
    # print(coords[0])
    startX=int(coords[0].split(',')[0])
    startY=int(coords[0].split(',')[1])
    stopX=int(coords[1].split(',')[0])
    stopY=int(coords[1].split(',')[1])
    # print("I want to do {0} with lights starting at {1},{2} ending at {3},{4}".format(cmd,startX, startY, stopX, stopY))
    for xax in range(startX, stopX+1):
        for yax in range(startY, stopY+1):
            light=str(xax)+"x"+str(yax)
            if cmd == 'on':
                light_set.add(light)
            elif cmd == 'off':
                light_set.discard(light)
            elif cmd == 'flip':
                if (light in light_set):
                    light_set.discard(light)
                else:
                    light_set.add(light)
            else:
                print("You musta taken a wrong turn at Albuquerque")
    pass


for command in task_file:
    coordStart=command.split()[-3]
    coordStop=command.split()[-1]
    coords=[coordStart, coordStop]
    if command.startswith('turn on'):
        cmd="on"
        lights(cmd, coords)
    elif command.startswith('toggle'):
        cmd="flip"
        lights(cmd, coords)
    elif command.startswith('turn off'):
        cmd="off"
        lights(cmd, coords)
    else:
        print("Panic! At the christmas lights!: {0}".format(command))
print("{0} lights are on:".format(len(light_set)))
# print(light_set)
