import sys
import requests
import bs4


def find_checkpoint(URL, tag, attribute):
    response = requests.get(URL).content
    soup = bs4.BeautifulSoup(response, 'html.parser')
    try:
        tag_result = soup.find(tag, attrs={attribute: True})
        if tag_result is None:
            print("No such tag found.")
            return None
        result = tag_result[attribute]
    except (TypeError, KeyError):
        print("No such tag or attribute found.")
        return None
    if attribute == "final":
        return result

    if result:
        newURL, newTag, newAttribute = result.split(",")
        return find_checkpoint(newURL, newTag, newAttribute)
    return None

if __name__ == '__main__':
    args = sys.argv[1:]
    URL, tag, attribute, output_file = args
    print(find_checkpoint(URL, tag, attribute))
    with open(output_file, 'w') as f:
        f.write(find_checkpoint(URL, tag, attribute))


