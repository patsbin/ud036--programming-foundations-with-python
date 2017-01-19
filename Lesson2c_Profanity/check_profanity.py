import os
import urllib

def read_text():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movie_quotes.txt")
    quotes = open(file_path)
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()

    if (output == 'true'):
        print("Profanity detected!")
    elif (output == 'false'):
        print("Everything's fine")
    else:
        print("Something went wrong: "+output)

read_text() 
