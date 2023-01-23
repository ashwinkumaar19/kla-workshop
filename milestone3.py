import math


o = open("output3.txt","w")


with open("Milestone_Input\Milestone_Input\Milestone 3\Source.txt","r") as f:
    lines = f.readlines()

for i in lines:
    if i == "boundary\n":
        break
    else:
        o.write(i)
o.close()

target_points = []
n = 0
with open("Milestone_Input\Milestone_Input\Milestone 3\POI.txt","r") as d:
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

def find_distance(points):

    temp = []
    for i in range(len(points)):
        if i+1 < len(points):
            temp.append(math.dist(points[i],points[i+1]))
    return temp


def dist_match(source,target):
    t = []
    i = 1
    while(i < len(target)):
        temp = []
        if i+1 < len(target):
            temp.append(target[i])
            temp.append(target[i+1])
            t.append(temp)
            i += 2
    #print(t)    

    s = []
    i = 1
    while(i < len(source)):
        temp = []
        if i+1 < len(source):
            temp.append(source[i])
            temp.append(source[i+1])
            s.append(temp)
            i += 2
    #print(s)   
    
    a = find_distance(t)
    b = find_distance(s)

    #print(a,b)
    if sum(a) == sum(b):
        return 1
    else:
        return 0


o = open("output3.txt","a")
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
            #print(temp)
            #print(target_points[0])
        if dist_match(temp,target_points[0]):
            o.write("boundary\n")
            o.write("layer 1\n")
            o.write("datatype 0\n")
            o.write(i)
            #o.write("\n")
            o.write("endel\n")

o.write("endstr\n")
o.write("endlib\n")
      



        

