"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
import csv
source = input()
with open(source, 'r') as file:
    encoder = csv.reader(file, delimiter = ',')
    result = dict()
    for x in encoder:
        for y in x:
            if y in result:
                result[y] = result[y] + 1
            else:
                result[y] = 1
    for w in list(result.keys()):
        print("{} {}".format(w, result[w]))