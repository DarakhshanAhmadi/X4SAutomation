
import parse_json_common

class parse_bit():

    def read_bits(bit):
        list_of_items = ['imSubscriptionId','sku','bitDateFrom','bitDateTo','billingPeriod','bitCurrency',
                         'bitAmount','vendorSubscriptionId','rbBitClass','rbSubProcess','sourceTransactionType',
                         'sourceTransactionId','durationUnit','duration','orderItemsNumber','bitText50','channel',
                         'country','bcn','bitTextLong','imcHub','orderNumber','orderDate','itemNumber',
                         'resourceId','resourceIdText','subscriptionDateFrom','subscriptionDateTo','billingPeriodUnit',
                         'billingPeriod','endCustomerEmail','mpn','resellerTotalContractValue',
                         'rbBitType']
        output_bit = parse_bit.bit_maker(list_of_items , bit)

        return output_bit

    def fetch_filtered_attributes(data_dict , bit):
        extra_items_dict = {}
        if not data_dict['customAttributes']:
            extra_items_dict['bill_to'] = ''
        else:
            extra_items_dict['bill_to'] = data_dict['customAttributes']['bill_to']

        if bit['bitClass'] == 'REV1':
            extra_items_dict['unitPrice'] = bit['unitPrice']
            extra_items_dict['poNumber'] = bit['poNumber']
            extra_items_dict['unitCost'] = ''
        else:
            extra_items_dict['unitPrice'] = ''
            extra_items_dict['poNumber'] = ''
            extra_items_dict['unitCost'] = bit['unitCost']
        return extra_items_dict

    def get_data_per_json(json_file):
        bit_details = {}
        bits_list =[]
        bits_per_json = []
        data_dic = parse_json_common.common_json_ops.read_json_file(json_file)
        bits_list = data_dic["bits"]
        for bit in bits_list:
            bit_details = parse_bit.read_bits(bit)
            filtered_attributes = parse_bit.fetch_filtered_attributes(data_dic, bit)
            bit_details.update(filtered_attributes)
            bit_details.update({'testCaseID': 'T1'})
            bits_per_json.append(bit_details)

        return bits_per_json

    def bit_maker(item_list , bit):
        return_dict = {}
        for item in item_list:
            return_dict[item] = bit[item]
        #print(return_dict)
        return return_dict


