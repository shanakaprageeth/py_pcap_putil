__author__="shanaka prageeth"
__description__="This script captures urls given in csv file and save the html responses in files"
#python3
import urllib.request

URL_LIST_FILE = "url_list.csv"
# collect urls from csv file
def caputure_urls(csv_file_name, condition, condition_idx, url_idx):
	urls_list = []
	url_list_file = open(csv_file_name, "r")
	url_lines = url_list_file.readlines()
	for url_line in url_lines:
		url_data = url_line.replace(" ","").replace("\n","").split(',')
		if(len(url_data)> condition_idx and len(url_data)> url_idx):
			if(condition in url_data[condition_idx] ):
				urls_list.append(url_data[url_idx])
			else:
				pass
		else:
			pass
	return urls_list


# download urls
def access_urls(urls_to_fetch):
	for url_to_fetch in urls_to_fetch: 
		try:
			with urllib.request.urlopen(url_to_fetch) as response:
				html = response.read()
				f = open("{}.html".format(url_to_fetch),"w")
				f.write(html)
				f.close()
				print("grabbed url ",url_to_fetch)
		except:
			print("error: failed to fetch url : ",url_to_fetch)

#urls_to_fetch = caputure_urls(csv_file_name, condition, condition_idx, url_idx)
urls_to_fetch = caputure_urls(URL_LIST_FILE, "normal", 1, 0)
access_urls(urls_to_fetch)


