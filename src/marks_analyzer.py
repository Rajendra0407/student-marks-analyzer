def calculate_average(marks):
    if not marks:              # Check if list is empty
        return 0
    return sum(marks) / len(marks)  # Total / Count

#print(calculate_average([80, 65, 90]))
#print(calculate_average([])


students = {
    "Aman": [80, 65, 90],
    "Riya": [70, 88, 75],
}

for name, marks in students.items():
    avg = calculate_average(marks)
    print(f"{name}: {round(avg, 2)}")

averages = {}

for name, marks in students.items():
    averages[name] = round(calculate_average(marks), 2)

print(averages)