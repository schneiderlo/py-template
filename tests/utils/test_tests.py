import pytest

from py_template.utils.tests import get_test_directory, get_test_data


def test_get_test_data():
  readme_path = get_test_data("example", "README.md")
  with open(readme_path) as f:
    lines = f.readlines()
    assert lines[0] == "This is a very simple readme file.\n"


def test_get_test_directory(request):
  test_dir = get_test_directory(request)
