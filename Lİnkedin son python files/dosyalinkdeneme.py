f = open('alınacaksertifikalar.txt', 'r')
lines = f.readlines()
f.close()
lines = filter(lambda x: not x.isspace(), lines)
liste1=[]
liste2=[]
for line in lines:
        line = line.rstrip()
        liste1.append(line)
        print(line)

with open('alınacaksertifikalar2.txt', 'w') as filehandle:
    for listitem in liste1:
        filehandle.write("\n"+listitem)
f2 = open('alınacaksertifikalar2.txt', 'r')
for a in f2:
    if a not in liste2:
        liste2.append(a)
with open('alınacaksertifikalar3.txt', 'w') as filehandle:
    for listitem in liste2:
        filehandle.write(listitem)




# Write
#fh = open("alınacaksertifikalar2.txt", "w")
#fh.write("/n"+liste1)
# should also work instead of joining the list:
# fh.writelines(lines)
#fh.close()

"""
liste1=[]
liste2=[]
for line in f:
   if line!="\n":
        line = line.rstrip()
        liste1.append(line)
        print(line)
f.close()

with open('alınacaksertifikalar2.txt', 'w') as filehandle:
    for listitem in liste1:
        filehandle.write("\n"+listitem)


# Read lines as a list
fh = open("myfile", "r")
lines = fh.readlines()
fh.close()

# Weed out blank lines with filter
lines = filter(lambda x: not x.isspace(), lines)

# Write
fh = open("output", "w")
fh.write("".join(lines))
# should also work instead of joining the list:
# fh.writelines(lines)
fh.close()
"""