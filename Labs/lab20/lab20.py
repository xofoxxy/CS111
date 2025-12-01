import requests
import bs4
import regex as re


def download(url, output_filename):
    website = requests.get(url)
    text = website.text
    with open(output_filename, 'w') as f:
        f.write(text)
    return output_filename


def make_pretty(url, output_filename):
    website = requests.get(url)
    soup = bs4.BeautifulSoup(website.text, 'html.parser')
    pretty = soup.prettify()
    with open(output_filename, 'w') as f:
        f.write(pretty)
    return output_filename


def find_paragraphs(url, output_filename):
    website = requests.get(url)
    soup = bs4.BeautifulSoup(website.text, 'html.parser')
    paragraphs = soup.find_all('p')  # EXACT match for expected output
    with open(output_filename, 'w') as f:
        for p in paragraphs:
            f.write(str(p)+"\n")
    return output_filename


def find_links(url, output_filename):
    website = requests.get(url)
    soup = bs4.BeautifulSoup(website.text, 'html.parser')
    links = soup.find_all("a")
    with open(output_filename, 'w') as f:
        for link in links:
            f.write(link.get("href") + "\n")
    return output_filename

