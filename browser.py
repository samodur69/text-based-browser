import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def create_cache_dir():
    """
    func to create dir from argv
    @return: folder name where cached pages
    """
    arg = sys.argv
    directory = arg[1]
    try:
        if len(arg) == 2 and not os.path.exists(directory):
            os.mkdir(f'./{directory}')
        return directory
    except IndexError:
        print("Wrong number of arguments Should be 2 args")
        exit()


def display_cache(path):
    """
    Func for checking cache and showing pages
    @param path: name of file where page was cached
    @return: cached text from file
    """
    try:
        with open(path, "r", encoding='UTF-8') as file_open:
            print(file_open.read())
    except IndexError:
        print(f'File {path} not found')


def display_cache2(filename):
    try:
        with open(os.path.join(sys.argv[1], filename), "r", encoding='UTF-8') as file_open:
            print(file_open.read())
    except IndexError:
        print(f'File {filename} not found')


def cache_page(url, path):
    tag_list = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    page = requests.get(add_prefix(url))
    soup = BeautifulSoup(page.content, "html.parser")
    we_need = soup.find_all(tag_list)
    with open(path, 'w+', encoding='UTF-8') as cache:
        for el in we_need:
            cache.write(el.get_text() + '\n')


def remove_domain(link):
    """
    func for removing domain .com and ect from url
    @param link: url from input
    @return:
    """
    domains = link.split('.')
    if len(domains) > 1:
        return '.'.join(domains[:-1])
    else:
        return link


def check_connection(link):
    """
    check response from server.
    @param link: url
    @return: bool
    """
    r = requests.get(link)
    if 200 <= r.status_code < 400:
        return True


def add_prefix(link):
    """
    add https:// to url
    @param link: url without http
    @return: url
    """
    return "https://" + link


def main():
    actions = ['back', 'quit', 'history']
    history = []
    directory = create_cache_dir()
    while (url := input("Enter url:\n")) != "exit":
        path = os.path.join(directory, remove_domain(url))
        # path = directory + '/' + remove_domain(url)
        if url in actions:
            if url == 'back':
                # if len(history) >= 1: # TODO check history
                history.pop()
                display_cache(f'{directory}/{history.pop()}')
            elif url == 'history':
                for el in history:
                    print(el)
        else:
            if os.path.isfile(path):
                display_cache(path)
                # display_cache2(remove_domain(url))
                history.append(remove_domain(url))
            elif url.count('.'):
                if check_connection(add_prefix(url)):
                    cache_page(url, path)
                    display_cache(path)
                    history.append(remove_domain(url))
                else:
                    print("Error: Incorrect URL")
            else:
                print("Error: Incorrect URL. Didn't use . in url")


if __name__ == "__main__":
    main()
