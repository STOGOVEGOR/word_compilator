import csv
csv_filename = 'nouns.csv'

cut_iterable = 4
word_len_min = 6
word_len_max = 8

with open(csv_filename,'r', encoding='utf-8') as data:
    new_dict = [line[0] for line in csv.reader(data, delimiter='\t')]
    for x in range(len(new_dict)):
        if word_len_min < len(new_dict[x]) <= word_len_max:
            word_end = new_dict[x][-cut_iterable:]
            for i in new_dict:
                if len(i) > cut_iterable + 3:
                    word_begin = i[:cut_iterable]
                    if word_begin == word_end:
                        print(new_dict[x][:-cut_iterable] + i + '  --->  '
                              + new_dict[x] + ' + ' + i)
