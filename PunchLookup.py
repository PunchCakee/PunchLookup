import random
import requests
import sys
import time 
inp = input("what ip do you want to lookup? ")
response = requests.get("http://ip-api.com/json/"+ inp).json()
f = open("output.txt" , "w")
f.write("country = " + response['country'])
f.write("\ncity = " + response['city'])
f.write("\nthe isp of this ip is = " + response['isp'])
f.write("\nlatitude = "+ str(response['lat']) )
f.write("\nlongtuide = " + str(response['lon']) )
print("output has been saved in output.txt")
f.close()
time.sleep(5)
