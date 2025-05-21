lines = "---#--###----\n-#---#----##-\n####-#-#-#-##\n---#---#-#---\n-#-####---##-\n-#------#----\n-############\n------------@"
splitLines = lines.split("\n")
for i in range(len(splitLines)):
    splitLines[i] = list(splitLines[i])

for x in range(len(splitLines)):
    for y in range(len(splitLines[x])):
        if splitLines[x][y] == "-":
            splitLines[x][y] = "+"
            if x == len(splitLines):
                continue
            break

for i in range(len(splitLines)):
    splitLines[i] = ''.join(splitLines[i])

splitLines = '\n'.join(splitLines)
print(splitLines)




