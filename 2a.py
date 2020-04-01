def package(l=0, w=0, h=0):
    area = (2*l*w + 2*w*h + 2*h*l)
#    print("Area of the thing is {0}".format(area))
    sides = []
    sides.append(int(l*w))
    sides.append(int(l*h))
    sides.append(int(w*h))
#    print("Smallest side is {0}".format(min(sides)))
#    print("Total sqft needed for package is: {0}".format(area+min(sides)))
    return(area+min(sides))

total=0
packages = [(1,1,10), (2,3,4)]
for dims in packages:
    total+=package(*dims)
print(total)