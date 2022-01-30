# Created by: Zack Isingoma
# Created on: 28th Jan 2022.
# Finds and displays the average of user marks
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def main():
    # this function uses an array
    print("Welcome")
    student_marks = []

    # input
    for marks in range(0, 10):
        a_single_mark = input("Enter a mark (percentage): ")
    # try catch
        try:
            a_single_mark_int = int(a_single_mark)
            if a_single_mark_int > MIN_NUM:
                student_marks.append(a_single_mark_int)
                average = sum(student_marks) / 10
            if a_single_mark_int > MAX_NUM:
                print("Number is greater than 100")
        except Exception:
            print("Invalid input")

    print("")
    print("The average of the given marks is\n{:.2f}".format(average))


if __name__ == "__main__":
    main()
