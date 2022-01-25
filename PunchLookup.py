import random
import requests
import sys
inp = input("what ip do you want to lookup?")
response = requests.get("http://ip-api.com/json/"+ inp).json()
f = open("output.txt" , "w")
print("country = " + response['country'] , file=f)
print("city = " + response['city'] ,file=f)
print("the isp of this ip is = " + response['isp'] ,file=f)
print("latitude = "+ str(response['lat']) ,file=f)
print("longtuide = " + str(response['lon']) ,file=f)
print("details save in output.txt file, Enjoy :)")
