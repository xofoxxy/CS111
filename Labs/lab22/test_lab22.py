from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, ensure_missing
from pytest import xfail

@ensure_missing(this_folder / 'sample.output.txt')
@max_score(6)
def test_sample_scavenger_hunt():
    with open(test_files / 'sample.key.png', 'r') as fin:
        expected = fin.read()

    obs_path = this_folder / 'sample.output.txt'
    run_python_script(str(this_folder / 'lab22.py'), 'https://cs111.byu.edu/Labs/lab22/assets/sample1.html',
                      'li', 'checkpoint1', obs_path)

    with open(obs_path, 'r') as fin:
        observed = fin.read()
    obs_path.unlink(missing_ok=True)

    assert observed == expected


@ensure_missing(this_folder / 'mediumhunt.output.txt')
@max_score(7)
def test_medium_scavenger_hunt():
    with open(test_files / 'mediumhunt.key.png', 'r') as fin:
        expected = fin.read()

    obs_path = this_folder / 'mediumhunt.output.txt'
    run_python_script(str(this_folder / 'lab22.py'), 'https://cs111.byu.edu/Labs/lab22/assets/webpage1.html',
                      'p', 'mediumhunt-checkpoint1', obs_path)

    with open(obs_path, 'r') as fin:
        observed = fin.read()
    obs_path.unlink(missing_ok=True)

    assert observed == expected


@ensure_missing(this_folder / 'longhunt.output.txt')
@max_score(7)
def test_long_scavenger_hunt():
    with open(test_files / 'longhunt.key.png', 'r') as fin:
        expected = fin.read()

    obs_path = this_folder / 'longhunt.output.txt'
    run_python_script(str(this_folder / 'lab22.py'), 'https://cs111.byu.edu/Labs/lab22/assets/webpage4.html',
                      'ul', 'longhunt-checkpoint1', obs_path)

    with open(obs_path, 'r') as fin:
        observed = fin.read()
    obs_path.unlink(missing_ok=True)

    assert observed == expected


@max_score(0)
def test_relative_links():
    try:
        @ensure_missing(this_folder / 'relative.output.txt')
        def inner_relative_links():
            with open(test_files / 'relative.key.png') as fin:
                expected = fin.read()

            obs_path = this_folder / 'relative.output.txt'
            run_python_script(str(this_folder / 'lab22.py'), 'https://cs111.byu.edu/Labs/lab22/assets/webpage10.html',
                              'footer', 'link-checkpoint1', obs_path)

            with open(obs_path) as fin:
                observed = fin.read()
            obs_path.unlink(missing_ok=True)

            assert observed == expected
        inner_relative_links()
    except Exception as e:
        xfail(f'\nOPTIONAL: going further with relative links is not implemented correctly:\n{e}')

