def read_file(file_name):
    file_dic = {}
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
        for index in range(0, len(lines) - 1, 2):
            if lines[index].strip() == '':
                continue
            cnt = int(lines[index].strip())
            name = lines[index + 1].strip()
            if cnt in file_dic.keys():
                name_list = file_dic.get(cnt)
                name_list.append(name)
                name_list.sort()
            else:
                file_dic[cnt] = [name]
            print(cnt, name)
    return file_dic


def output_keys(file_dic, file_name):
    with open(file_name, 'w') as outfile:
        for key in sorted(file_dic.keys()):
            outfile.write('{}:{}\n'.format(key, '; '.join(file_dic.get(key))))
            print('{}: {}\n'.format(key, ';'.join(file_dic.get(key))))


def output_titles(file_dic, file_name):
    titles = []
    for title in file_dic.values():
        titles.extend(title)
    with open(file_name, 'w') as out_file:
        for title in sorted(titles):
            out_file.write('{}\n'.format(title))
            print(title)


def main():
    file_name = '/Users/wayne/PycharmProjects/pythonProject1/venv/file1'
    dic = read_file(file_name)
    if dic is None:
        print('Error: Invalid file name provided.')
        return
    print(dic)
    output_file_name1 = 'output_key.txt'
    output_file_name2 = 'output_titles.txt'

    output_keys(dic, output_file_name1)
    output_titles(dic, output_file_name2)


main()
