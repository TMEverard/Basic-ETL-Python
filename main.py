from Transform import Transform
from Extract import Extract
from Load import Load

e = Extract()
dataset = e.fromCSV(file_path="train.csv")

t = Transform()
removes = t.remove_attributes(dataset, ["Fare","Embarked", "Ticket", "SibSp"])

t.rename_attribute(dataset, "PassengerId", "PassId")

l = Load()
l.toCSV(file_path="train_changed.csv", dataset=removes)

new_data = e.fromCSV(file_path='train_changed.csv', delimiter=',')

new_head = t.head(new_data, 10)
for row in new_head:
    print(row)

