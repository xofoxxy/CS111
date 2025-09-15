# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def clear_files():
    with open("chosen_students.csv", "w") as f:
        f.write("")
    with open("outliers.csv", "w") as f:
        f.write("")
    with open("chosen_improved.csv", "w") as f:
        f.write("")
    with open("better_improved.csv", "w") as f:
        f.write("")
    with open("composite_chosen.csv", "w") as f:
        f.write("")
    with open("student_scores.csv", "w") as f:
        f.write("")


# define your functions here
def get_student_info(row):
    row = row.split(",")
    try:
        student = {"name": row[0],
                   "sat": float(row[1]),
                   "gpa": float(row[2]),
                   "interest": float(row[3]),
                   "hs_quality": float(row[4]),
                   "s1": float(row[5]),
                   "s2": float(row[6]),
                   "s3": float(row[7]),
                   "s4": float(row[8])
                   }
        return student
    except Exception as e:
        print(f"error when figuring out the student: {e}")
        return None


def calculate_score(student):
    score = (0.3 * float(student["sat"]/160) + 0.4 * float(student["gpa"]*2) +
             0.1 * float(student["interest"]) + 0.2 * float(student["hs_quality"]))
    student["score"] = score
    with open("student_scores.csv", "a") as f:
        f.write(f"{student['name']},{score:.2f}\n")
    return student


def chosen_students(student):
    if student["score"] >= 6:
        student["chosen"] = True
        with open("chosen_students.csv", "a") as f:
            f.write(f"{student['name']}\n")
    else:
        student["chosen"] = False


def is_outlier(student):
    if student["interest"] == 0 or student["gpa"]*2 > student["sat"]/160:
        print(student["name"] + " is an outlier!")
        student["outlier"] = True
        with open("outliers.csv", "a") as f:
            f.write(f"{student['name']}\n")
        return True
    else:
        student["outlier"] = False
        return False


def chosen_improved(student):
    if student["score"] >= 6 or (student["outlier"] and student["score"] >= 5):
        student["chosen_imp"] = True
        with open("chosen_improved.csv", "a") as f:
            f.write(f"{student['name']}\n")
    else:
        student["chosen_imp"] = False


def check_improved(student):
    if student["s1"] <= student["s2"] <= student["s3"] <= student["s4"]:
        student["improved"] = True
        return True
    else:
        student["improved"] = False
        return False


def check_for_grade_outlier(student):
    lowest = 100
    second_lowest = 100
    for grades in [student["s1"], student["s2"], student["s3"], student["s4"]]:
        if grades < lowest:
            second_lowest = lowest
            lowest = grades
        elif grades < second_lowest:
            second_lowest = grades

    if second_lowest - lowest > 20:
        student["grade_outlier"] = True
        print(student["name"] + " is a grade outlier!")
        return True
    else:
        student["grade_outlier"] = False
        return False


def better_improved(student):
    check_improved(student)
    check_for_grade_outlier(student)
    if student["score"] >= 6 or (student["score"] >= 5 and (student["outlier"] or student["grade_outlier"] or student["improved"])):
        student["better_imp"] = True
        string = f"{student['name']},{student['sat']},{student['gpa']},{student['interest']},{student['hs_quality']}"
        with open("better_improved.csv", "a") as f:
            f.write(string.strip())
            f.write("\n")
        with open("composite_chosen.csv", "a") as f:
            f.write(f"{student['name']}")
            f.write("\n")


def check_list_eligibility(student):
    chosen_students(student)
    is_outlier(student)
    chosen_improved(student)
    better_improved(student)
    # composite_chosen(student) # this is also resolved in better improved


def main():
    filename = "admission_algorithms_dataset.csv"
    clear_files()
    input_file = open(filename, "r")

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    students = []
    for lines in input_file:
        student = get_student_info(lines)
        if student:
            student = calculate_score(student)
            students.append(student)
    for student in students:
        print(student)
        check_list_eligibility(student)
    print("done!")
    input_file.close()


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
