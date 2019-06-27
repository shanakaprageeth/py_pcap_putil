
# Python scripts for simple net app measurnments

## Description
This project include python scripts used for 
-pcap file filtration
-URL fetching
-record CPU process data


### Prerequisites

python3 , libpcap, tshark

## Running the tests

pcap file filtration
This script will filter all the pcap files in the directory for a single protocol(ex:tcp 80). Script will create new pcap files that can be used to benchmark applications on specific protocol. 
``` 
python3 pcap_protocol_filter.py
``` 

URL fetching
Download or define url list as a csv file under "url_list.csv". (ex: http://github.com, development,\n http://youtube.com, entertainment)
This python script will capture http responses for the urls on list to and save them in a file. You could use this script with tcpdump to generate a pcap file with http responses of the websites in url list.
``` 
python3 fetch_pages.py
``` 

Record CPU process data
This script will periodically print process information as a list for a given pid.
``` 
python3 record_processs_data.py [pid]
``` 

## License
[MIT](https://choosealicense.com/licenses/mit/)
