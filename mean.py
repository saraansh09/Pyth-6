import csv


with open( "S.csv" , newline = "") as f:
    reader = csv.reader(f)
    a = list(reader)
    a.pop(0)
    ab = []
    for i in range(len(a)):
        abcd = a[i][1]
        ab.append(float(abcd))
    hello = len(ab)
    world = 0
    for e in ab:
        world += e
    mean = world/hello
    print("The mean is: " + str(mean))
    
    
    