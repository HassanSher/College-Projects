# Home Work 1 (Hassan Sher)

# Question 1:

#Personal Information

student_name = "Hassan Sher"
student_address = "123 Parkway \nPiscataway, NJ, 08854"
student_number = "(123)456-7890"
student_major = "Computer Science"

print("Student Information:")
print(student_name)
print(student_address)
print(student_number)
print(student_major)
print("------------------")
print("------------------")

# Question 2:

# Sales Prediction

profit_percentage = 0.23
total_sales = float(input("Enter Total Sales "))
profit = round(total_sales * profit_percentage)
# I used round for accuracy but float can be turned into int to remove the decimals.
print("Profit is: ")
print(profit)