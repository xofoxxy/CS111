from byu_pytest_utils import max_score, ensure_missing, this_folder, test_files, dialog, run_python_script
from random import seed


seed('My favorite maze is purple!')


@max_score(5)
def test_no_solution(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-s', test_files / 'maze1.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert 'no solution' in captured.out.lower()


@max_score(5)
def test_invalid_or_missing_arguments(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-g')
    captured = capsys.readouterr()
    assert 'usage:' in captured.out.lower()
    assert '-s' in captured.out.lower()
    assert '-g' in captured.out.lower()


@max_score(10)
def test_invalid_maze_size(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-g', '3', '3', test_files / 'maze.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert '3x5' in captured.out.lower()


@max_score(10)
def test_generic_errors(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-s', test_files / 'big_maze.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert 'maximum recursion depth exceeded' in captured.out.lower()


@max_score(10)
@dialog(test_files / 'maze0.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze0.txt')
def test_solve_maze_0():
    ...


@max_score(10)
@dialog(test_files / 'maze2.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze2.txt')
def test_solve_maze_2():
    ...


@max_score(10)
@ensure_missing(this_folder / 'maze3.output.txt')
@dialog(test_files / 'maze3.key.txt', this_folder / 'maze_solver.py',
        '-g', '15', '15', this_folder / 'maze3.output.txt',
        output_file=this_folder / 'maze3.output.txt')
def test_generate_maze_3():
    ...


@max_score(10)
@ensure_missing(this_folder / 'maze4.output.txt')
@dialog(test_files / 'maze4.key.txt', this_folder / 'maze_solver.py',
        '-g', '50', '50', this_folder / 'maze4.output.txt',
        output_file=this_folder / 'maze4.output.txt')
def test_generate_maze_4():
    ...


@max_score(10)
@ensure_missing(this_folder / 'maze5.output.txt')
@dialog(test_files / 'maze5.generated.key.txt', this_folder / 'maze_solver.py',
        '-g', '39', '27', this_folder / 'maze5.output.txt',
        output_file=this_folder / 'maze5.output.txt')
def test_generate_maze_5():
    ...


@max_score(10)
@dialog(test_files / 'maze5.solved.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze5.generated.key.txt')
def test_solve_maze_5():
    ...
