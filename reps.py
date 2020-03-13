f = open("C:\\Users\\rskov\\Projects\\whodatrep\\reps.csv")

out = open("repsout.txt", "w")

reps = f.readlines()

for x in range(0,len(reps)):
    spaceIndex = reps[x].find(" ")
    if reps[x].find(",") < 5:
        reps[x] ="0"+reps[x]
    newzip = "\""+reps[x][:5]+"\""+":"+"\""+reps[x][6:spaceIndex]+"\","
    out.write(newzip)




f.close()

out.close()
