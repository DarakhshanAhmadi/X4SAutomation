import csv


class CSVWriter:

    def __init__(self, file_location, data_dict):
        self.file_location = file_location
        self.data_dict = data_dict
        self.headers = data_dict[0].keys()

    def write_file(self):
        with open(self.file_location, mode='w', newline='') as csv_file:
            dict_writer = csv.DictWriter(csv_file, fieldnames=self.headers)
            dict_writer.writeheader()
            dict_writer.writerows(self.data_dict)
