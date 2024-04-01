#!/usr/bin/python3
"""script for testing status of web pages
"""
if __name__ == "__main__":
    import requests
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    content = response.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_str)
