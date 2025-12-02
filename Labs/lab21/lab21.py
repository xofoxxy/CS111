import urllib.parse
import requests
import bs4


def get_domain(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc == "" or parsed.scheme not in ["https", "http"]:
        return ""
    return str(parsed.scheme) + "://" + str(parsed.netloc)


def combine_paths(url1, path):
    parsed = urllib.parse.urlparse(url1)

    if parsed.scheme and parsed.netloc:
        base = f"{parsed.scheme}://{parsed.netloc}"
    else:
        base = ""
        return base
    return urllib.parse.urljoin(base, path)


def combine_urls(url1, url2):
    return urllib.parse.urljoin(url1, url2)


def print_pages(url, path_list, output_file):
    current_url = url
    # open once in write mode so the file is clean
    with open(output_file, "w") as f:
        for path in path_list:
            full_url = combine_urls(current_url, path)
            resp = requests.get(full_url)

            text = resp.text.strip()
            f.write(text + "\n")

            current_url = full_url

    return output_file

if __name__ == "__main__":
    print_pages('https://cs111.byu.edu/pages/about/',
                ['/Labs/lab21/assets/page1.html'],
                'paths.output.txt')


