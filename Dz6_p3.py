import csv
from itertools import zip_longest
import json

data_dict = {}
with open('user.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        lines_users = sum(1 for lines in users)
        lines_hobby = sum (1 for lines in hobby)
        if lines_users < lines_hobby:
            exit(1)

            users.seek(0)
            hobby.seek(0)
            for lines_users, lines_hobby in zip_longest(users, hobby):
                data_dict[lines_users.strip()] = lines_hobby.strip() if lines_hobby is not None else lines_hobby

with open('UserHobby.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False)
print(data_dict)

