from byu_pytest_utils import max_score, with_import

@max_score(10)
@with_import('digit_counter', 'even_digit_counter')
def test_digit_counter(even_digit_counter):
    assert even_digit_counter(1112) == 1
    assert even_digit_counter(1832233) == 3
    assert even_digit_counter(134) == 1
