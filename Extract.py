import csv


class Extract:
    def fromCSV(self, file_path, delimiter=','):
        try:
            with open(file_path) as f:
                csv_file = csv.reader(f, delimiter=',')
                dataset = list()
                csv_file = csv.DictReader(f, delimiter=delimiter)
                for row in csv_file:
                    dataset.append(row)
            return dataset
        except IOError as e:
            print("File Not Found.")
            print(format(e))