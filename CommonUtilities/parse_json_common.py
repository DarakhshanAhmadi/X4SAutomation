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
