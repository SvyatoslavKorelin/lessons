a = input().split(", ")
n = ["5","4","3"]
usp = 0
for elem in n:
    usp += a.count(elem)
print(usp / len(a) * 100)