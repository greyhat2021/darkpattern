import requests
from bs4 import BeautifulSoup
import time
import json

def check_timer_changes_within_duration(url, duration=60):
    def get_timer_info_flipkart(url):
        # Fetch webpage
        response = requests.get(url)

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract timer information, modify the class accordingly
        timer_info = soup.find('div', {'class': '_1dXn7l'})

        return timer_info.text.strip() if timer_info else None

    # Check if the timer class is present
    initial_timer_info = get_timer_info_flipkart(url)

    result_json = {"initial_time": initial_timer_info, "updated_time": None, "result": None}

    if initial_timer_info is not None:
        print("Analyzing Offer Timer...")
        print(f"Initial Timer Info: {initial_timer_info}")

        # Check for timer changes every second for the specified duration
        for _ in range(duration):
            time.sleep(1)
            updated_timer_info = get_timer_info_flipkart(url)

            if updated_timer_info != initial_timer_info:
                print(f"Updated Timer Info: {updated_timer_info}")
                print("Fake Timers used. Potential dark pattern Found.")
                result_json["updated_time"] = updated_timer_info
                result_json["result"] = "Fake Timers used. Potential dark pattern Found."
                return json.dumps(result_json)

        print("No timer changes detected within the duration. Timer is likely real.")
        result_json["result"] = "No timer changes detected within the duration. Timer is likely real."
    else:
        print("No Urgency Timer Found")
        result_json["result"] = "No Urgency Timer Found"

    return json.dumps(result_json)
