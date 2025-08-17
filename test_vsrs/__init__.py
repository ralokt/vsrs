import pytest
from PIL import Image, ImageChops

from vsrs.rescale import rescale


@pytest.fixture
def simple_skin(replay_path):
    return Image.open(str(replay_path / "simple.bmp"))


@pytest.fixture
def simple_24px_skin(replay_path):
    return Image.open(str(replay_path / "simple_24px.bmp"))


@pytest.fixture
def simple_33px_skin(replay_path):
    return Image.open(str(replay_path / "simple_33px.bmp"))


@pytest.fixture
def coloursonly_skin(replay_path):
    return Image.open(str(replay_path / "coloursonlyskin.bmp"))


@pytest.fixture
def ref_32px_nn_5(replay_path):
    return Image.open(str(replay_path / "ref_32px_nn_5.png")).convert("RGB")


def image_eq(im1, im2):
    if im1.size != im2.size:
        return False
    if im1.mode != im2.mode:
        return False
    diff = ImageChops.difference(im1, im2)
    return diff.getbbox() is None


def test_dimensions(simple_skin, simple_24px_skin, simple_33px_skin):
    assert image_eq(rescale(simple_skin, 24, "#0000ff"), simple_24px_skin)
    assert not image_eq(rescale(simple_skin, 24, "#00ff00"), simple_24px_skin)
    assert image_eq(rescale(simple_skin, 33, "#0000ff"), simple_33px_skin)
    assert not image_eq(rescale(simple_skin, 33, "#00ff00"), simple_33px_skin)
    assert image_eq(rescale(simple_24px_skin, 33, "#0000ff"), simple_33px_skin)
    assert image_eq(rescale(simple_33px_skin, 24, "#0000ff"), simple_24px_skin)


def test_scaling_5(coloursonly_skin, ref_32px_nn_5):
    scaled = rescale(coloursonly_skin, 32, "#0000ff")
    scaled_5 = scaled.crop((160, 0, 160 + 32, 32))
    assert image_eq(scaled_5, ref_32px_nn_5)
