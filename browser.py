import sys
import os
from collections import deque


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


def input_url() -> str:
    """
    func for processing user input to out format
    check for at least one dot else Errno message
    :return: formatted url or exit command
    """
    user_url = input()
    if user_url == "exit":
        return "exit"
    elif not user_url.count('.'):
        print("Error: Incorrect URL")
    return user_url.replace('.', '_')


def create_cache_dir(argv):
    """
    func to create dir from argv
    #TODO check for more than 1 args
    @return: path to folder with cached pages
    """
    if len(argv) != 2:
        pass    # TODO
    dir_name = argv[1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name


def save_page_to_cache(page_url, content, dir_name):
    """
    save page content to file
    @param page_url: filename from page url # TODO
    @param content: content of page
    @param dir_name: cache dir from argv
    @return: create file
    """
    filename = dir_name + '/' + remove_domain(page_url)
    print(filename)
    with open(filename, "w") as f_new:
        f_new.write(content)
    return filename


def read_cache(name, dir_name):
    filename = dir_name + '/' + remove_domain(name)
    if os.path.exists(filename):
        with open(filename, "r") as file_open:
            cache = file_open.read()
            return cache
    else:
        return False


def remove_domain(page_url):
    filename = page_url.split('.')
    return filename[0]


args = sys.argv
path = create_cache_dir(args)
history = deque()
while (url := input_url()) != "exit":
    page = ''
    if read_cache(url, path):
        page = read_cache(url, path)
    elif url == 'bloomberg_com':
        page = bloomberg_com
        history.append(save_page_to_cache("bloomberg", page, path))
    elif url == 'nytimes_com':
        page = nytimes_com
        history.append(save_page_to_cache("nytimes", page, path))
    elif url == 'back':
        pass
    else:
        print("error")
    print(page)