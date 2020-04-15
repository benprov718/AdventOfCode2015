import re
# import pprint

wires = {}
incomplete= []
incomproc=False
incomiter = 0

def connect(signal, wire):
    global wires
    wires[wire]=int(signal)


def store(commanded):
    if not incomproc:
        str1= " "
        incomplete.append(str1.join(commanded))

def process(commanded):
    global wires
    # if incomproc:
        # print("Checking if {0} is wired up, wanting to run {1}".format(commanded[1], commanded))
        # print(wires[commanded[1]])
    if commanded[1] in wires.keys():
        if re.match(r'[A-Z]', line):
            # print("Line starts with uppercaseletter, thingdo")
            # print("Trying bitwise complement of {0} into {1}".format(commanded[1], commanded[3]))
            nei = ~int(wires[commanded[1]]) + 0x10000
            # print("Bitwise of {0}({1}) is {2}l".format(commanded[1], wires[commanded[1]], int(nei)))
            # print(nei)
            connect(nei, commanded[3])
    elif re.match(r'[a-z]', line):
        # print("Line starts with lowercaseletter, thingdo")
        if len(commanded) == 3 and wires[str(commanded[0])] not in wires:
            store(commanded)
        else:
            operate(commanded)
    else:
        store(commanded)


def operate(commanded):
    op1=commanded[0]
    op2=commanded[2]
    op=commanded[1]
    target=commanded[4]
    # if incomproc:
    #     print("processing target {0}".format(target))
    # source="VOID"
    # print("Doing operation \"{0}\" on \'{1}\' and \'{2}\' into {3}".format(op, op1,op2,target))
    if op1 in wires.keys():
        if op == "LSHIFT":
            connect((wires[op1] << int(op2)), target)
        elif op == "RSHIFT":
            connect((wires[op1] >> int(op2)), target)
        elif op2 in wires.keys():
            if op == "AND":
                connect((wires[op1] & wires[op2]), target)
            elif op == "OR":
                connect((wires[op1] | wires[op2]), target)
    else:
        # print("PANIC! At the bitwise operator {0}".format(op))
        store(commanded)
    # if source != "VOID":
    #     connect(source, target)


for line in open('taskfiles/task7-2.txt'):
    commanded=line.split()
    if re.match(r'^\d', line):
        # print("Line starts with number, connect signal")
        connect(commanded[0], commanded[2])
    else:
        process(commanded)

# print("There are {0} incomplete instructions.".format(len(incomplete)))
incomproc=True
while len(incomplete) > 0 and incomiter < 3:
    for queue in incomplete:
        # print("Attempting to wire: {0}".format(queue))
        # queue1=queue.split()
        line=queue
        process(queue.split())
        # print(wires)
        if queue.split()[-1] in wires.keys():
            # print("{0} is in wires, removing {1}".format(queue.split()[-1], queue))
            incomplete.remove(queue)
        incomiter+=1

print(wires)
# pp = pprint.PrettyPrinter(width=1)
# pp.pprint(wires)
print(incomplete)
print(wires['h'])
