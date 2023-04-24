from csv import reader
from os import system

def get_questions(csv_file) -> dict:
    info = {}

    with open(csv_file, 'r') as file:
        data = reader(file)
        first_row = True
        for row in data:
            if first_row:
                first_row = False
                continue
            info[row[2]] = row[3].split("\n")
            info[row[5]] = row[6].split("\n")
    return info

def main():
    #files = ['d1w3', 'd2w3', 'd3w3', 'd4w3']
    files = ["unlimitedform"]
    info = {}
    for file in files:
        info = info | get_questions(f'{file}.csv')

    return info

data = main()
start = 180
start_from = 0

for k, v in data.items():
    if start_from>start:
        start += 1
        continue
    print(f"{start}. {k}")
    system(f'termux-clipboard-set "{start}. {k}"')
    input()
    for i in v:
        print(i)
        system(f'termux-clipboard-set "{i}"')
        input()
    start += 1
