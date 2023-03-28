from FileReader import FileReader


def test_getting_same(prepare_first_file, prepare_second_file):
    expected = ['same line 1\n',
                'same line 2\n',
                'same line 3\n',
                'same line 4\n']
    reader = FileReader(prepare_first_file, prepare_second_file)
    same = reader.get_same()
    assert set(same) == set(expected)

