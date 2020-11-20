import requests
from random import randint
from json import loads, dumps


class Request:
    def __init__(self, id, name, user_agent):
        self.id = id
        self.name = name
        self.user_agent = user_agent


class UserAgent:
    def __init__(self, user_agent, OS, enabled, hardware, popularity):
        self.user_agent = user_agent
        self.OS = OS
        self.enabled = enabled
        self.hardware = hardware
        self.popularity = popularity

    def set_user_agent(self, user_agent):
        self.user_agent = user_agent
        return user_agent

    def set_OS(self, OS):
        self.OS = OS
        return OS

    def set_enabled(self, enabled):
        self.enabled = enabled
        return enabled

    def set_hardware(self, hardware):
        self.hardware = hardware
        return hardware

    def set_popularity(self, popularity):
        self.popularity = popularity
        return popularity


def get_http(URL, http_headers):
    return requests.get(URL, headers=http_headers)


def get_rand42():
    num = ''
    for i in range(0, 41):
        rng = "0123456789abcdef"
        num += rng[randint(0, len(rng) - 1)]

    return num


# r = get_http("http://nyu.edu", {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
#                                "like Gecko) Chrome/87.0.4280.66 Safari/537.36", "Connection": "keep-alive",
#                                "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Accept":
#                                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
#                                "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding":
#                                "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Cookie":
#                                f"BIGipServer~WSQ-EDU-MED~www-http={get_rand42()}",
#                                "If-None-Match": "781285-15230-5b48b9dd4ba52"})

user_agents = loads()
