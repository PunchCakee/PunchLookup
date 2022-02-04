import random
import sys
import time
import asyncio
import httpx
from io import TextIOWrapper
from colorama import Fore
inp = open('ips.txt', 'r')
f = open("output.txt" , "w")
async def main():
    for line in inp:
        async with httpx.AsyncClient(follow_redirects=False, timeout=1000) as client:
            url = "http://ip-api.com/json/" + str(line.rstrip())
            r = await client.get(url)
            if r.status_code == 200:
                data = r.json()
                country = data.get("country", "Not Found")
                city = data.get("city", "Not Found")
                isp = data.get("isp", "Not Found")
                lat = data.get("lat", "Not Found")
                long = data.get("lon", "Not Found")
                ip = data.get("query", "Not Found")
                print(Fore.GREEN + "REQUEST SUCCEEDED!")
                f.write("\nip: " + str(ip))
                f.write("\ncountry : " + country)
                f.write("\ncity : " + city)
                f.write("\nisp : " + isp)
                f.write("\nlatitude : " + str(lat))
                f.write("\nlongitude : " + str(long))
                f.write("\n")
            else:
                print(Fore.RED + "REQUEST FAILED")
            if r.status_code == 429:
                print(Fore.YELLOW + "Request limit exceeded, Sleeping for 1 min")
                await asyncio.sleep(60)
asyncio.run(main())
f.close()
inp.close()
