import matplotlib.pyplot as plt


o = open("output2.txt","w")


with open("Milestone_Input\Milestone_Input\Milestone 2\Source.txt","r") as f:
    lines = f.readlines()

for i in lines:
    if i == "boundary\n":
        break
    else:
        o.write(i)
o.close()

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

def ismatch(source,target):
    
    #target
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
    '''
    plt.figure()
    plt.plot(x,y)
    plt.show()
    '''
    x = list(x)
    y = list(y)
    x.pop()
    y.pop()
    a = find_area(x,y)

    #source
    new2 = []
    i = 1
    while(i < len(source)):
        temp = []
        if i+1 < len(source):
            temp.append(source[i])
            temp.append(source[i+1])
            new2.append(temp)
            i += 2
    x , y = zip(*new2)
    x = list(x)
    y = list(y)

    x.pop()
    y.pop()
    a2 = find_area(x,y)
    
    if a == a2:
        return 1
    else:
        return 0


def find_area(x,y):
    area = 0.0

    j = len(x) - 1
    n = len(x)
    for i in range(0,n):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return int(abs(area/2.0))
            
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
        if ismatch(temp,target_points[0]):
            print("YES")

a = ismatch(points[0],target_points[0])            
print(a)


        

