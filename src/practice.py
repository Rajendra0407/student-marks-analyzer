def read_marks():
    while True:
        try:
            value = float(input("Enter marks: "))

            if value < 0 or value > 100:
                print("OUT OF RANGE (Enter marks between 0 and 100)")
                continue

            return value

        except ValueError:
            print("NOT A NUMBER (Please enter numeric marks)")


marks = read_marks()
print("Your marks:", marks)