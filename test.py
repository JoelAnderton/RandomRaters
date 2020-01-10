import random
org_list = [x + 1 for x in range(100)]
print(org_list)
random.seed(123)
random.shuffle(org_list)

print(org_list)

rater1 = []
rater2 = []
rater3 = []
rater4 = []
for i in org_list[:25]:
    rater1.append(org_list.pop())

for i in org_list[:25]:
    rater2.append(org_list.pop())

for i in org_list[:25]:
    rater3.append(org_list.pop())

rater4 = org_list

print()
print(rater1, len(rater1))
print(rater2, len(rater2))
print(rater3, len(rater3))
print(rater4, len(rater4))

reliability1 = rater1[:5]
reliability2 = rater2[:5]
reliability3 = rater3[:5]
reliability4 = rater4[:5]

print()
print(reliability1, len(reliability1))
print(reliability2, len(reliability2))
print(reliability3, len(reliability3))
print(reliability4, len(reliability4))

while len(reliability1) > 0:
    if len(reliability1) <= 0:
        continue
    rater4.append(reliability1.pop())
    if len(reliability1) <= 0:
        continue
    rater3.append(reliability1.pop())
    if len(reliability1) <= 0:
        continue
    rater2.append(reliability1.pop())
    if len(reliability1) <= 0:
        continue

while len(reliability2) > 0:
    if len(reliability2) <= 0:
        continue
    rater1.append(reliability2.pop())
    if len(reliability2) <= 0:
        continue
    rater4.append(reliability2.pop())
    if len(reliability2) <= 0:
        continue
    rater3.append(reliability2.pop())
    if len(reliability2) <= 0:
        continue

while len(reliability3) > 0:
    if len(reliability3) <= 0:
        continue
    rater1.append(reliability3.pop())
    if len(reliability3) <= 0:
        continue
    rater2.append(reliability3.pop())
    if len(reliability3) <= 0:
        continue
    rater4.append(reliability3.pop())
    if len(reliability3) <= 0:
        continue

while len(reliability4) > 0:
    if len(reliability4) <= 0:
        continue
    rater2.append(reliability4.pop())
    if len(reliability4) <= 0:
        continue
    rater3.append(reliability4.pop())
    if len(reliability4) <= 0:
        continue
    rater1.append(reliability4.pop())
    if len(reliability4) <= 0:
        continue


print()
print(sorted(rater1), len(rater1))
print(sorted(rater2), len(rater2))
print(sorted(rater3), len(rater3))
print(sorted(rater4), len(rater4))
