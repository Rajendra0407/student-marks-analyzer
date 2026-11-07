SUBJECT_COUNT = 5
REPORT_FILE = "report.txt"


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg < 0 or avg > 100:
        raise ValueError("Average must be between 0 and 100")
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


def read_marks(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 100:
                print("Marks must be between 0 and 100")
                continue
            return value
        except ValueError:
            print("Please enter a number")


def read_all_marks(subject_count):
    marks = []
    for i in range(subject_count):
        m = read_marks(f"Marks for subject {i + 1}: ")
        marks.append(m)
    return marks


def read_students():
    students = {}
    while True:
        name = input("Student name (or type done): ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("Name cannot be empty")
            continue
        if name in students:
            print(f"{name} already exists. Use a different name.")
            continue
        students[name] = read_all_marks(SUBJECT_COUNT)
    return students


def build_report(students):
    lines = []
    total = 0
    topper_name = ""
    topper_avg = -1

    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = get_grade(avg)
        lines.append(f"{name}: Percentage: {round(avg, 2)} Grade: ({grade})")
        total += avg
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name

    class_avg = total / len(students)
    lines.append(f"Topper: {topper_name} with {round(topper_avg, 2)}")
    lines.append(f"Class average: {round(class_avg, 2)}")
    return lines


def main():
    students = read_students()
    if not students:
        print("No students entered")
        return

    lines = build_report(students)
    for line in lines:
        print(line)

    with open(REPORT_FILE, "w") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"Report saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()