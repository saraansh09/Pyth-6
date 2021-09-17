import csv

with open( "S.csv" , newline = "") as f:
    reader = csv.reader(f)
    a = list(reader)
    a.pop(0)
    ab = []
    for i in range(len(a)):
        abcd = a[i][3]
        ab.append(float(abcd))
    hello = len(ab)
    ab.sort()
    if hello % 2 == 0 :
        avog = float(ab[hello // 2])
        agog = float(ab[hello // 2-1])
        median = (avog+agog)/2
    else:
        median = ab[hello // 2]
        
    print("THE MEDIAN IS:" + str(median))