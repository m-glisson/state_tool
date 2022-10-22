import csv 

class DataSource: 
    def __init__(self) -> None:
        self.data = self.read_data('data.csv')
        self.current_index = 1
        

    def read_data(self, csv_file):
        with open(csv_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            data_array = []
            for row in csv_reader:
                data_array.append(row)

        return data_array

    def get_value(self):
        self.current_index += 1
        if self.current_index >= len(self.data): 
            self.current_index = 0

        return self.data[self.current_index]

data_source = DataSource()
print('I am here')