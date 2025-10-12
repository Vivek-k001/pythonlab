nums = input("Enter integers separated by spaces: ").split()
result = []

for n in nums:
    value = int(n)
    if value > 100:
        result.append("over")
    else:
        result.append(value)

print("Modified List:", result)
