__description__ = 'This function will search all the pcap files in the folder and filter the pcap files for a given protocol using tshark'
import os
import sys
import glob

TCP_PORT = "80"

def get_file_lines(src_file):
    with open(src_file) as file:
        content = file.readlines()
    return content

def get_files_in_folder(extension, avoid = "http"):
    file_list = []
    file_extension = "*."+extension
    for file_name in glob.glob(file_extension):
        if(not (avoid in file_name)):
            file_list.append(file_name)
    return file_list


def list_files(os_dir = '.',extension= '', avoid = "http"):
    file_list = []
    for root, dirs, files in os.walk(os_dir):
        for file_name in files:
            if(not (avoid in file_name) and extension in file_name):
                file_list.append(os.path.join(root,file_name))
    return file_list

file_list = list_files('.','.pcap','http')
for file_name in file_list:
    new_file_name = file_name.split("/")[-1]
    folder = file_name.split(new_file_name)[0]
    new_file_name = folder + 'http_'+new_file_name
    print ('filtering file ',file_name, ' to ', new_file_name)
    command = 'tshark -nr {} -Y "tcp.port == {}" -w  {}'format(file_name, TCP_PORT,new_file_name)
    os.system(command)
