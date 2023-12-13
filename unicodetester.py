import requests
import unicodedata

# User input for base URL
base_url = input("Enter the base URL: ")

# Ensure the URL ends with a slash if not present
if not base_url.endswith('/'):
    base_url += '/'

# Characters in NFC and NFD forms
char_nfc = unicodedata.normalize('NFC', 'é')
char_nfd = unicodedata.normalize('NFD', 'é')

# Constructing URLs
url_nfc = base_url + char_nfc
url_nfd = base_url + char_nfd

# Sending requests
response_nfc = requests.get(url_nfc)
response_nfd = requests.get(url_nfd)

# Comparing responses
if response_nfc.text == response_nfd.text:
    print("The server handles Unicode normalization correctly.")
else:
    print("The server does not handle Unicode normalization correctly.")
