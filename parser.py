import json
import csv

with open('result.json', 'r', encoding='utf8') as fin:
        data=fin.read()

obj = json.loads(data)
ts = obj['data']
ts_obj = json.loads(ts)

with open('transcript.csv', 'w') as fout:
    
    fnames = ['bg', 'ed', 'content']
    writer = csv.DictWriter(fout, fieldnames=fnames)    

    writer.writeheader()

    for item in ts_obj:
        bg = item['bg']
        ed = item['ed']
        content = item['onebest']
        writer.writerow({'bg' : bg, 'ed': ed, 'content': content})
