import requests
import sys


""" 
Get url from user input and make a request to /robots.txt
Then check to see if response is successful (200 code) and run the file_to_write_valid_directories function
"""
def get_robots_from_single_url():
    ask_user_for_url = input("Enter the url you want to get the robots.txt file from. Please include http or https: ")
    add_robots_to_given_url = ask_user_for_url + "/robots.txt"
    get_robots_response = requests.get(add_robots_to_given_url)
    get_robots_response_code = get_robots_response.status_code

    if get_robots_response_code == 200:
        print(get_robots_response.text)
        file_to_write_valid_directories(ask_user_for_url, get_robots_response.text)
    else:
        print("That request wasn't successful. It looks like that url can't resolve a robots.txt file.")
        sys.exit()


"""
Stripping http/https and www. This isn't necessary, but it makes identifying files easier
Then writing the response to a file
"""

def file_to_write_valid_directories(prepend_filename, response):
    protocols = ['http://', 'https://']
    www_prefix = 'www.'
    for x in protocols:
        if x in prepend_filename:
            strip_protocol = prepend_filename.replace(x, '')
            if www_prefix in strip_protocol:
                strip_www = strip_protocol.replace(www_prefix, '')
    new_file = open(f"{strip_protocol}--robots-content.txt", "w+")
    new_file.write(response + "\n")


# TODO: two functions, one for a single input and another for multiple urls from a text file

if __name__ == "__main__":
    get_robots_from_single_url()
