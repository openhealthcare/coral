"""
Utility script to convert ICD10 codes to Opal Lookuplist Format
"""
import json
import csv
import sys

def main():
    output = []
    filename = sys.argv[-1]
    with open(filename, 'r') as fh:
        csvfile = csv.reader(fh)
        for row in csvfile:
            output.append({'name': row[1], 'code': row[0], 'system': 'ICD10'})
    print(json.dumps({'condition': output}, indent=2))
    return 0

if __name__ == '__main__':
    main()
