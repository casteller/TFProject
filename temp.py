import re
path=r"C:\Users\Administrator\Desktop\IDcard.txt"

with open(path, 'r')as f:
    ids = f.read().splitlines()
    for id in ids:
        print(id.strip())



