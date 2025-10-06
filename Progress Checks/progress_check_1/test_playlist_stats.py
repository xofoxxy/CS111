from byu_pytest_utils import max_score, dialog, test_files, this_folder, tier

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)

@core
@max_score(25)
@dialog(test_files / "test_CORE_playlist_1.dialog.txt", this_folder / "playlist_stats.py")
def test_CORE_playlist_1():
    ...

@core
@max_score(25)
@dialog(test_files / "test_CORE_playlist_2.dialog.txt", this_folder / "playlist_stats.py")
def test_CORE_playlist_2():
    ...

@core
@max_score(25)
@dialog(test_files / "test_CORE_playlist_3.dialog.txt", this_folder / "playlist_stats.py")
def test_CORE_playlist_3():
    ...

@advanced
@max_score(2)
@dialog(test_files / "test_ADVANCED_playlist_1.dialog.txt", this_folder / "playlist_stats.py")
def test_ADVANCED_playlist_1():
    ...

@advanced
@max_score(4)
@dialog(test_files / "test_ADVANCED_playlist_2.dialog.txt", this_folder / "playlist_stats.py")
def test_ADVANCED_playlist_2():
    ...

@advanced
@max_score(4)
@dialog(test_files / "test_ADVANCED_playlist_3.dialog.txt", this_folder / "playlist_stats.py")
def test_ADVANCED_playlist_3():
    ...

@excellent
@max_score(5)
@dialog(test_files / "test_EXCELLENT_playlist_1.dialog.txt", this_folder / "playlist_stats.py")
def test_EXCELLENT_playlist_1():
    ...

@excellent
@max_score(5)
@dialog(test_files / "test_EXCELLENT_playlist_2.dialog.txt", this_folder / "playlist_stats.py")
def test_EXCELLENT_playlist_2():
    ...

@excellent
@max_score(5)
@dialog(test_files / "test_EXCELLENT_playlist_3.dialog.txt", this_folder / "playlist_stats.py")
def test_EXCELLENT_playlist_3():
    ...
