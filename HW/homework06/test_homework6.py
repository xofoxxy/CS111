from byu_pytest_utils import max_score, with_import


def get_request_guard_domain(RequestGuard):
    guard = RequestGuard("https://cs111.byu.edu")
    # Mocking a different robots.txt
    guard.forbidden = ['/data', '/images', '/lectures']
    return guard


def get_request_guard_subdomain(RequestGuard):
    guard = RequestGuard("https://cs111.byu.edu/Homework/homework07/")
    # Mocking a different robots.txt
    guard.forbidden = ['/data', '/images', '/lectures']
    return guard


def get_request_guard_offsite_domain(RequestGuard):
    guard = RequestGuard("https://code.visualstudio.com")
    # Mocking a different robots.txt
    guard.forbidden = ['/data', '/images', '/lectures']
    return guard


@max_score(11.25)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_domain(RequestGuard):
    guard = get_request_guard_domain(RequestGuard)
    assert guard.can_follow_link('https://cs111.byu.edu/Homework/homework01')
    assert guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/images/cat.jpg')
    assert not guard.can_follow_link('https://byu.edu')
    assert not guard.can_follow_link('https://cs111.byu.edu/images/logo.png')
    assert not guard.can_follow_link('https://cs111.byu.edu/data/spectra1.txt')

    assert RequestGuard('https://cs111.byu.edu').forbidden == ['/Projects/project04/assets/page5.html']


@max_score(11.25)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_subdomain(RequestGuard):
    guard = get_request_guard_subdomain(RequestGuard)
    assert guard.can_follow_link('https://cs111.byu.edu/Homework/homework01')
    assert guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/images/cat.jpg')
    assert not guard.can_follow_link('https://www.wikipedia.org')
    assert not guard.can_follow_link('https://cs111.byu.edu/images/logo.png')
    assert not guard.can_follow_link('https://cs111.byu.edu/data/spectra1.txt')

    assert RequestGuard('https://cs111.byu.edu/Homework/homework07/').forbidden == ['/Projects/project04/assets/page5.html']


@max_score(11.25)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_offsite_domain(RequestGuard):
    guard = get_request_guard_offsite_domain(RequestGuard)
    assert guard.can_follow_link('https://code.visualstudio.com/Homework/homework01')
    assert guard.can_follow_link('https://code.visualstudio.com/Projects/Project4/images/cat.jpg')
    assert not guard.can_follow_link('https://www.jetbrains.com')
    assert not guard.can_follow_link('https://code.visualstudio.com/images/logo.png')
    assert not guard.can_follow_link('https://code.visualstudio.com/data/spectra1.txt')

    assert RequestGuard('https://code.visualstudio.com/Homework/homework07/').forbidden == ['/raw']


@max_score(11.25)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_make_get_request(RequestGuard):
    guard = RequestGuard("https://cs111.byu.edu")
    assert guard.forbidden == ['/Projects/project04/assets/page5.html']

    for i in range(1, 5):
        assert guard.make_get_request(f'https://cs111.byu.edu/Projects/project04/assets/page{i}.html').status_code == 200
    assert guard.make_get_request('https://cs111.byu.edu/Projects/project04/assets/page5.html') == None
