import math


o = open("output7.txt","w")

with open("Milestone_Input\Milestone_Input\Milestone 7\Source.txt","r") as f:
    lines = f.readlines()

for i in lines:
    if i == "boundary\n":
        break
    else:
        o.write(i)
o.close()

target_points = []
n = 0
with open("Milestone_Input\Milestone_Input\Milestone 7\POI.txt","r") as d:
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


def dist_match(s,t):
 
    a = find_distance(t)
    b = find_distance(s)
    
    scale = []
    for i in range(len(a)):
        scale.append(a[i]/b[i])
    


    if len(set(scale)) == 1:
        return 1
    else:
        return 0
    '''
    if sum(a) == sum(b):
        return 1
    else:
        return 0
    '''

def find_area(x,y):
    area = 0.0

    j = len(x) - 1
    n = len(x)
    for i in range(0,n):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return int(abs(area/2.0))

def area_match(s,t):

    a = find_distance(t)
    b = find_distance(s)
    
    scale = []
    for i in range(len(a)):
        scale.append(a[i]/b[i])
    
    k = 0
    if sum(a) > sum(b):
        k = sum(a)/sum(b)
    else:
        k = sum(b)/sum(a)

    if len(set(scale)) == 1:
        x1 = []
        y1 = []
        for i in s:
            x1.append(i[0])
            y1.append(i[1])
        
        x2 = []
        y2 = []
        for i in t:
            x2.append(i[0])
            y2.append(i[1])
        
        a1 = find_area(x1,y1)
        b1 = find_area(x2,y2)

        if b1 == k*k*a1:
            return 1
        else:
            return 0
    else:
        return 0

def is_match(source,target):
    t = []
    i = 1
    while(i < len(target)):
        temp = []
        if i+1 < len(target):
            temp.append(target[i])
            temp.append(target[i+1])
            t.append(temp)
            i += 2

    s = []
    i = 1
    while(i < len(source)):
        temp = []
        if i+1 < len(source):
            temp.append(source[i])
            temp.append(source[i+1])
            s.append(temp)
            i += 2
    
    if area_match(s,t):
        return 1
    else:
        return 0

    

o = open("output7.txt","a")
points = []
for i in lines:
    if "xy" in i:
        temp = []
        l = i.split()
        temp.append(int(l[1]))
        for j in range(2,len(l)):
            temp.append(int(l[j]))
            points.append(temp)
        if is_match(temp,target_points[0]) or is_match(temp,target_points[1]):
            o.write("boundary\n")
            o.write("layer 1\n")
            o.write("datatype 0\n")
            o.write(i)
            o.write("endel\n")

o.write("endstr\n")
o.write("endlib\n")




        

