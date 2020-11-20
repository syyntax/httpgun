from os.path import abspath, join, dirname
import requests
from random import randint
from json import loads
from lib.httpgunlib import Request, UserAgent

# Path for this script
scr_path = dirname(abspath(__file__))


def get_http(url_string, http_headers):
    return requests.get(url_string, headers=http_headers)


def get_rand42():
    num = ''
    for i in range(0, 41):
        rng = "0123456789abcdef"
        num += rng[randint(0, len(rng) - 1)]

    return num


def populate_user_agents(user_agents_list):
    user_agent_lst = list()
    for obj in user_agents_list:
        user_agent_lst.append(obj)

    return user_agent_lst


# r = get_http("http://nyu.edu", {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
#                                "like Gecko) Chrome/87.0.4280.66 Safari/537.36", "Connection": "keep-alive",
#                                "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Accept":
#                                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
#                                "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding":
#                                "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Cookie":
#                                f"BIGipServer~WSQ-EDU-MED~www-http={get_rand42()}",
#                                "If-None-Match": "781285-15230-5b48b9dd4ba52"})

user_agents = loads(open(abspath(join(scr_path, 'data/user_agents.json')), 'r').read())['headers']['User-agent']['Chr'
                                                                                                                 'ome']

a = populate_user_agents(user_agents)
