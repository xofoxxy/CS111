from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import max_score, run_python_script, test_files, ensure_missing, this_folder, with_import
import functools
from pytest import approx, fail
from pathlib import Path


def compare_images(obs: Path | PILImage.Image, exp: Path | PILImage.Image):
    if not isinstance(obs, PILImage.Image):
        observed = PILImage.open(obs).convert('RGB')
    else:
        observed = obs
    if not isinstance(exp, PILImage.Image):
        expected = PILImage.open(exp).convert('RGB')
    else:
        expected = exp

    assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

    diff = ImageChops.difference(observed, expected)
    if bbox := diff.getbbox():
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                if not observed_pixel or not expected_pixel:
                    assert False, f"Failed to get pixels at ({x}, {y})!"

                if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                    assert False, "Failed to get correct pixel type!"

                assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`."
                assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`."
                assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`."

    if isinstance(obs, Path):
        obs.unlink(missing_ok=True)


@max_score(15)
@with_import('byuimage', 'Image')
def test_display_image(Image, monkeypatch):
    observed = None

    @functools.wraps(Image.show)
    def patched_Image_show(self):
        nonlocal observed
        observed = self.image
    monkeypatch.setattr(Image, 'show', patched_Image_show)

    run_python_script(this_folder / 'image_processing.py', '-d',
                      test_files / 'explosion.input.jpg')

    if observed is None:
        fail('No Image was shown')

    compare_images(observed, test_files / 'explosion.input.jpg')


def make_filter_tester(observed_file: Path, key_file: Path, *script_args):
    def decorator(func):
        @functools.wraps(func)
        def inner_func():
            run_python_script(this_folder / 'image_processing.py', *script_args)
            compare_images(observed_file, key_file)
            observed_file.unlink(missing_ok=True)
        return inner_func
    return decorator


@max_score(2.5)
@ensure_missing(this_folder / "darkened-explosion-1.output.png")
@make_filter_tester(
    this_folder / 'darkened-explosion-1.output.png', test_files / 'darkened-explosion-1.key.png',
    '-k', test_files / 'explosion.input.jpg', this_folder / 'darkened-explosion-1.output.png', 0.3
)
def test_darken_filter_1():
    ...

@max_score(2.5)
@ensure_missing(this_folder / "darkenened-explosion-2.output.png")
@make_filter_tester(
    this_folder / 'darkened-explosion-2.output.png', test_files / 'darkened-explosion-2.key.png',
    '-k', test_files / 'explosion.input.jpg', this_folder / 'darkened-explosion-2.output.png', 0.6
)
def test_darken_filter_2():
    ...

@max_score(5)
@ensure_missing(this_folder / "sepia-explosion.output.png")
@make_filter_tester(
    this_folder / 'sepia-explosion.output.png', test_files / 'sepia-explosion.key.png',
    '-s', test_files / 'explosion.input.jpg', this_folder / 'sepia-explosion.output.png'
)
def test_sepia_filter():
    ...


@max_score(5)
@ensure_missing(this_folder / "grayscale-explosion.output.png")
@make_filter_tester(
    this_folder / 'grayscale-explosion.output.png', test_files / 'grayscale-explosion.key.png',
    '-g', test_files / 'explosion.input.jpg', this_folder / 'grayscale-explosion.output.png'
)
def test_grayscale_filter():
    ...


@max_score(2.5)
@ensure_missing(this_folder / "bordered-explosion-1.output.png")
@make_filter_tester(
    this_folder / 'bordered-explosion-1.output.png', test_files / 'bordered-explosion-1.key.png',
    '-b', test_files / 'explosion.input.jpg', this_folder / 'bordered-explosion-1.output.png', 10, 120, 20, 14
)
def test_border_filter_1():
    ...

@max_score(2.5)
@ensure_missing(this_folder / "bordered-explosion-2.output.png")
@make_filter_tester(
    this_folder / 'bordered-explosion-2.output.png', test_files / 'bordered-explosion-2.key.png',
    '-b', test_files / 'explosion.input.jpg', this_folder / 'bordered-explosion-2.output.png', 20, 30, 40, 150
)
def test_border_filter_2():
    ...

@max_score(5)
@ensure_missing(this_folder / "flipped-explosion.output.png")
@make_filter_tester(
    this_folder / 'flipped-explosion.output.png', test_files / 'flipped-explosion.key.png',
    '-f', test_files / 'explosion.input.jpg', this_folder / 'flipped-explosion.output.png'
)
def test_flip_filter():
    ...


@max_score(10)
@ensure_missing(this_folder / "mirrored-explosion.output.png")
@make_filter_tester(
    this_folder / 'mirrored-explosion.output.png', test_files / 'mirrored-explosion.key.png',
    '-m', test_files / 'explosion.input.jpg', this_folder / 'mirrored-explosion.output.png'
)
def test_mirror_filter():
    ...


@max_score(10)
@ensure_missing(this_folder / "collage-1.output.png")
@make_filter_tester(
    this_folder / 'collage-1.output.png', test_files / 'collage-1.key.png',
    '-c', test_files / 'beach1.input.jpg', test_files / 'beach2.input.jpg',
    test_files / 'beach3.input.jpg', test_files / 'beach4.input.jpg',
    this_folder / 'collage-1.output.png', 10
)
def test_collage_filter_1():
    ...

@max_score(10)
@ensure_missing(this_folder / "collage-2.output.png")
@make_filter_tester(
    this_folder / 'collage-2.output.png', test_files / 'collage-2.key.png',
    '-c', test_files / 'beach1.input.jpg', test_files / 'beach2.input.jpg',
    test_files / 'beach3.input.jpg', test_files / 'beach4.input.jpg',
    this_folder / 'collage-2.output.png', 30
)
def test_collage_filter_2():
    ...

@max_score(10)
@ensure_missing(this_folder / "greenscreen-1.output.png")
@make_filter_tester(
    this_folder / 'greenscreen-1.output.png', test_files / 'greenscreen-1.key.png',
    '-y', test_files / 'man.input.jpg', test_files / 'explosion.input.jpg',
    this_folder / 'greenscreen-1.output.png', 90, 1.3
)
def test_greenscreen_filter_1():
    ...

@max_score(10)
@ensure_missing(this_folder / "greenscreen-2.output.png")
@make_filter_tester(
    this_folder / 'greenscreen-2.output.png', test_files / 'greenscreen-2.key.png',
    '-y', test_files / 'man.input.jpg', test_files / 'explosion.input.jpg',
    this_folder / 'greenscreen-2.output.png', 75, 1.4
)
def test_greenscreen_filter_2():
    ...
