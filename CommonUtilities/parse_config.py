import os
import pathlib

from CommonUtilities.EncryptDecrypt import EncrptDecrpt
from CommonUtilities.parse_json_common import common_json_ops


class ParseConfigFile():
    json_ops = common_json_ops()

    def get_data_from_config_json(self, section_of_config, section_variable, config_file_name=None):
        data_details = None
        try:

            repo_path = os.path.dirname(os.path.abspath(__file__))
            root_path = pathlib.Path(repo_path)
            root_path = root_path.parent
            root_path = str(root_path).replace('WindowsPath(', '').replace(')', '')
            if config_file_name is None:
                path = root_path + "\\Configuration\\config.json"
            else:
                path = root_path + "\\Configuration\\" + config_file_name
            config_dic = self.json_ops.read_json_file(path)

            data_details = self.read_config_details(config_dic, section_of_config, section_variable)
        except Exception as e:
            # self.logger.error("Exception occurred while reading config file for section variable %s ", section_variable)
            raise e

        return data_details

    def read_config_details(self, data, section, section_variable):
        output_data = {}
        if section_variable not in data[section]:
            section = "default"
        output_data[section_variable] = data[section][section_variable]
        output_value = output_data[section_variable]
        if output_value is not None and output_value.strip() != "" and "enc_" in section_variable:
            obj_decrypt = EncrptDecrpt()
            try:
                output_value = obj_decrypt.decrypt(output_value)
            except:
                output_value = None
                print("Exception occur during decrypt")

        # print(output_value)
        return output_value

# parse_config_file.get_data_from_config_json("browserDriverPaths", "firefoxExecutablePath")
