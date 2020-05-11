numbers = []
count = 15
for i in range(50):
  if i % 2 == 0 and i % 6 != 0 and count > 0:
    numbers.append(i)
    count -= 1
print(numbers)