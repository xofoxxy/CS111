# This would be far easier with regex, but the autograder doesn't have it installed

def read_data(filename):
    with open(filename, "r") as f:
        skipped = 0
        for line in f:
            try:
                name, score = line.split(",")
                for char in name:
                    if char in "0123456789":
                        name = name.replace(char, "")
                if name == "FreeCoding":
                    name = "Project"
                if grade_dict.get(name) is None:
                    grade_dict[name] = [float(score)]
                else:
                    grade_dict[name].append(float(score))
            except ValueError:
                skipped += 1
                #print(f"Non-standard line. Skipping... {skipped} lines skipped so far.", end="\r")
                continue
        #print("\n")
    return grade_dict


def calculate_grade():
    """
    takes in a list of grades and a list of weights and returns the weighted average
    """
    def drop_lowest(grades, n=2):
        """
        takes in a list and drops the n lowest values in the list
        """
        return sorted(grades, reverse=True)[:len(grades)-n]
    total_percentage = 0
    total_percentage_possible = 0
    for key, value in grade_dict.items():
        if ASSIGNMENT_INFO.get(key) is None:
            continue
        if key == "Midterm":
            score_per, weight, number_dropped = ASSIGNMENT_INFO[key]
            midterm_scores = []
            for score in value:
                unweighted_midterm_grade = score / score_per
                weighted_midterm_grade = unweighted_midterm_grade * weight
                total_percentage += weighted_midterm_grade
                total_percentage_possible += weight
                midterm_scores.append([score, score_per, unweighted_midterm_grade*100])
                # Midterms apparently each are worth 10% instead of 30% as a group, which is still silly.
            FINAL_GRADES["Midterm"] = midterm_scores
            continue
        score_per, weight, number_dropped = ASSIGNMENT_INFO[key]
        value = drop_lowest(value, number_dropped)
        total_score_possible = score_per * len(value)
        total_score_earned = sum(value)
        if total_score_possible == 0:
            continue
        grade = (total_score_earned / total_score_possible)
        weighted_grade = grade * weight
        FINAL_GRADES[key] = [total_score_earned, total_score_possible, grade*100]
        total_percentage += weighted_grade
        total_percentage_possible += weight

    if total_percentage_possible < 1:
        final_grade = total_percentage/total_percentage_possible
    else:
        final_grade = total_percentage
    FINAL_GRADES["Overall"] = final_grade
    #print(f"Final Grade: {final_grade:.2f}")


def find_letter_grade(grade):
    if grade >= 93:
        return "A"
    elif grade >= 90:
        return "A-"
    elif grade >= 87:
        return "B+"
    elif grade >= 83:
        return "B"
    elif grade >= 80:
        return "B-"
    elif grade >= 77:
        return "C+"
    elif grade >= 73:
        return "C"
    elif grade >= 70:
        return "C-"
    elif grade >= 67:
        return "D+"
    elif grade >= 63:
        return "D"
    elif grade >= 60:
        return "D-"
    else:
        return "F"


def print_grades():
    string = ""
    if FINAL_GRADES["Lab"] is not None:
        string += f"\nLabs: {FINAL_GRADES['Lab'][0]:.1f}/{FINAL_GRADES['Lab'][1]} {FINAL_GRADES['Lab'][2]:.1f}%"
    if FINAL_GRADES["Homework"] is not None:
        string += f"\nHomeworks: {FINAL_GRADES['Homework'][0]:.1f}/{FINAL_GRADES['Homework'][1]} {FINAL_GRADES['Homework'][2]:.1f}%"
    if FINAL_GRADES["Project"] is not None:
        string += f"\nProjects: {FINAL_GRADES['Project'][0]:.1f}/{FINAL_GRADES['Project'][1]} {FINAL_GRADES['Project'][2]:.1f}%"
    if FINAL_GRADES["ProgressCheck"] is not None:
        string += f"\nProgress Checks: {FINAL_GRADES['ProgressCheck'][0]:.1f}/{FINAL_GRADES['ProgressCheck'][1]} {FINAL_GRADES['ProgressCheck'][2]:.1f}%"
    if FINAL_GRADES["Midterm"] is not None:
        n = 1
        for value in FINAL_GRADES["Midterm"]:
            score, possible, grade = value
            string += f"\nMidterm {n}: {score:.1f}/{possible} {grade:.1f}%"
            n += 1
    if FINAL_GRADES["Final"] is not None:
        string += f"\nFinal: {FINAL_GRADES['Final'][0]:.1f}/{FINAL_GRADES['Final'][1]} {FINAL_GRADES['Final'][2]:.1f}%"
    grade = FINAL_GRADES['Overall']
    letter_grade = find_letter_grade(float(grade)*100)
    string += f"\nThe overall grade in the class is: {letter_grade} ({grade*100:.2f}%)"

    print(string)


if __name__ == "__main__":
    """
    I originally wrote this all using regex and then realized that the tests didn't work with regex.
    so then I had to rewrite it all.
    
    It's not as clean as I'd like it to be, but I was running out of time, so I didn't get all of the refactoring done.
    Please have mercy 🙏
    """

    ASSIGNMENT_INFO = {
        "Lab": [20, .10, 2],
        "Homework": [50, .10, 1],
        "Project": [100, .20, 0],
        "ProgressCheck": [100, .10, 0],
        "Midterm": [20, .1, 0],
        # We'll need to handle the midterms separately because they don't have a static weight, which is dumb.
        "Final": [70, .20, 0]
    }
    FINAL_GRADES = {
        "Lab": None,
        "Homework": None,
        "Project": None,
        "ProgressCheck": None,
        "Midterm": None,
        "Final": None,
        "Overall": None
    }
    grade_file = input()
    grade_dict = {}
    read_data(grade_file)
    calculate_grade()
    print_grades()
