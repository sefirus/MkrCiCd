import os
import pytest


@pytest.fixture(autouse=True)
def prepare_first_file(tmp_path):
    first_file = os.path.join(tmp_path, 'file1.txt')
    with open(first_file, 'w') as file:
        lines = ['same line 1\n',
                 'same line 2\n',
                 'same line 3\n',
                 'diff FIRST FILE 1\n',
                 'same line 4\n',
                 'diff FIRST FILE 2\n',
                 'same line 1\n',
                 'same line 3\n',
                 'diff FIRST FILE 3\n',
                 'same line 2\n',
                 'diff FIRST FILE 4\n'
                 ]
        file.writelines(lines)
    return first_file


@pytest.fixture(autouse=True)
def prepare_second_file(tmp_path):
    second_file = os.path.join(tmp_path, 'file2.txt')
    with open(second_file, 'w') as file:
        lines = ['same line 1\n',
                 'same line 2\n',
                 'same line 3\n',
                 'diff SECOND FILE 1\n',
                 'same line 4\n',
                 'diff SECOND FILE 2\n',
                 'same line 1\n',
                 'same line 3\n',
                 'diff SECOND FILE 3\n',
                 'same line 2\n',
                 'diff SECOND FILE 4\n'
                 ]
        file.writelines(lines)
    return second_file

@pytest.fixture(autouse=True)
def prepare_reader(tmp_path):
    second_file = os.path.join(tmp_path, 'file2.txt')
    with open(second_file, 'w') as file:
        lines = ['same line 1\n',
                 'same line 2\n',
                 'same line 3\n',
                 'diff SECOND FILE 1\n',
                 'same line 4\n',
                 'diff SECOND FILE 2\n',
                 'same line 1\n',
                 'same line 3\n',
                 'diff SECOND FILE 3\n',
                 'same line 2\n',
                 'diff SECOND FILE 4\n'
                 ]
        file.writelines(lines)
    return second_file

