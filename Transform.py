from Extract import Extract  # import the external extract class


class Transform:
    def head(self, dataset: list, n: int): # return the top N records from the dataset
        return dataset[:n]

    def tail(self, dataset: list, n: int):  # return the last N records from the dataset
        length = len(dataset)
        return dataset[(length - n):]

    def rename_attribute(self, dataset: list, rename_from: str, rename_to: str):  # rename a column in the dataset
        for row in dataset:
            row[rename_to] = row.pop(rename_from)
        return dataset

    def remove_attribute(self, dataset: list, remove: str):  # remove a column from the dataset
        for row in dataset:
            row.pop(remove)
        return dataset

    def rename_attributes(self, dataset: list, rename_from: list, rename_to: list):  # rename a list of columns in the dataset
        for i in range(len(rename_from)):
            for row in dataset:
                row[rename_to[i]] = row.pop(rename_from[i])
        return dataset

    def remove_attributes(self, dataset: list, remove: list):  # remove a list of columns in the dataset
        for removal_item in remove:
            for row in dataset:
                row.pop(removal_item)
        return dataset
