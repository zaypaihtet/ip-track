RED = '\033[91m' #RED
OK = '\033[92m' #GREEN
RESTART = '\033[0m' #RESET COLOR
YELLOW = '\033[93m' #YELLOW
from urllib.request import urlopen as open
import json
import pyttsx3
import re 
import webbrowser
from pyfiglet import Figlet
engine = pyttsx3.init()
engine.say("Welcome Baby")
print(Figlet().renderText('IP-Tracker'))
print(RED + "                                       by Red_Z" + YELLOW )
engine = pyttsx3.init()

engine.say("I'm RED_Z")
engine.say("Don't copy my script")
engine.say("Respet the coader")
engine.runAndWait()





def goto2():
    global ip
    ip = input(YELLOW + "Enter ip address  : " + RESTART)
    exit() if ip.lower() == 'exit' else check(ip)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
    
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

       
def check(Ip):
    if(Ip.startswith('192')):
        print( RED + "I think its a private ip address " + RESTART)
        speak('I think its a private ip address,Bro')
        goto2()

    elif(re.search(regex, Ip)): 
        print(OK + "Valid Ip address found" + RESTART)
        speak("locating,Bro")
        goto1()
     
    else:
        print(RED + "Invalid ip address" + RESTART)
        speak("Wrong ip address,Bro")
        goto2()

def goto1():
   
    url = "http://ip-api.com/json/"
    response = open(url + ip)
    data = response.read()
    values = json.loads(data)
    status = values['status']
    success = "success"
    lat = str(values['lat'])
    lon = str(values['lon'])
    a = lat + ","
    b = lon + "/" + "data=!3m1!1e3?hl=en"
    location = a + b


    maps = "https://www.google.com/maps/search/"
    webbrowser.open(maps + location)
    

    print(RED + " IP: " + values['query'] + RESTART)
    print(YELLOW + " Status: " + values['status'] + RESTART)
    print(RED + " city: " + values['city'] + RESTART)
    print(YELLOW + " ISP: " + values['isp'] + RESTART)
    print(RED + " latitude: " + lat)
    print(YELLOW + " longitude: " + lon)
    print(RED + " country: " + values['country'] + RESTART)
    print(YELLOW + " region: " + values['regionName'] + RESTART)
    print(RED + " city: " + values['city'] + RESTART)
    print(YELLOW + " zip: " + values['zip'] + RESTART)
    print(RED + " AS: " + values['as'] + RESTART)
    if status == success:
        speak("sucessfully located")
    else:
        speak("cannot find the location,Bro")    
    
    goto2()           
        
goto2()
