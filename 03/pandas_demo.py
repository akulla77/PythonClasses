from pandas import DataFrame, read_excel

if __name__ == '__main__':
    data_frame: DataFrame = read_excel('input.xlsx', sheet_name='Sheet1')
    students = data_frame['Unnamed: 1'][2:20]
    print(data_frame.columns)
