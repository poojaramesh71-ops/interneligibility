def check_intern_eligibility(age, percentage):
    if age >= 18 and percentage >= 60:
        print("Eligible: Age is 18 or above and percentage is 60 or above")
        return "Eligible"
    else:
        print("Not Eligible: Age is below 18 or percentage is below 60")
        return "Not Eligible"


age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))

result = check_intern_eligibility(age, percentage)
print("Eligibility Status:", result)