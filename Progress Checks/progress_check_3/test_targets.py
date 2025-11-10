from byu_pytest_utils import max_score, with_import, tier

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


def link_eq(Link, left, right):
    if left is not Link.empty and not isinstance(left, Link):
        return False
    if right is not Link.empty and not isinstance(right, Link):
        return False
    while left is not Link.empty and right is not Link.empty:
        if left.first != right.first:
            return False
        left = left.rest
        right = right.rest
    if left is not Link.empty or right is not Link.empty:
        return False
    return True

@core
@max_score(0)
@with_import('targets', 'count_targets')
@with_import('targets', 'Link')
def test_CORE_count_targets_1(Link, count_targets):
    link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
    targets = [2, 4, 'b']
    key = {2: 3, 'b': 1, 4: 2}
    output = count_targets(link, targets)
    assert output == key

@core
@max_score(0)
@with_import('targets', 'count_targets')
@with_import('targets', 'Link')
def test_CORE_count_targets_2(Link, count_targets):
    link = Link(1)
    targets = [1]
    key = {1: 1}
    output = count_targets(link, targets)
    assert output == key

@core
@max_score(0)
@with_import('targets', 'count_targets')
@with_import('targets', 'Link')
def test_CORE_count_targets_3(Link, count_targets):
    link = Link(0, Link(1, Link(4, Link(1, Link(4, Link(2, Link(3, Link(4, Link(5, Link(8, Link(12, Link(13))))))))))))
    targets = [4, 12, 0]
    key = {4: 3, 12: 1, 0: 1}
    output = count_targets(link, targets)
    assert output == key

@advanced
@max_score(0)
@with_import('targets', 'remove_targets')
@with_import('targets', 'Link')
def test_ADVANCED_remove_targets_1(Link, remove_targets, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
    targets = [2, 4, 'b']
    key = Link('c', Link('a', Link('t', Link('s'))))
    output = remove_targets(link, targets)
    assert output == key

@advanced
@max_score(0)
@with_import('targets', 'remove_targets')
@with_import('targets', 'Link')
def test_ADVANCED_remove_targets_2(Link, remove_targets, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    link = Link(1)
    targets = [1]
    key = ()
    output = remove_targets(link, targets)
    assert output == key

@advanced
@max_score(0)
@with_import('targets', 'remove_targets')
@with_import('targets', 'Link')
def test_ADVANCED_remove_targets_3(Link, remove_targets, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    link = Link(0, Link(1, Link(4, Link(1, Link(4, Link(2, Link(3, Link(4, Link(5, Link(8, Link(12, Link(13))))))))))))
    targets = [4, 12, 0]
    key = Link(1, Link(1, Link(2, Link(3, Link(5, Link(8, Link(13)))))))
    output = remove_targets(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_iterative')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_iterative_1(Link, count_targets_iterative):
    link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
    targets = [2, 4, 'b']
    key = {2: 3, 'b': 1, 4: 2}
    output = count_targets_iterative(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_iterative')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_iterative_2(Link, count_targets_iterative):
    link = Link(1)
    targets = [1]
    key = {1: 1}
    output = count_targets_iterative(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_iterative')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_iterative_3(Link, count_targets_iterative):
    link = Link(0, Link(1, Link(4, Link(1, Link(4, Link(2, Link(3, Link(4, Link(5, Link(8, Link(12, Link(13))))))))))))
    targets = [4, 12, 0]
    key = {4: 3, 12: 1, 0: 1}
    output = count_targets_iterative(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_recursive')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_recursive_1(Link, count_targets_recursive):
    link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
    targets = [2, 4, 'b']
    key = {2: 3, 'b': 1, 4: 2}
    output = count_targets_recursive(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_recursive')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_recursive_2(Link, count_targets_recursive):
    link = Link(1)
    targets = [1]
    key = {1: 1}
    output = count_targets_recursive(link, targets)
    assert output == key

@excellent
@max_score(0)
@with_import('targets', 'count_targets_recursive')
@with_import('targets', 'Link')
def test_EXCELLENT_count_targets_recursive_3(Link, count_targets_recursive):
    link = Link(0, Link(1, Link(4, Link(1, Link(4, Link(2, Link(3, Link(4, Link(5, Link(8, Link(12, Link(13))))))))))))
    targets = [4, 12, 0]
    key = {4: 3, 12: 1, 0: 1}
    output = count_targets_recursive(link, targets)
    assert output == key
