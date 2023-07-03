from CommonUtilities import parse_json_common


class parse_json_feed():

    def read_data_from_cbrequest(data):
        cust_attribute_value = []
        list_of_items = ['subscriptionname', 'subscriptionstartdate', 'subscriptionenddate', 'subscriptionid',
                         'subscriptionperiod',
                         'subscriptionperiodunit', 'billingperiod', 'billingperiodunit', 'status']
        output_data = parse_json_feed.data_maker(list_of_items , data)
        output_data['customeracopeuid'] = data['customerdetails']['customeracopeuid']
        for item in data['serviceparameters']:
            if item['name'] == "vendor_subscription_id":
                value = item['value']
        output_data.update({'vendorsubscriptionid': value})
        for item in data['customattributes']:
            if item['name'] == "bill_to" or item['name'] == "payment_method":
                cust_attribute_value.append(item['value'])
        output_data.update({'bill_to': cust_attribute_value[0]})
        output_data.update({'payment_method': cust_attribute_value[1]})
        output_data.update({'testCaseID': 'T1'})
        return output_data

    def data_maker(data_list, data):
        return_dict = {}
        for item in data_list:
            return_dict[item] = data[item]
        return return_dict

    def get_data_per_feedjson(json_file):
        data_dic = parse_json_common.common_json_ops.read_json_file(json_file)
        data_details = parse_json_feed.read_data_from_cbrequest(data_dic["cbrequest"])
        return data_details


