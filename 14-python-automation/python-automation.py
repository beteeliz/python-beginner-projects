# Install library - schedule
# pip install schedule

# Install library - requests
# pip install requests

from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Good morning!',
        # The key is free to be used once a day
        'key': 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('08:00').do(send_message)

schedule.every(10).seconds.at('08:00').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)