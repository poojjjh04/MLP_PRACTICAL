students = ("Arun", "Priya", "Rahul", "Sneha", "Karthik", "Divya")
print("Students who completed training:")
for s in students:
    print(s)
name = input("Enter student name to search: ")
if name in students:
    print(name, "is present in the tuple.")
    print("Position:", students.index(name))
else:
    print(name, "is not present in the tuple.")
print("Total number of students:", len(students))
