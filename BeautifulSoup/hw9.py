import urllib.request
import urllib.robotparser
import urllib.parse
import bs4
import re


def get_links(url):
    """
    Open the given url and return all the anchor links.
    :param url:(string) -the address of the web page to be read
    :return: (list of strings) all the filtered links
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            soup = bs4.BeautifulSoup(url_file, "html.parser")
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        regex = re.compile("/web-dbgen/artic/[A-Z]")
        relative_links = {urllib.parse.urljoin(url, anchor.get('href', None))
                          for anchor in soup('a', href=regex)}
        return sorted(relative_links)


def read_url(url_list):
    dictionary = dict()
    for url in url_list:
        try:
            with urllib.request.urlopen(url) as url_file:
                bytes = url_file.read()
        except urllib.error.URLError as url_err:
            print(f'Error opening url: {url}\n{url_err}')
        else:
            soup = bs4.BeautifulSoup(bytes, 'html.parser')
            name = soup.find('h3')
            print(name.text[31:])
            td = soup.find_all('td')
            for each_td in td:
                if "CS 0" in each_td.text:
                    next_td = each_td.find_next_sibling('td')
                    next_next_td = next_td.find_next_sibling('td')
                    if next_next_td.text != "No Current Equivalent":
                        dictionary[each_td.text] = \
                            next_next_td.text
                        print(each_td.text + ": " + next_next_td.text)
    return dictionary


def main():
    link_list = get_links("http://info.sjsu.edu/web-dbgen/artic/"
                          "all-course-to-course.html")
    print(link_list)
    class_dictionary = read_url(link_list)


if __name__ == "__main__":
    main()
