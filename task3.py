import json
import sys

var1 = sys.argv[1]
var2 = sys.argv[2]
tests = open(var1, 'r')
text_test = json.load(tests)
values=open(var2, 'r')
text_values = json.load(values)
report = text_test


def rec(lst, num, val):
    for k in lst:
        if 'value' in k and k['id'] == num:
            k['value'] = val
        for n in k:
            if 'values' in k:
                ret = rec(k['values'], num, val)
    return lst


for item in text_values['values']:
    rec(report['tests'], item['id'], item['value'])

json.dumps(report, indent=1)

with open('report.json', 'w', encoding='utf-8') as r:
    json.dump(report, r, indent=1)
































