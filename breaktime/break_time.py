import time
import webbrowser

total_break = 3
break_count = 0

print("This program started on" + time.ctime())
while(break_count < total_break):
    # time.sleep(2*60*60)
    time.sleep(10)
    webbrowser.open("http://corderogerardo.me")
    break_count=break_count+1