class FileReader:

    def __init__(self, first_file_path: str, second_file_path: str):
        with open(first_file_path, 'r') as first_file, open(second_file_path, 'r') as second_file2:
            self.first_file_lines = set(first_file.readlines())
            self.second_file_lines = set(second_file2.readlines())

    def get_difference(self):
        diff_lines = self.first_file_lines.symmetric_difference(self.second_file_lines)
        return diff_lines

    def get_same(self):
        same_lines = self.first_file_lines.intersection(self.second_file_lines)
        return same_lines

    def write_diff(self):
        lines_to_write = self.get_difference()
        self.write_to_file(lines_to_write, 'diff.txt')

    def write_same(self):
        lines_to_write = self.get_same()
        self.write_to_file(lines_to_write, 'same.txt')

    def write_to_file(self, lines: [str], file_name: str):
        with open(file_name, 'w') as file:
            for line in lines:
                file.write(line)

