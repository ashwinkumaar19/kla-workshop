import matplotlib.pyplot as plt

o = open("output.txt","w")
with open("Milestone_Input\Milestone_Input\Milestone 2\Source.txt","r") as f:
    lines = f.readlines()

target_points = []
n = 0
with open("Milestone_Input\Milestone_Input\Milestone 2\POI.txt","r") as d:
    for i in d:
        if "xy" in i:
            temp = []
            l = i.split()
            temp.append(int(l[1]))
            n = int(l[1])
            for j in range(2,len(l)):
                temp.append(int(l[j])) 
            target_points.append(temp)
#print(target_points)
#print(n)
points = []
for i in lines:
    if "xy" in i:
        temp = []
        l = i.split()
        if int(l[1]) == n:
            temp.append(int(l[1]))
            for j in range(2,len(l)):
                temp.append(int(l[j]))
            points.append(temp)
#print(points)

def ismatch(target):
    print(target)

    new = []
    i = 1
    while(i < len(target)):
        temp = []
        if i+1 < len(target):
            temp.append(target[i])
            temp.append(target[i+1])
            new.append(temp)
            i += 2
    x , y = zip(*new)
    plt.figure()
    plt.plot(x,y)
    plt.show()

#for i in points:
#    for j in target_points:
ismatch(target_points[0])