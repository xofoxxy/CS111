from byu_pytest_utils import dialog, max_score, test_files, this_folder

@max_score(22.5)
@dialog(test_files / 'input1.dialog.txt', this_folder / "grade_calculator.py")
def test_grade_1():
    ...

@max_score(22.5)
@dialog(test_files / 'input2.dialog.txt', this_folder / 'grade_calculator.py')
def test_grade_2():
    ...

@max_score(22.5)
@dialog(test_files / 'input3.dialog.txt', this_folder / 'grade_calculator.py')
def test_grade_3():
    ...

@max_score(22.5)
@dialog(test_files / 'input4.dialog.txt', this_folder / 'grade_calculator.py')
def test_grade_4():
    ...
