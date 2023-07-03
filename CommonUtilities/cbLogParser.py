from ParseFeed import parse_json_feed
from ParseItemDetailFeed import parse_json_item_detail
import ParseBitDetail as rs
import os
from CommonUtilities import CSVWriter

json_loc = os.listdir(r'..\Input\bits')
parse_file_location = r'..\Input\feed\feed.json'


def main():
    final_data_list = []
    item_data_list = parse_json_item_detail.get_item_data_json(parse_file_location)
    writer = CSVWriter.CSVWriter('../Output/COMMERCE_Output_subs_mpn_details.csv', item_data_list)
    writer.write_file()
    data_list = parse_json_feed.get_data_per_feedjson(parse_file_location)
    final_data_list.append(data_list)
    writer = CSVWriter.CSVWriter('../Output/COMMERCE_Output_subs_general_details.csv', final_data_list)
    writer.write_file()
    print()
    all_bits_list = []
    for file in json_loc :
        file_location = r"../Input/bits/" + file
        bit_list_per_file = rs.parse_bit.get_data_per_json(file_location)
        for bit in bit_list_per_file:
            all_bits_list.append(bit)
    writer = CSVWriter.CSVWriter('../Output/COMMERCE_Output_bits_details.csv', all_bits_list)
    writer.write_file()

if __name__ == '__main__':
    main()




