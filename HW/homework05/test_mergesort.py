from byu_pytest_utils import max_score, test_files, this_folder, ensure_missing
import runpy, sys

def check_output_file(output_file, expected_file):
    try:
        with open(output_file, 'r') as ofile, open(expected_file, 'r') as tfile:
                assert ofile.read() == tfile.read(), "Output file does not match expected file"
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Couldn't find the output file: {e}")


@max_score(15)
@ensure_missing(this_folder / 'test1.output.txt')
def test_mergesort_already_sorted_data():
    # run mergesort.py
    sys.argv = ['mergesort.py', str(test_files / 'test1.input.txt'), str(this_folder / 'test1.output.txt')]
    runpy.run_path(str(this_folder / 'mergesort.py'), run_name='__main__')
    check_output_file(this_folder / 'test1.output.txt', test_files / 'test1.key.txt')


@max_score(15)
@ensure_missing(this_folder / 'test2.output.txt')
def test_mergesort_reversed_data():
    # run mergesort.py
    sys.argv = ['mergesort.py', str(test_files / 'test2.input.txt'), str(this_folder / 'test2.output.txt')]
    runpy.run_path(str(this_folder / 'mergesort.py'), run_name='__main__')
    check_output_file(this_folder / 'test2.output.txt', test_files / 'test2.key.txt')


@max_score(15)
@ensure_missing(this_folder / 'test3.output.txt')
def test_mergesort_shuffled_data():
    # run mergesort.py
    sys.argv = ['mergesort.py', str(test_files / 'test3.input.txt'), str(this_folder / 'test3.output.txt')]
    runpy.run_path(str(this_folder / 'mergesort.py'), run_name='__main__')
    check_output_file(this_folder / 'test3.output.txt', test_files / 'test3.key.txt')
