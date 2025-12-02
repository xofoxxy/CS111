from byu_pytest_utils import max_score, with_import
import ast
import inspect
from pytest import fail, xfail

@max_score(6)
@with_import('lab14', 'multiply')
def test_multiply(multiply):
    tree = ast.parse(inspect.getsource(multiply))
    recursive_call_seen = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Mult):
            fail('You may not use the * operator in the multiply function')
        elif isinstance(node, ast.Call) and node.func.id == 'multiply':
            recursive_call_seen = True
    if not recursive_call_seen:
        fail('In the multiply function, you must make a recursive call to the multiply function')

    assert multiply(0, 0) == 0
    assert multiply(0, 3) == 0
    assert multiply(0, 4) == 0
    assert multiply(2, 0) == 0
    assert multiply(5, 0) == 0
    assert multiply(3, 1) == 3
    assert multiply(1, 7) == 7
    assert multiply(5, 3) == 15
    assert multiply(4, 7) == 28
    assert multiply(13, 12) == 156


@max_score(7)
@with_import('lab14', 'is_prime')
def test_is_prime(is_prime):
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert is_prime(13)
    assert not is_prime(16)
    assert is_prime(31)
    assert not is_prime(35)


@max_score(7)
@with_import('lab14', 'skip_mul')
def test_skip_mul(skip_mul):
    tree = ast.parse(inspect.getsource(skip_mul))
    recursive_call_seen = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and node.func.id == 'skip_mul':
            recursive_call_seen = True
    if not recursive_call_seen:
        fail('In the skip_mul function, you must make a recursive call to the skip_mul function')

    assert skip_mul(1) == 1
    assert skip_mul(2) == 2
    assert skip_mul(5) == 15
    assert skip_mul(6) == 48
    assert skip_mul(8) == 384


@max_score(0)
def test_hailstone():
    try:
        @with_import('lab14', 'hailstone')
        def inner_hailstone(hailstone):
            import sys
            from io import StringIO

            tree = ast.parse(inspect.getsource(hailstone))
            recursive_call_seen = any(
                isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'hailstone'
                for node in ast.walk(tree)
            )
            if not recursive_call_seen:
                raise Exception('In the hailstone function, you must make a recursive call to the hailstone function')

            for value, expected_steps in [(1, 1), (2, 2), (3, 8), (4, 3), (5, 6), (10, 7)]:
                captured_output = StringIO()
                original_stdout = sys.stdout
                sys.stdout = captured_output
                try:
                    result = hailstone(value)
                finally:
                    sys.stdout = original_stdout
                output = captured_output.getvalue().strip().split('\n')

                assert result == expected_steps, f"Expected {expected_steps} steps for {value}, got {result}"
                assert all(line.strip().isdigit() for line in output), f"Output should contain integers, got {output}"
                assert int(output[0]) == value, f"First printed value should be {value}, got {output[0]}"
                assert int(output[-1]) == 1, f"Last printed value should be 1, got {output[-1]}"
                assert len(output) == expected_steps, f"Expected {expected_steps} printed values, got {len(output)}"

        inner_hailstone()
    except Exception as e:
        xfail(f'\nOPTIONAL: hailstone() is not implemented correctly: {e}')


@max_score(0)
def test_paths():
    try:
        @with_import('lab14', 'paths')
        def inner_paths(paths):
            tree = ast.parse(inspect.getsource(paths))
            recursive_call_seen = any(
                isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'paths'
                for node in ast.walk(tree)
            )
            if not recursive_call_seen:
                raise Exception('In the paths function, you must make a recursive call to the paths function')

            for m, n, expected in [(1, 1, 1), (2, 2, 2), (3, 3, 6), (5, 7, 210), (117, 1, 1), (1, 157, 1), (0, 0, 0), (0, 5, 0), (5, 0, 0)]:
                result = paths(m, n)
                assert result == expected, f"Expected {expected} paths for {m}, {n}, got {result}"

        inner_paths()
    except Exception as e:
        xfail(f'\nOPTIONAL: paths() is not implemented correctly: {e}')
