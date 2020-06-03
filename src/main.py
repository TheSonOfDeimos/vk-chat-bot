import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re
import random
from keyChain import *

def main():
    sicretName = 'vk_bot_token'
    login = 'vk_bot_token'
    groupId = 195201032
    token = getpassword(sicretName, login)
 
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, groupId)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от: ', end='')
            print(event.message.from_id)
            print('Текст:', event.message.text)
            print()

            if event.from_chat :
                vk.messages.send(message='Привет я DeimosVkBot и пока ничего не умею.', random_id=get_random_id(), chat_id=event.chat_id)
            
            if event.from_user:
                vk.messages.send(message='Привет я DeimosVkBot и пока ничего не умею.', random_id=get_random_id(), user_id=event.message.from_id)
   
        else:
            print(event.type)
            print()

if __name__ == '__main__':
    main()
