from typing import List, Tuple

task_file=open('taskfiles/task2.txt', 'r')
packages: List[Tuple[int, int, int]] = [ ]
total_wrap=0
total_ribbon=0

for line in task_file:
    pkg = line.rstrip()
    #    print(pkg.split('x'))
    packages.append(pkg.split('x'))


def package_wrap(l=0, w=0, h=0):
    l=int(l)
    w=int(w)
    h=int(h)
    area = (2*l*w + 2*w*h + 2*h*l)
#    print("Area of the thing is {0}".format(area))
    sides = []
    sides.append(int(l*w))
    sides.append(int(l*h))
    sides.append(int(w*h))
#    print("Smallest side is {0}".format(min(sides)))
#    print("Total sqft needed for package is: {0}".format(area+min(sides)))
    return(area+min(sides))



def package_ribbon(l=0, w=0, h=0):
    l=int(l)
    w=int(w)
    h=int(h)
    sides = []
    sides.append(int(l))
    sides.append(int(h))
    sides.append(int(w))
#    biggest=max(sides)
    sides.remove(max(sides))
    return( 2*sides[0] + 2*sides[1] + l*w*h )
#    print("Popping {0} from line and now left with {1}".format(biggest,sides))
#    length=( 2*sides[0] + 2*sides[1] + l*w*h )
#    print("Ribbonlength is {0}".format(length))
#    return(length)



for dims in packages:
    total_wrap+=package_wrap(*dims)
    total_ribbon+=package_ribbon(*dims)
print("Wrapping paper needed is: {0}, and ribbon needed is: {1}".format(total_wrap, total_ribbon))