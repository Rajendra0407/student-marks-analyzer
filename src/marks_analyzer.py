def calculate_average(marks):
    if not marks:              # Check if list is empty
        return 0
    return sum(marks) / len(marks)  # Total / Count

#print(calculate_average([80, 65, 90]))
#print(calculate_average([])

def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    elif avg >= 30:
        return "D"
    else:
        return "F"


students = {
    "Aman": [80, 65, 90],
    "Riya": [70, 88, 75],
}

for name, marks in students.items():
    avg = calculate_average(marks)
    grade = get_grade(avg)
    print(f"{name}: Percentage: {round(avg, 2)} Grade: ({grade})")

averages = {}

for name, marks in students.items():
    averages[name] = round(calculate_average(marks), 2)

print(averages)
