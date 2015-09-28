
from python.messenger import Messenger
from python.UsersHub import UsersHub

__author__ = 'mBAR'


usersHub_ref=UsersHub.start()
users_Proxy=usersHub_ref.proxy()

nnn=input('Choose a number: ')
messageParts=nnn.split(' ')
sender=messageParts[0]
if sender.isdigit():
    message=messageParts[1]
    users_Proxy.handelMessage(sender,message)

print (sender)
counter_ref = Messenger.start()
proxy = counter_ref.proxy()

proxy.write(nnn)
