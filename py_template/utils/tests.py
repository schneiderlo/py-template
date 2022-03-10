import os
from shutil import rmtree

from py_template import ROOT_DIR


def get_project_root() -> str:
  """Return the absolute path to the project directory."""
  return ROOT_DIR


def get_test_data(*args) -> str:
  """Return the absolute path to data.

  Args:
    args: List of string.
  """
  return os.path.join(
    get_project_root(),
    'tests',
    'data',
    *args
  )


def get_test_workspace(*list_dir) -> str:
  """Return a path locacated inside the test workspace directory."""
  return os.path.join(
    get_project_root(),
    'build',
    'tests',
    'workspace',
    *list_dir
  )


def get_test_directory(request, clear: bool = True):
  """Retrieve a test directory.

  Args:
    request: Pytest request.
    clear: Boolean to indicate if the test directory must be clear.

  Return: Path to the test directory.
  """
  dir_name = request.node.name
  directory_path = get_test_workspace(dir_name)
  if os.path.exists(directory_path) and os.path.isdir(directory_path) and clear:
    rmtree(directory_path)
  os.makedirs(directory_path, exist_ok=True)
  return directory_path
