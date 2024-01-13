import json
import os.path
import requests

from send_email import send_email, logging


def get_current_ranking():
    url = 'https://leetcodestats.cyclic.app/KateF20'
    response = requests.get(url)

    if response:
        cur_ranking = response.json()['ranking']
        logging.info(f'cur ranking is: {cur_ranking}')
        stored_ranking = get_previous_ranking()
        logging.info(f'stored ranking is: {stored_ranking}')

        if cur_ranking != stored_ranking:
            store_ranking(cur_ranking)
            send_email(cur_ranking)

    else:
        logging.info(f'Failed to fetch data: {response.status_code}')
        return None


def get_previous_ranking():
    if os.path.exists('stored_ranking.json'):
        with open('stored_ranking.json', 'r') as f:
            data = json.load(f)
            return data.get('previous_ranking')

    return None


def store_ranking(ranking):
    with open('stored_ranking.json', 'w') as f:
        json.dump({"previous_ranking": ranking}, f)


if __name__ == '__main__':
    get_current_ranking()
