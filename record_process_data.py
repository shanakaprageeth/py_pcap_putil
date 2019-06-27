__author__ = "shanaka prageeth"
__description__ = "Record CPU process statistics in intervals"

import os 
import sys
import time
import argparse
import psutil



parser = argparse.ArgumentParser()
parser.add_argument("pid", help="please enter process number:"+','.join(str(x) for x in psutil.pids()),
                    type=int)
args = parser.parse_args()


def record_data(process_id):

    proc = psutil.Process(process_id)
    cpu_precentage = proc.cpu_percent(interval=1.0)
    cpu_num = proc.cpu_num()
    num_threads = proc.num_threads()
    memory_percent = proc.memory_percent()
    memory_full_info = proc.memory_full_info()

    return [proc, cpu_precentage, cpu_num, num_threads, memory_percent, memory_full_info]


def main():
    while(1):
        time.sleep(1)
        recorded_data = record_data(args.pid)
        print(recorded_data)

if __name__ == "__main__":
    main()