import sys
import os
import requests
from bs4 import BeautifulSoup
# from collections import deque


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


def create_cache_dir(argv):
    """
    func to create dir from argv
    #TODO check for more than 1 args
    @return: path to folder with cached pages
    """
    if len(argv) == 1:
        print("Restart browser with cache-dir argument")
    dir_name = argv[1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name


def save_page_to_cache(page_url, content):
    """
    save content from current page to file
    @param page_url: filename from page url # TODO
    @param content: content of page
    @return: filename
    """
    filename = path + '/' + remove_domain(page_url)
    with open(filename, "w") as f_new:
        f_new.write(content)
    return remove_domain(page_url)


def read_cache(name):
    """
    Func for checking cache and showing pages
    @param name: name of file where page was cached
    @return: cached text from file
    """
    filename = path + '/' + remove_domain(name)
    if os.path.exists(filename):
        with open(filename, "r") as file_open:
            cache = file_open.read()
            file_open.close()
            return cache
    else:
        return False


def check_cache(name):
    """
    check cache dir if there is cached page
    @param name:
    @return: bool
    """
    filename = path + '/' + remove_domain(name)
    if os.path.exists(filename):
        return True


def remove_domain(page_url):
    """
    func for removing domain .com and ect from url
    @param page_url: url from input
    @return:
    """
    filename = page_url.split('.')
    return filename[0]


def is_url(act):
    """
    func check if arg is url and refactor it
    @param act: url or action
    @return: refactored url replace . _
    """
    if act.count('.'):
        return True


def check_connection(url):
    """
    check response from server.
    @param url: url
    @return: bool
    """
    r = requests.get(url)
    if 200 <= r.status_code < 400:
        return True


def show_content(url):
    r = requests.get(url)
    return r.text


def add_prefix(url):
    """
    add https:// to url
    @param url: url without http
    @return: url
    """
    return "https://" + url


args = sys.argv
path = create_cache_dir(args)
actions = ['back', 'quit']
history = []
while (url := input("Enter url:\n")) != "exit":
    page = ''
    if url in actions:
        if url == 'back':
            # if len(history) >= 1: # TODO check history
            history.pop()
            page = read_cache(history.pop())
        elif url == 'history':
            for el in history:
                print(el)
    if check_cache(url):
        page = read_cache(url)
        history.append(url)
    elif is_url(url):
        # if action == 'bloomberg.com':
        #     page = bloomberg_com
        #     history.append(save_page_to_cache(remove_domain(action), page))
        # elif action == 'nytimes.com':
        #     page = nytimes_com
        #     history.append(save_page_to_cache(remove_domain(action), page))
        if check_connection(add_prefix(url)):
            page = show_content(add_prefix(url))
            history.append(save_page_to_cache(remove_domain(url), page))
        else:
            print("Error: Incorrect URL")
    else:
        print("Error: Incorrect URL")
    print(page)
