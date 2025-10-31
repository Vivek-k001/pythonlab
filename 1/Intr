def simple_interest(p, t, is_senior):
    if is_senior.lower() == "yes":
        rate = 12
    else:
        rate = 10
    si = (p * t * rate) / 100
    return si

# Main program
p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
is_senior = input("Is the customer a senior citizen? (yes/no): ")

interest = simple_interest(p, t, is_senior)
print("Simple Interest =", interest)
