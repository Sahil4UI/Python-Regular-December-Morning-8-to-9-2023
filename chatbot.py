#chatbot
import webbrowser
from datetime import datetime
helloIntent = ["hi","hello","hey","hie","how are you?"]
dateIntent = ["date","date please","whats the date?"]
timeIntent = ["time","time please","whats the time?"]
msg = input("Enter Msg :").lower()
if msg in helloIntent:
    print("Hello...")
elif msg.startswith("open"):
    webbrowser.open("https://www."+msg.split()[-1]+".com")
elif msg in dateIntent:
    dt = datetime.now()
    print(dt.strftime("%d/%m/%Y,%a"))
elif msg in timeIntent:
    dt = datetime.now()
    print(dt.strftime("%H:%M:%S,%p"))
