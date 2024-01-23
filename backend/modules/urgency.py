import requests
from bs4 import BeautifulSoup

def urgency_check(url):
    urgency_result = {'status': '', 'text_inside_div': ''}

    # Send an HTTP GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for the presence of a div with class "_2JC05C"
        urgency_div = soup.find('div', class_='_2JC05C')

        if urgency_div:
            urgency_result['status'] = "Urgency found - Potential Dark Pattern Found"
            urgency_result['text_inside_div'] = urgency_div.get_text(strip=True)
        else:
            urgency_result['status'] = "Urgency not found - No potential dark pattern detected"

    else:
        urgency_result['status'] = f"Error: Unable to fetch the URL. Status Code: {response.status_code}"

    return urgency_result

    