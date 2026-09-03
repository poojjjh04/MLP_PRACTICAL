cgpa_list = []

n = int(input("Enter number of students: "))

for i in range(n):
    cgpa = float(input(f"Enter CGPA of student {i+1}: "))
    cgpa_list.append(cgpa)

print("\nAll student CGPA records:")
print(cgpa_list)

eligible_students = []

for cgpa in cgpa_list:
    if cgpa >= 6.5:
        eligible_students.append(cgpa)

print("\nEligible students for Campus Placement (CGPA >= 6.5):")
print(eligible_students)
