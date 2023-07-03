from CommonUtilities import parse_json_common


class parse_json_item_detail():

    def read_from_item_details(data):
        output_data_list = []
        list_of_items = ['itemcode','itemquantity','resellertotalcontractvalue', 'currency','vendortotalcontractvalue']
        for item in data['items']:
            output_data = parse_json_item_detail.data_maker(list_of_items, item)
            output_data['subscriptionid'] = data['subscriptionid']
            output_data.update({'testCaseID': 'T1'})
            output_data_list.append(output_data)
        return output_data_list

    def get_item_data_json(json_file):
        data_dic = parse_json_common.common_json_ops.read_json_file(json_file)
        data_details = parse_json_item_detail.read_from_item_details(data_dic["cbrequest"])
        return data_details

    def data_maker(data_list, data):
        return_dict = {}
        for item in data_list:
            return_dict[item] = data[item]
        return return_dict
