import json
import os
import psutil
import time
from datetime import datetime
from multiprocessing import Process, Queue, Pool


def to_dict(process_id):
    try:
        process = psutil.Process(process_id)
        return process.as_dict()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    processes = psutil.pids()

    start = datetime.now()
    with Pool() as pool:
        results = pool.map(to_dict, processes)
    process_list = [p for p in results if p is not None]
    jsonFile = json.dumps(process_list, indent=4)

    with open(f'jsons/process_list{round((time.time() + datetime.timestamp(start)) / 2)}.json', 'w') as outfile:
        outfile.write(jsonFile)
    print(f"Full processing took {datetime.now() - start}")