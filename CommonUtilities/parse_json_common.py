import json


class common_json_ops():

    def read_json_file(self, parse_file):
        try:
            with open(parse_file, "r+") as jsonFile:
                data = json.load(jsonFile)
                data_dic = dict(data)
                return data_dic
        except Exception as e:
            raise e

    def update_json_object(self, data, section, sub_section, sub_section_variable, variable_data):
        try:
            data[section][sub_section][sub_section_variable] = variable_data
            return data
        except Exception as e:
            raise e

    def read_json_data(self, json_data, section, sub_section, sub_section_variable):
        try:
            data = json_data[section][sub_section][sub_section_variable]
            return data
        except Exception as e:
            raise e

    def read_json_data1(self, json_data, section):
        try:
            data = json_data[section]
            return data
        except Exception as e:
            raise e
