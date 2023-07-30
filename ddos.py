import aiohttp
import asyncio
import time
from datetime import datetime
from colorama import Fore, Style
import sys
import argparse

# Argümanları tanımlayalım
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, help='URL to be assigned to the "url" variable')

# Argümanları alalım
args = parser.parse_args()

# URL değişkenine atayalım
url = args.url

tests = 0

async def make_requests():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, i + 1) for i in range(1, 101)]
        await asyncio.gather(*tasks)

async def fetch_url(session, url, request_number):
    global tests  # "tests" değişkenini global olarak tanımlıyoruz
    while True:
        async with session.get(url) as response:
            status_code = response.status
            tests += 1
            current_time = datetime.now().strftime("%H:%M:%S")
            if status_code == 200:
                status_color = Fore.GREEN
            else:
                status_color = Fore.RED
            
            print(f"{Fore.GREEN}[{current_time}]{Style.RESET_ALL} Sended: {Fore.GREEN}{tests}{Style.RESET_ALL}; Yanıt kodu: {status_color}{status_code}{Style.RESET_ALL}")


loop = asyncio.get_event_loop()
loop.run_until_complete(make_requests())
