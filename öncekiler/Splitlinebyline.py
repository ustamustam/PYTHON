f = open('inputFile.txt', 'r')
Passfile = open('passfile.txt', 'w')
Failfile = open ('failfile.txt', 'w')
for line in f:
 line_split = line.split()
 if line_split[2] == 'F':
     Passfile.write(line)
 else:
     Failfile.write(line)
f.close()
Passfile.close()
Failfile.close()

