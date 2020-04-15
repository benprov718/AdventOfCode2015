import re
import pprint

pp = pprint.PrettyPrinter(width=1)
wires = {}
incomplete= []
incomproc=False
incomiter = 0

def connect(signal, wire):
    global wires
    if re.match(r'[0-9]+', str(signal)):
        wires[wire]=int(signal)
        # print("Connecting wire {0} with signal {1}".format(signal,wire))
        # print(wires)
    else:
        store(signal + " -> " + wire)

def isWired(connected):
    if connected in wires:
        return True

def store(commanded):
    incomplete.append(commanded)
    print("Storing {0}".format(commanded))
    pass

def process(commanded):
    global wires
    if len(commanded) > 3 and not incomproc:
        action=re.search(r'([A-Z]+)', line).group(0)
        # print("Command from \'{0}\' is {1}".format(line, action))
    elif not incomproc:
        action="ASSIGN"
    elif incomproc and commanded[0] == "NOT":
        action="NOT"
    else:
        action=commanded[1]
    if action == "ASSIGN":
        # print("Do an assign!")
        connect(commanded[0], commanded[2])
    elif action == "NOT":
        # print("Do a bitwise of {0} into {1}".format(commanded[1], commanded[3]))
        if commanded[1] in wires.keys():
            nei = ~int(wires[commanded[1]]) + 0x10000
            connect(nei, commanded[3])
        else:
            store(commanded)
    elif commanded[0] in wires.keys():
        if action == "LSHIFT":
            # print("Do an LSHIFT !")
            connect((wires[commanded[0]] << int(commanded[2])), commanded[4])
        elif action == "RSHIFT":
            # print("Do an RSHIFT !")
            connect((wires[commanded[0]] >> int(commanded[2])), commanded[4])
        elif commanded[2] in wires.keys():
            if action == "AND":
                # print("Do an AND!")
                connect((wires[commanded[0]] & wires[commanded[2]]), commanded[4])
            elif action == "OR":
                # print("Do an OR !")
                connect((wires[commanded[0]] | wires[commanded[2]]), commanded[4])
    else:
        store(commanded)
        # print("PANIC! Cannot comprehend: {0}".format(action))


def operate(commanded):
    pass


for line in open('taskfiles/task7-2.txt'):
    commanded=line.split()
#    if len(commanded) > 3:
#        action=re.search(r'([A-Z]+)', line).group(0)
#        # print("Command from \'{0}\' is {1}".format(line, action))
#    else:
#        action="ASSIGN"
#        # print("Command from \'{0}\' is {1}".format(line, commanded[1]))
    process(commanded)

incomproc=True
pp.pprint(wires)
if len(incomplete) > 0:
    print("We have unfinished business!")
    print(incomplete)
    while incomiter < 4:
        for queue in incomplete:
            process(queue)
            print("Processing queued: {0}. Len {1}".format(queue, len(queue)))
            incomiter+=1


print("End")
# print(wires)
# print("End")
# print(wires['h'])
