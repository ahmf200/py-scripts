import requests
import sys


url = sys.argv[1]
wordlist = sys.argv[2]
# file_extension = sys.argv[3]


# function to write valid directories which return with response code of 200, to a file
def file_to_write_valid_directories(word):
    new_file = open("valid-directories-found.txt", "w+")
    new_file.write(word + "\n")


wordlist_file = open(wordlist, "r+")
for i in range(2000):
    word = wordlist_file.readline(10).strip()
    full_url = url + word

    # Create a get request for url and word from the wordlist
    response = requests.get(full_url)

    # Check if the response code returns a success
    if response.status_code == 200:
        print("[+] found :- ", full_url)
        file_to_write_valid_directories(word)
    else:
        print("[-] Not found :- ", full_url)
        pass
