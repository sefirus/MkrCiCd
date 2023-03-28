from FileReader import FileReader


def test_getting_same(prepare_normal_first_file, prepare_normal_second_file):
    expected = ['same line 1\n',
                'same line 2\n',
                'same line 3\n',
                'same line 4\n']
    reader = FileReader(prepare_normal_first_file, prepare_normal_second_file)
    same = reader.get_same()
    assert set(same) == set(expected)


def test_getting_diff(prepare_normal_first_file, prepare_normal_second_file):
    expected = ['diff FIRST FILE 1\n',
                'diff FIRST FILE 2\n',
                'diff FIRST FILE 3\n',
                'diff FIRST FILE 4\n',
                'diff SECOND FILE 1\n',
                'diff SECOND FILE 2\n',
                'diff SECOND FILE 3\n',
                'diff SECOND FILE 4\n']
    reader = FileReader(prepare_normal_first_file, prepare_normal_second_file)
    diff = reader.get_difference()
    assert set(diff) == set(expected)


def test_getting_full_diff(prepare_full_diff_first_file, prepare_full_diff_second_file):
    expected_same = []
    expected_diff = ['diff FIRST FILE 1\n',
                     'diff FIRST FILE 2\n',
                     'diff FIRST FILE 3\n',
                     'diff SECOND FILE 1\n',
                     'diff SECOND FILE 2\n',
                     'diff SECOND FILE 3\n',
                     'diff SECOND FILE 4\n',
                     'diff SECOND FILE 5\n']
    reader = FileReader(prepare_full_diff_first_file, prepare_full_diff_second_file)
    same = reader.get_same()
    diff = reader.get_difference()
    assert set(expected_same) == set(same)
    assert  len(set(diff)) > 0


def test_getting_full_same(prepare_full_same_first_file, prepare_full_same_second_file):
    expected_diff = []
    reader = FileReader(prepare_full_same_first_file, prepare_full_same_second_file)
    same = reader.get_same()
    diff = reader.get_difference()
    assert len(set(same)) > 0
    assert set(expected_diff) == set(diff)
