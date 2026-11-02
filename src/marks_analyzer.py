def calculate_average(marks):
    if not marks:              # Check if list is empty
        return 0
    return sum(marks) / len(marks)  # Total / Count

print(calculate_average([80, 65, 90]))
print(calculate_average([]))