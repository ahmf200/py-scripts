import requests
import re
import sys


def get_robots_from_single_url():
    ask_user_for_url = input("Enter the url you want to get the robots.txt file from. Please include http or https: ")
    parse_url_to_name_file = ask_user_for_url.replace('http://', '').replace('.co.uk', '')
    add_robots_to_given_url = ask_user_for_url + "/robots.txt"
    get_robots_response = requests.get(add_robots_to_given_url)
    get_robots_response_code = get_robots_response.status_code
    # print(type(get_robots_response_code))
    # print(get_robots_response.text)

    if get_robots_response_code == 200:
        print(get_robots_response.text)
        file_to_write_valid_directories(parse_url_to_name_file, get_robots_response.text)
    else:
        print("That request wasn't successful. It looks like that url can't resolve a robots.txt file.")
        sys.exit()


def file_to_write_valid_directories(title, response):
    new_file = open(f"{title}--robots-content.txt", "a")
    new_file.write(response + "\n")


# two functions, one for a single input and another for multiple urls from a text file

if __name__ == "__main__":
    get_robots_from_single_url()




