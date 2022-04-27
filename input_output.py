"""The input_output module contains several functions to load files and to format the SACS outputs

    Functions
    ---------------
    load_config_file(file_path:str)->dict
    comparison_output(results:dict)->

"""

def load_config_file(file_path:str)->dict:
    pass

def formated_output(results:dict):
    header = "{0:^10}|{1:^20}|{2:^30}|"
    row = "{algorithm:^10}|{address:^20X}|{lista!s:^30}|"
    print(header.format("Algorithm", "Physical address", "List"))
    for value in results:
        algorithm = value[0]
        sorted_list = value[1]
        print(row.format(algorithm = algorithm, address = id(sorted_list), lista = sorted_list))
