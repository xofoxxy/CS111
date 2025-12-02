import urllib
import requests
import bs4
import re


class RequestGuard:
    def __init__(self, url):
        parseddata = urllib.parse.urlparse(url)
        self.scheme = parseddata.scheme
        self.url = parseddata.netloc
        print(self.url)
        self.forbidden = self.parse_robots()

    def parse_robots(self):
        robots_url = f"{self.scheme}://{self.url}/robots.txt"
        response = requests.get(robots_url).text.split("\n")
        forbidden = []
        re_forbidden = re.compile("^Disallow: (\/.*)")
        for line in response:
            print(line)
            match = re_forbidden.match(line)
            if match:
                print("match found!")
                forbidden.append(match.group(1))
            else:
                print("no match found")
        return forbidden

    def can_follow_link(self, URL):
        given_url = urllib.parse.urlparse(URL)
        if given_url.netloc != self.url:
            return False
        for disallowed in self.forbidden:
            if given_url.path.startswith(disallowed):
                return False
        return True

    def make_get_request(self, URL):
        if self.can_follow_link(URL):
            return requests.get(URL)
        else:
            return None

if __name__ == "__main__":
    guard = RequestGuard("https://cs111.byu.edu/")
    print(guard.forbidden)