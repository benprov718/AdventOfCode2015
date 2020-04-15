import pprint
pp = pprint.PrettyPrinter(width=1)

signals = dict()

with open("taskfiles/task7-2.txt") as f:
    instructions = f.readlines()


for i in instructions:
    tmp = i.split("->")

    val = tmp[0]
    val = val.split()
    var = tmp[1].strip()

    #signal
    if len(val)  == 1 and val[0].isdigit():
        val = int(val[0])
        signals[var] = val

    elif len(val) == 1 and not val[0].isdigit():
        signals[var] = ("SUBST", val[0])

    elif "AND" in val or "OR" in val or "LSHIFT" in val or "RSHIFT" in val:
        (a, op, b) = val[0],val[1], val[2]
        signals[var] = (op, a, b)

    #NOT
    elif "NOT" in val:
        (op, a) = val[0], val[1]
        signals[var] = (op, a)

#substitute
while True:

    for key in signals.keys():

        val = signals[key]

        if str(val).isdigit():
            continue

        op = val[0]

        if op == "NOT":
            (_, var) = val
            tmp = signals[var]
            if str(tmp).isdigit():
                signals[key] = ~tmp & 0x10000

pp.pprint(signals)

