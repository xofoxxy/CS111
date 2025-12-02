from byu_pytest_utils import max_score, test_files, this_folder, with_import, ensure_missing

@ensure_missing(this_folder / 'download.key.html')
@max_score(5)
@with_import('lab20', 'download')
def test_download(download):
    with open(test_files / 'download.key.html') as fin:
        expected = fin.read()

    download('https://cs111.byu.edu/Labs/lab20/assets/webpage.html',
             this_folder / 'download.output.html')
    with open(this_folder / 'download.output.html') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'make_pretty.output.html')
@max_score(5)
@with_import('lab20', 'make_pretty')
def test_make_pretty(make_pretty):
    with open(test_files / 'make_pretty.key.html') as fin:
        expected = fin.read()

    make_pretty('https://cs111.byu.edu/Labs/lab20/assets/webpage.html',
                this_folder / 'make_pretty.output.html')
    with open(this_folder / 'make_pretty.output.html') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'find_paragraphs.output.html')
@max_score(5)
@with_import('lab20', 'find_paragraphs')
def test_find_paragraphs(find_paragraphs):
    with open(test_files / 'find_paragraphs.key.txt') as fin:
        expected = fin.read()

    find_paragraphs('https://cs111.byu.edu/Labs/lab20/assets/webpage.html',
                    this_folder / 'find_paragraphs.output.txt')
    with open(this_folder / 'find_paragraphs.output.txt') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'find_links.output.html')
@max_score(5)
@with_import('lab20', 'find_links')
def test_find_links(find_links):
    with open(test_files / 'find_links.key.txt') as fin:
        expected = fin.read()

    find_links('https://cs111.byu.edu/Labs/lab20/assets/webpage.html',
               this_folder / 'find_links.output.txt')
    with open(this_folder / 'find_links.output.txt') as fin:
        observed = fin.read()

    assert observed == expected
