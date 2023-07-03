import csv


class CSVReader:

    def __init__(self, file_location):
        self.file_location = file_location

    def read_file(self):
        with open(self.file_location, mode='r') as csv_file:
            data_dict = [{k: v for k, v in row.items()} for row in csv.DictReader(csv_file, skipinitialspace=True)]
            print(data_dict)
            return data_dict
