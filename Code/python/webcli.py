import requests
from bs4 import BeautifulSoup

# Function to fetch and display web page content
def browse_web(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Print the title of the web page
        title_tag = soup.find('title')
        if title_tag:
            print(f"Title: {title_tag.text.strip()}\n")

        # Print the main content of the web page (text only)
        for paragraph in soup.find_all('p'):
            print(paragraph.text.strip())

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Main program loop
while True:
    user_input = input("Enter a URL (or 'q' to quit): ").strip()
    if user_input.lower() == 'q':
        break
    browse_web(user_input)
