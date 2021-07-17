import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def test_backward_arrow():
    path_to_file = os.path.join(BASE_DIR, 'images', 'icons', 'backward_arrow_icon.png')
    assert os.path.exists(path_to_file)

def test_forward_arrow():
    path_to_file = os.path.join(BASE_DIR, 'images', 'icons', 'forward_arrow_icon.png')
    assert os.path.exists(path_to_file)

def test_refresh_btn():
    path_to_file = os.path.join(BASE_DIR, 'images', 'icons', 'refresh_btn.png')
    assert os.path.exists(path_to_file)
