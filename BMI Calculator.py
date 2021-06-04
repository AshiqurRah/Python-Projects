print("///Welcome to BMI calculator///")
height = float(input("What is your height in m?\n"))
weight = float(input("What is your weight in kg?\n"))
bmi_cal = weight / height ** 2
bmi = round(bmi_cal,2)

if bmi < 18.5 :
    print(f"Your bmi score is {bmi}, you are underweight, you should gain some weight.")
elif bmi < 25 :
    print(f"Your bmi score is {bmi}, you're in normal position.")
elif bmi < 30 :
    print(f"Your bmi score is {bmi}, you're overweight, try to loose some fat.")
elif bmi < 35 :
    print(f"Your bmi score is {bmi}, you're obese, start ecercise to become a fit person.")
else:
    print(f"your bmi score is {bmi}, you're extremely obese. You need to meet with a doctor.")










