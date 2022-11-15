from time import sleep

print("When you are done listing names or items, dont forget to type 'done' in order to move forward with the app.\n")
sleep(2)
t = False #placed this here to allow initiation of while loop
counts = dict()
names = []
while t == False :
    counts = dict()
    Counts = input("Enter names or items to count: ")
    names.append(Counts)
    if Counts == "done": break #this breaks us out of while loop from input queries

#This section will do the counting of our names or items that show up in our newly made dictionary called names


for name in names:

    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

counts.pop("done")
print(counts)

