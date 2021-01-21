## suppose i have to print a combo
combo = (3, 6, 1)

def genrate_combo():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield (i, j, k)

for (i,j,k) in genrate_combo():
    print(i, j, k)
    if (i, j, k) == combo:
        print("found")
        break