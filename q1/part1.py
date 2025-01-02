one = []
two = []

with open("q1/input", "r") as f:
    lines = f.readlines()

    for line in lines:
        a, b = line.split("   ")
        one.append(int(a))
        two.append(int(b))

res = 0
one.sort()
two.sort()

for i in range(len(one)):
    res += abs(one[i] - two[i])

# nlogn mlogm O(m + m)

print(res)
