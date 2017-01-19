import time
import webbrowser

count = 0
total_breaks = 3
break_after = 2*60*60 

print("Started on " + time.ctime())
while (count < total_breaks):
    time.sleep(break_after)
    webbrowser.open("https://www.youtube.com/watch?v=VaJjPRwExO8")
    count = count+1
