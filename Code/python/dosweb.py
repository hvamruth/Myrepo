import urllib.request

def fetch_webpage(url):
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')
        return html_content
    except Exception as e:
        return f"Error: {e}"

def main():
    print("DOS CLI Web Browser")
    print("Enter 'exit' to quit.")
    
    while True:
        url = input("Enter a URL: ").strip()
        
        if url.lower() == 'exit':
            break
        
        html_content = fetch_webpage(url)
        print("\nHTML Content:\n")
        print(html_content)

if __name__ == "__main__":
    main()
