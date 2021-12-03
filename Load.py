import csv
import json


class Load:
    def toCSV(self, dataset: list, file_path: str):
        with open(file_path, 'w') as csv_file:  # open file in write mode
            field_names = []
            for i in dataset[0].keys():
                field_names.append(i)
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=field_names)
            writer.writeheader()  # writing the header row
            for row in dataset:
                writer.writerow(row)
        csv_file.close()

    def toJSON(self, dataset: list, file_path: str):
        data = []
        for row in dataset:
            data.append(row)
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()



