import random

import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

from session import UserSession
from configLoader import ConfigLoader



class Server:

    def __init__(self, api_token, group_id, server_name: str="Empty"):

        self.server_name = server_name
        self.group_id = group_id
        self.vk = vk_api.VkApi(token=api_token)
        self.long_poll = VkBotLongPoll(self.vk, group_id, wait=30)
        self.vk_api = self.vk.get_api()
        self.userSessions = {}
        

    def reduse_appeal(self, message):
        group_name = self.vk_api.groups.getById(fields='name', group_ids=self.group_id)[0]['name']
        appeal_template = "[club" + str(self.group_id) + "|" + group_name + "]"
        if len(message) >= len(appeal_template) :
            if message[:len(appeal_template)] == appeal_template :
                return message[len(appeal_template) + 1:]
        
        appeal_template = "[club" + str(self.group_id) + "|" + "@club" + str(self.group_id) + "]"
        if len(message) >= len(appeal_template) :
            if message[:len(appeal_template)] == appeal_template :
                return message[len(appeal_template) + 1:]
        return message


    def send_msg(self, send_id, message):
        return self.vk_api.messages.send(peer_id=send_id,
                                         message=message,
                                         random_id=random.randint(0, 2048),
                                         keyboard=open(ConfigLoader.getKeyboard(), "r", encoding="UTF-8").read())

    def start(self):
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.message.from_id not in self.userSessions:
                    self.userSessions[event.message.from_id] = UserSession(self.group_id, self.long_poll, self.vk_api)
                self.send_msg(event.message.peer_id, self.userSessions[event.message.from_id].responce(event))

