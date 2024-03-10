
from time import sleep
import os

count=1

def update():
    if 'test1.txt' in os.listdir():
        os.system('rename test1.txt test2.txt')  #Renames file
    elif 'test2.txt' in os.listdir():
        os.system('rename test2.txt test1.txt')  #Renames file
    else:
        listdir=os.listdir()
        for list in listdir:
            if list != '.git':
                os.system('del '+ list)
        os.system('type nul > test1.txt')


def pull(repo,url):
    if os.path.exists(repo)==False:
        os.system('git clone ' + url)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, ''+repo)
    os.chdir(filename)

def push():
    global count
    os.system('cd')
    os.system('git add . && git commit -m "commit ' + str(count) + '"')
    os.system('git push origin main')
    count+=1

def main():
    repo=input("Enter Git Repository name: ")
    url = input("Enter Git Repository URL: ")
    comm=int(input("Enter Number Of Commits To Perform: "))
    pull(repo,url)
    for i in range(0,comm):
        update()
        push()


if __name__=='__main__':
    main()
