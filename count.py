def countdown(n):
    'count from n down to 1'
    if n <= 0:
        print('Blast off!')
    else:
        print(n)
        countdown(n-1)

def cheers(n):
    if n <= 0:
        print('Hooray!')
    else:
        print('Hip',end=" ")
        cheers(n-1)


def nonRecursive(n):

    while n > 0:
        print(n)

#countdown(3)
#cheers(3)

def pattern(n):
    if n == 0:
        print(0, end=' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)


#pattern(2)
import os
def scan(pathname, file_extension):
    if os.path.isfile(pathname): # base case, scan pathname
        # infile = open(pathname)
        # content = infile.read()
        # infile.close()
        if file_extension in pathname:
            # check whether virus signature appears in content
            #if content.find(file_extension[virus]) >= 0:
                print('{}, found a {}'.format(pathname, file_extension).upper())
        else:

            print('{}, found a file'.format(pathname))
        return
    
    # pathname is a folder so recursively scan every item in it
    for item in os.listdir(pathname):
        # create pathname for item relative to current working directory
        # fullpath = pathname + '/' + item      # Mac only
        # fullpath = pathname + '\' + item      # Windows only
        fullpath = os.path.join(pathname, item) # any OS
        
        scan(fullpath, file_extension)

scan('C:\\Users\\bodonne3\\Documents\\csc242_week7', '.jpg')