import argparse
from hashlib import sha256
import os 
import csv 
import json

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=True)
args = parser.parse_args()
filename = args.filename
data = {}
def convert_csv_json(filename):
    with open(filename,'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file) 
        for rows in csv_reader:
            data['format'] = 'CHIP-007'
            data['Serial Number'] = rows['Serial Number']
            data['Filename'] = rows["Filename"]
            data['UUID'] = rows['UUID']
            with open('nft'+rows['Filename']+'.json', 'w') as json_file:
                json_file.write(json.dumps(data, indent=4))
    hash_json()
    
def hash_json():
    json_file = [json_file for json_file in os.listdir(os.path.abspath(os.getcwd())) if json_file.endswith('.json') ]
    BUFF_SIZE = 65536
    list_of_hash = []
    
    for file in json_file:
        with open(file, 'rb',) as f:
            file_hash = sha256()
            fb = f.read(BUFF_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb =f.read(BUFF_SIZE)
                print(file_hash.hexdigest())
            list_of_hash.append(file_hash.hexdigest())
    print([list_of_hash])
    # A 2d-array is needed before a list can be properly converted for csv. We are convertin our 1d-array
    new_hash_list = []
    for x in list_of_hash:
        sub = x.split(', ')
        new_hash_list.append(sub)
    
    with open('filename.output.csv', 'w') as hashed_csv:
        csv_writer = csv.writer(hashed_csv)
        csv_writer.writerows(new_hash_list)
convert_csv_json(filename)    


