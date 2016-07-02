'''
Initial thought process
Okay so this program's purpose is to help a sick workaholics
remind themselves that they must take a break.
Step 1. get current time
Step 2. From Current time it goes off every X amount of time e.g 30 mins
Step 3. Get the time current time + x amount of time
Step 4. As current time updates and keep checking with current time + x until its equivalent.
Step 5. When it is finally equivalent, play a youtube link
'''
import webbrowser
import time

i = 0
print("this is a program that helps you manage your break")
print("This program executed today on: " + time.ctime())
while i < 3:
    time.sleep(60*30)#30 minute break sttarts
    webbrowser.open("https://www.youtube.com/watch?v=CVEuPmVAb8o")
    i = i + 1;