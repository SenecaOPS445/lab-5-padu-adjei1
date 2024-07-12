#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    list_of_lines = read_data.split('\n')
    if list_of_lines[-1] == '':
        list_of_lines = list_of_lines[:-1]
    return list_of_lines

if __name__ == '__main__':
    file_name = '/home/padu-adjei1/ops445/lab5/lab-5-padu-adjei1/data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
