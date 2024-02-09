# import shutil 

# shutil.copyfile('first.csv','second.csv')

def transfer():
    with open('first.csv','r', encoding='utf-8') as firstfile, open('second.csv','a', encoding='utf-8') as secondfile: 
        for line in firstfile: 
            secondfile.write(line)

transfer()