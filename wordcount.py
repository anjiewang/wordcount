# put your code here.
import sys

def wordcount():
    input_file = open(sys.argv[1])
    file_dict = {}

    for line in input_file:
        line_split = line.rstrip().split(' ')
        for word in line_split:
            word = word.lower()
            if word == '':
                continue
            elif word[-1] == ',' or word[-1] == '?' or word[-1] == '.':
                word = word[:-1]
            if word in file_dict:
                file_dict[word] += 1
            else:
                file_dict[word] = 1
    

    return file_dict

wordcount()