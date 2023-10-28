from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        if result.scheme and result.netloc:
            return True
        else:
            return False
    except ValueError:
        return False
    
url = "https://www.google.com"
if is_valid_url(url):
    print("Valid URL.")
else:
    print("Invalid URL.")