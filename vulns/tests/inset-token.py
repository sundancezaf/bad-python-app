import requests

# Make a GET request to an API endpoint
response = requests.get('https://semgrep.dev/api/v1/deployments')
token = 'asdfasdf2341asdfasdfasd234232323'

headers = f"Authorization: Bearer {token}"

# Check the status code (200 means success)
print(f"Status Code: {response.status_code}")

# Access the response content
# .text for raw content, .json() for JSON data
if response.status_code == 200:
    data = response.json()
    print(data)