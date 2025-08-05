# Dictionary example
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

# Access values
print(student["name"])
print(student.get("age"))

# Add / update values
student["grade"] = "A"
student["marks"] = 90

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
________________________________________
