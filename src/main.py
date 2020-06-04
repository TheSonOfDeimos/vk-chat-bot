from server import Server
from appleKeyChain.keyChain import getPassword

def main():
    sicretName = 'vk_bot_token'
    login = 'vk_bot_token'
    groupId = 195201032
    token = getPassword(sicretName, login)

    server1 = Server(token, groupId, "server1")
    server1.start()


if __name__ == '__main__':
    main()
