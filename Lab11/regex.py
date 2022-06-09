import re
from zipfile import ZipFile

ctn = 0
regex = re.compile(r'^[1-8][0-9][.]|^[9][0][.]')
with ZipFile('access_log.zip', 'r') as zipfile:
    zipfile.extractall()
with open('result.txt', 'w') as result_file:
    with open('access.log.txt', 'r') as file:
        for line in file:
            if regex.search(line) is not None:
                ctn += 1
                result_file.write(line)
print(ctn)
