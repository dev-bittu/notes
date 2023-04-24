from csv import reader
from os import system

qa = ["a", "yyi", "cyf"]

response_file = "form.csv"

def get_info() -> dict:
    """
    extract information from responsed csv file

    return:
        {
            email: [answers in order maintained by qa]
        }
    """
    info = {}

    with open(response_file, 'r') as file:
        data = reader(file)
        first_row = True
        for row in data:
            info[row[1]] = row[2:]
    return info

def main():
    """
    get marks of users
    """
    info = get_info()

    questions_order = []

    for i in info["Username"]:
        questions_order.append(
            i.partition(".")[0]
        )

    marks = {}

    for user in info:
        marks[user] = 0
        
        index = 0

        for ans in info[user]:
            if qa[index].strip().lower() == ans.strip().lower():
                marks[user] += 1
            index += 1

    return marks

def get_question_order():
    """
    get questions order
    """
    info = get_info()
    return info["Username"]

def set_answers(file):
    """
    set answers from a txt file.

    """
    with open(file) as f:
        out = f.readlines()

    for i in out:
        qa.append(i.replace("\n", ""))
    
if __name__ == "__main__":
    marks = main()
