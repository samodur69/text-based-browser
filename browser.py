import sys
import os
import requests
from bs4 import BeautifulSoup


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's
 Bad Moon Rising. The world is a very different place than
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.

'''


def create_cache_dir():
    """
    func to create dir from argv
    @return: folder name where cached pages
    """
    arg = sys.argv
    directory = arg[1]
    try:
        if len(arg) == 2 and not os.path.exists(directory):
            os.mkdir(directory)
        return directory
    except IndexError:
        print("Wrong number of arguments Should be 2 args")
        exit(1)


def display_cache(path):
    """
    Func for checking cache and showing pages
    @param path: name of file where page was cached
    @return: cached text from file
    """
    try:
        with open(path, "r") as file_open:
            print(file_open.read())
    except IndexError:
        print(f'File {path} not found')


def cache_page(url, path):
    tag_list = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    page = requests.get(add_prefix(url))
    soup = BeautifulSoup(page.content, "html.parser")
    we_need = soup.find_all(tag_list)
    with open(path, 'w+') as f_new:
        for el in we_need:
            f_new.write(el.get_text() + '\n')


# def check_cache(name):
#     """
#     check cache dir if there is cached page
#     @param name:
#     @return: bool
#     """
#     filename = directory + '/' + remove_domain(name)
#     if os.path.exists(filename):
#         return True


def remove_domain(link):
    """
    func for removing domain .com and ect from url
    @param link: url from input
    @return:
    """
    domains = link.split('.')
    if len(domains) > 1:
        return '_'.join(domains[:-1])
    else:
        return link


def is_url(act):
    """
    func check if arg is url
    @param act: url or action
    @return: boolean
    """
    if act.count('.'):
        return True


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
    actions = ['back', 'quit']
    history = []
    directory = create_cache_dir()

    while (url := input()) != "exit":
        path = directory + '/' + remove_domain(url)
        if url in actions:
            if url == 'back':
                # if len(history) >= 1: # TODO check history
                history.pop()
                # page = read_cache(history.pop())
            elif url == 'history':
                for el in history:
                    print(el)
        else:
            if os.path.isfile(path):
                display_cache(path)
                history.append(remove_domain(url))
            elif is_url(url):
                if url == 'bloomberg.com':
                    page = bloomberg_com
                    print(page)
                    history.append(bloomberg_com)
                elif url == 'nytimes.com':
                    page = nytimes_com
                    print(page)
                    history.append(nytimes_com)
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
