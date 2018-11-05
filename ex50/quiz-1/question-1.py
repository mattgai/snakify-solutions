print("Input your name first! Then say either sq for a square pool or nothing for a cylindrical pool. If you said square, input length, width, and height. If you said nothing, input radius and height." )
name = str(input())
sq = str(input())
if sq == "sq":
    l = int(input())
    w = int(input())
    h = int(input())
    sqvolume = str((l*w*h)*7.5)
    print("Hi " + name + ", Your square pool is going to be able to fill up " + sqvolume + " gallons.")
else:
    r = int(input())
    h = int(input())
    sqcylinder = str(((r**2)*(3.14)*h)*5.875)
    print("Hi " + name + ", Your cylindrical pool is going to be able to fill up " + sqcylinder + " gallons.")
