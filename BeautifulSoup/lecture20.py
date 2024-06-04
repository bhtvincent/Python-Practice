# ----------------------------------------------------------------------
# Name:        lecture20
# Purpose:     Demonstrate using Beautiful Soup to parse html files
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 20.

Demonstrate using Beautiful Soup to parse html files.
"""
import bs4
import re


def make_soup(filename):
    """
    Parse the html file specified.
    :param filename: string - name of the html file to be parsed
    :return: BeautifulSoup object
    """
    with open(filename, 'r', encoding='utf-8') as html_file:
        soup = bs4.BeautifulSoup(html_file, "html.parser")
    return soup


def taste(soup):
    """
    Explore the given Beautiful soup object.
    :param soup: BeautifulSoup object
    :return: None
    """
    table = soup.find_all('table')
    table = table[0]
    regex =re.compile(r"site",re.IGNORECASE)
    all_sites = table.find_all('td',string=regex)
    for each_site in all_sites:
        next_column = each_site.find_next_sibling('td')
        description = next_column.get_text(separator= ' ')
        description = ' '.join(description.split())
        print(description)



def main():
    soup = make_soup("demosoup.html")
    taste(soup)



if __name__ == "__main__":
    main()
