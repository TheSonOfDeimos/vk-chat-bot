import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

from commander import Commander
from messageProcessor import MessageProcessor


class UserSession :
    def __init__(self, t_group_id, t_long_poll, t_vk_api) :
        self.m_group_id = t_group_id
        self.m_long_poll = t_long_poll
        self.m_vk_api = t_vk_api

        self.m_message_processor = MessageProcessor(self.m_group_id, 
                                                    self.m_long_poll, 
                                                    self.m_vk_api)
        self.m_commander = Commander()
        
    
    def responce(self, t_event) :

        f = self.m_message_processor.isCommand(t_event.message.text)
        msg = self.m_message_processor.reduseAppeal(t_event.message.text)
        return self.m_commander.input(msg)