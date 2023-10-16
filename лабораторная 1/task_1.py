lst = list(map(float, input().split()))
lst.append(sum(lst) / (len(lst) + 1))
print(lst)
