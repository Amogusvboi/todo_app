# import glob
#
# myfiles = glob.glob('Practical\Txt files\*.txt')
#
# print(myfiles)
#
# for itempath in myfiles:
#     with open(itempath, 'r') as file:
#         print(file.read())

# import csv
#
# with open('Practical\Txt files\weather.csv', 'r') as file:
#     data = list(csv.reader(file))
#
# city = input('Enter a city from a list: ')
#
# for row in data[1:]:
#     if row[0] == city:
#         print('The temperature is:', row[1])

# import shutil
#
# shutil.make_archive('output', 'zip', 'Practical\Txt files')

import webbrowser

user_term = input('Enter a search term: ').replace(' ', '+')

webbrowser.open('https://www.google.com/search?q=' + user_term)