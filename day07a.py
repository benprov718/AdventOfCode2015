import re
# import pprint

wires = {}


def connect(signal, wire):
    global wires
    wires[wire]=int(signal)
    pass


def operate(commanded):
    op1=commanded[0]
    op2=commanded[2]
    op=commanded[1]
    target=commanded[4]
    # source="VOID"
    # print("Doing operation \"{0}\" on \'{1}\' and \'{2}\' into {3}".format(op, op1,op2,target))
    if op == "AND":
        connect((wires[op1] & wires[op2]), target)
    elif op == "OR":
        connect((wires[op1] | wires[op2]), target)
    elif op == "LSHIFT":
        connect((wires[op1] << int(op2)), target)
    elif op == "RSHIFT":
        connect((wires[op1] >> int(op2)), target)
    else:
        print("PANIC! At the bitwise operator {0}".format(op))
    # if source != "VOID":
    #     connect(source, target)


for line in open('taskfiles/task7.txt'):
    commanded=line.split()
    if re.match(r'^\d', line):
        # print("Line starts with number, connect signal")
        connect(commanded[0], commanded[2])
    elif re.match(r'[a-z]', line):
        # print("Line starts with lowercaseletter, thingdo")
        operate(commanded)
    elif re.match(r'[A-Z]', line):
        # print("Line starts with uppercaseletter, thingdo")
        print("Trying bitwise complement of {0} into {1}".format(commanded[1], commanded[3]))
        connect(wires[commanded[1]],commanded[3])
    else:
        pass

# print(wires)
# pp = pprint.PrettyPrinter(width=1)
# pp.pprint(wires)
print(wires['a'])