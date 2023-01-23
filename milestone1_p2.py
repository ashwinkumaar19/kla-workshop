o = open("output.txt","w")
with open("D:\KLA\Milestone_Input\Milestone_Input\Milestone 1\Format_Source.txt","r") as f:
    lines = f.readlines()
print(lines)
c = 0
for i in lines:
    if i == "boundary\n":
        c += 1
    if i == "boundary\n" and c > 2:
        break
    o.write(i)
print(c)
o.close()
a = open("output.txt","r")
print(a.read())
