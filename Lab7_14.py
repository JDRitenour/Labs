title_input = input('Enter a title for the data:\n')
print('You entered:', title_input, end='\n\n')

column1_input = input('Enter the column 1 header:\n')
print('You entered:', column1_input, end='\n\n')

column2_input = input('Enter the column 2 header:\n')
print('You entered:', column2_input, end='\n\n')

data_dictionary = {}
author_list = []

while True:
    data_point = input('Enter a data point (-1 to stop input):\n')
    if data_point == '-1':
        break
    else:
        data_list = [x.strip() for x in data_point.split(',')]
        if len(data_list) == 1:
            print('Error: No comma in string.')
        if len(data_list) > 2:
            print('Error: Too many commas in input.')
        if len(data_list) == 2:
            data_string = data_list[0]
            data_integer = data_list[1]
            if data_integer.isnumeric():
                print('Data string:', data_string)
                print('Data integer:', data_integer)
                author_list.append(data_string)
                data_dictionary[data_string] = int(data_integer)
            else:
                print('Error: Comma not followed by an integer.')

print('{:>33}'.format(title_input))
print('{:<20}|{:>23}'.format(column1_input, column2_input))
print('-' * 44)
for i in author_list:
    print('{:<20}|{:>23}\n'.format(i, data_dictionary[i]))

for i in author_list:
    print('{:>20} {}'.format(i, '*' * data_dictionary[i]))
