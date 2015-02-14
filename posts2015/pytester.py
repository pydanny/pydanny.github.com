import glob
import os
import pytest

TEST_ROOT = "testsforpython"


def extract(filename, lines):
    """Args:
        Filename for displaying error messages
        lines for the text in the file
    """
    in_block = False
    code_blocks = []
    block = ""

    for line in lines:
        line = line.replace("\n", "")
        if line.startswith(".. code-block:: python"):
            in_block = True
            continue

        if line.startswith("    >>>") and in_block == True:
            in_block = False
            continue

        # Code goes here
        if line.startswith(" ") and in_block == True:
            line = line[4:]  # kill the first tab
            block += line + "\n"
            continue

        # Adding blank lines
        if in_block == True and len(line.strip()) == 0:
            block += line + "\n"
            continue

        # Start of non-code line
        if in_block == True and not line.startswith("    "):
            code_blocks.append(block)
            block = ""
            in_block = False

    # in case a .rst file ends on a code sample, this will add the code
    #   same to the code_blocks.
    if in_block == True:
        code_blocks.append(block)

    # Print results
    print("{} has {} code blocks".format(filename, len(code_blocks)))
    return code_blocks


def sort_code_blocks(code_blocks):
    working_blocks = []
    testing_blocks = []
    for block in code_blocks:
        if "(unittest.TestCase)" in block or "def test_" in block:
            testing_blocks.append(block)
            continue
        working_blocks.append(block)

    return working_blocks + testing_blocks


def mk_test_dir(dir_path):
    os.makedirs(dir_path)
    init_file = os.path.join(dir_path, "__init__.py")
    with open(init_file, "w") as f:
        f.write("# boilerplate")


def mk_test_filename(filename, test_root=TEST_ROOT):
    """ 1. Returns a test filename
        2. Sets up the file structure for the filename"""
    test_filename = os.path.join(test_root, filename)
    test_filename = test_filename.replace(".rst", ".py")
    test_path, filename = os.path.split(test_filename)
    if not os.path.exists(test_root):
        mk_test_dir(test_root)
    if not os.path.exists(test_path):
        mk_test_dir(test_path)
    return test_filename


if __name__ == "__main__":

    print("Compiling tests into the {} directory...".format(TEST_ROOT))
    for filename in glob.glob("*.rst"):

        with open(filename) as f:
            lines = f.readlines()
        code_blocks = extract(filename, lines)
        code_blocks = sort_code_blocks(code_blocks)
        test_filename = mk_test_filename(filename)

        # normal .rst files
        with open(test_filename, "w") as f:
            f.write("# -*- coding: utf-8 -*-\n")
            for block in code_blocks:
                f.write(block)
    print("Running py.test...")
    pytest.main("testsforpython/")
    print("pytester.py has completed its run. Hopefully all tests passed!")