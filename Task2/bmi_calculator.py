print("=== BMI Calculator ===")

# -------- Height Input --------
while True:
    try:
        height = float(input("Enter your height in meters (e.g. 1.75): "))
        if height > 0:
            break
        else:
            print("❌ Height must be greater than 0.")
    except ValueError:
        print("❌ Please enter a valid number.")

# -------- Weight Input --------
while True:
    try:
        weight = float(input("Enter your weight in kg (e.g. 70): "))
        if weight > 0:
            break
        else:
            print("❌ Weight must be greater than 0.")
    except ValueError:
        print("❌ Please enter a valid number.")

# -------- BMI Calculation --------
bmi = weight / (height ** 2)

# -------- Result --------
print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
