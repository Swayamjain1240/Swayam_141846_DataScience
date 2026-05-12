#Method 1 :
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

#Method 2 :
for i in range(5, 51, 5):
    print(i)

#Method 3 :
i = 5

while i <= 50:
    print(i)
    i += 5