import sys
import os
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
    if len(argv) > 2:
        print("Too much arguments")
        pass    # TODO
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
        return act.replace('.', '_')


args = sys.argv
path = create_cache_dir(args)
history = []
while (action := input()) != "exit":
    page = ''
    if check_cache(action):
        page = read_cache(action)
        history.append(action)
    elif is_url(action):
        if action == 'bloomberg.com':
            page = bloomberg_com
            history.append(save_page_to_cache(remove_domain(action), page))
        elif action == 'nytimes.com':
            page = nytimes_com
            history.append(save_page_to_cache(remove_domain(action), page))
        else:
            print("Error: Incorrect URL")
    elif action == 'back':
        # if len(history) >= 1: # TODO check history
        history.pop()
        page = read_cache(history.pop())
    elif action == 'history':
        for el in history:
            print(el)
    else:
        print("error")
    print(page)
