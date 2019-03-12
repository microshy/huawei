import re

def data_input_from_file_web(filepath):
    data_list = []
    print("input data from", filepath)
    file = open(filepath)
    data_input = file.read().splitlines()
    r1 = re.compile(r'[(](.*?)[)]', re.S)
    for data in data_input:
        if data.startswith('#'):
            data_input.remove(data)
        data_input.remove('')
    for data in data_input:
        data_list.append(list(map(int,re.findall(r1, data)[0].split(','))))
    file.close()
    return data_list

def data_output_to_file_web(filepath, content):
    data_output = content
    symbol_used_in_output = ', '
    print("output data to", filepath)
    file  = open(filepath, 'w')
    file.write('#(carId,StartTime,RoadId...)\n' + '\n')
    for data in data_output:
        data = '('+(symbol_used_in_output.join((map(str, data)))).replace('None', ' ')+')'
        file.write(data+'\n'+'\n')
    file.close()
    return None

def data_input_from_file(filepath):
    data_list = []
    print("input data from", filepath)
    file = open(filepath)
    data_input = file.read().splitlines()
    for data in data_input:
        if data.startswith('#'):
            data_input.remove(data)
    r1 = re.compile(r'[(](.*?)[)]', re.S)
    for data in data_input:
        data_list.append(list(map(int,re.findall(r1, data)[0].split(','))))
    file.close()
    return data_list

def data_output_to_file(filepath, content):
    data_output = content
    symbol_used_in_output = ', '
    print("output data to", filepath)
    file  = open(filepath, 'w')
    file.write('#(carId,StartTime,RoadId...)\n')
    for data in data_output:
        data = '('+(symbol_used_in_output.join((map(str, data)))).replace('None', ' ')+')'
        file.write(data+'\n')
    file.close()
    return None


