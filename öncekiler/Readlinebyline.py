f = open('inputFile.txt', 'r')
count = 0
for line in f:
    ##print(line+'rrrrttt')
    print(str(count)+line)
    count = count+1
f.close()

for line in f:
    print(line)
f.close()
