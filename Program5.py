employee = {
    "Employee ID": 101,
    "Name": "Rahul",
    "Department": "Marketing",
    "Designation": "Sales Executive",
    "Salary": 45000
}
print("Employee Details:")
print(employee)
print("Employee Name:", employee["Name"])
print("Salary:", employee["Salary"])
print("\nEmployee Information:")
for key, value in employee.items():
    print(key, ":", value)
