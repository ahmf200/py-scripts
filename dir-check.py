import time
import requests
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# accept 2 arguments, a URL and a wordlist file
url = sys.argv[1]
wordlist = sys.argv[2]


# write the requests that returned successful responses to a text file
def file_to_write_valid_directories(word):
    with open("valid-directories-found.txt", "a") as new_file:
        new_file.write(word + "\n")


print(f"[ --- Running against {url} --- ]\n")

# Context manager
with open(wordlist, "r+") as wordlist_file:
    # loop through each word in the wordlist
    for line in wordlist_file:
        word = line.strip()
        # add the word to the url
        full_url = url + word

        # try for a connection
        try:
            response = requests.get(full_url)
            print(f"{bcolors.WARNING}Trying {full_url} ----> Status code: {response.status_code}{bcolors.ENDC}")
            if response.status_code == 200:
                # filter out potential empty lines
                if len(word) > 0:
                    file_to_write_valid_directories(full_url)
                    print(f"{bcolors.BOLD}  [!] FOUND :- {full_url} ----> Status code: {response.status_code}{bcolors.ENDC}")
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('\n[!] You might be missing a slash at the end of the url you provided [!]')
            break
    print("\nSaved successful urls to valid-directories-found.txt")
