import os
import re
import emoji

print('Enter path (press RETURN to set it as ', os.getcwd(), ' ): ')
fpath = input()
print(fpath)
if fpath == '':
    destination = os.getcwd() 
else:
    destination = fpath
    os.chdir(destination) 
print('==== Files you can rename ====')

for i in os.listdir():
    # print(len(re.findall('_\w{3}\d{4}_',i)))
    # x = re.search(r'Reference Material\b', i)
    if len(re.findall('_\w{3}\d{4}_',i)):
        print(i) #,'--> ',(x.span()[1])+1)

sub_code = input('\nSubject code to rename: ')

# TODO: add exceptions for file names lesser than 15 characters
fname = list()
new_fname = list()
for i in os.listdir():
    if i[15:22] == sub_code:
        x = re.search(r'Reference Material\b', i)
        start_name_index = x.span()[1]+1
        fname.append(i) 
        new_fname.append(sub_code+' - '+i[69:])

for i in range(len(new_fname)):
    print(fname[i], ' --> ', new_fname[i])

confirmation = input("\nDo you wish to Rename the files [Yes/No] [Y/N] :: ")
if confirmation in ['Yes','Y','y','yes']:
    print(emoji.emojize('Renaming :pencil: ...',use_aliases=True))
    for i in range(len(new_fname)):
        os.rename(fname[i], new_fname[i])

print(emoji.emojize(':white_check_mark: Done',use_aliases=True))
