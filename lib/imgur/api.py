import requests

def get_subreddit(url, clientId):
    try:
        response = requests.get(
            url=f'{url}',
            headers={
                'Authorization': f'Client-ID {clientId}',
            }
        )
        print(f'Status: {response.status_code}')
        print(f'Body: {response.content}')
    except requests.exceptions.RequestException:
        print('Failed')

# need to see what data we're looking for. will consolidate these GET reqs soon.
def get_post_data(url, clientId):
    try:
        response = requests.get(
            url=f'{url}',
            headers={
                'Authorization': f'Client-ID {clientId}',
            }
        )
        print(f'Status: {response.status_code}')
        print(str(f'Data: {response.content[1]}'))
    except requests.exceptions.RequestException:
        print('Failed')
