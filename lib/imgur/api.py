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
