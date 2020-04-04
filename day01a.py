task_file= open('taskfiles/task1.txt', 'r')
floor = 0
position = 0
for line in task_file:
    for i, c in enumerate(line, start=1):
        if c == "(":
            floor+=1
        else:
            floor-=1
        if floor == -1:
            print("Santa is at floor {0} at position {1}".format(floor,i))
print("Santa is at floor {0}".format(floor))