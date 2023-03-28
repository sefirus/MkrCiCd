from FileReader import FileReader

worker = FileReader('files/file1.txt', 'files/file2.txt')
print(worker.get_same())
print(worker.get_difference())
worker.write_diff()
worker.write_same()
