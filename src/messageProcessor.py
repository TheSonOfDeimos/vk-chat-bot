import re
from commander import Commander
from command_enum import CommandDictionary

class MessageProcessor :

    def __init__(self, t_group_id, t_long_poll, t_vk_api) :
        self.m_group_id = t_group_id
        self.m_long_poll = t_long_poll
        self.m_vk_api = t_vk_api
        
    def flow(self, t_message) :
        return 0

    def isCommand(self, t_message) :
        msg = self.reduseAppeal(t_message)
        if msg in CommandDictionary.commandMap() :
            return True
        
        for command in CommandDictionary.commandMap().items() :
            if msg in command[1] :
                return True

        False


    def isAppeal(self, t_message) :
        if re.findall(r'^\[((id)|(club))\d*\|.*\]', t_message) :
            return True
        return False
    
    def isAppealToBot(self, t_message) :
        if re.findall(rf"^\[(club)({str(self.m_group_id)})\|.*\]", t_message) :
            return True
        return False

    def reduseAppeal(self, t_message):
        msg_copy = t_message
        return re.sub(r'^\[((id)|(club))\d*\|.*\](\s)*', '', msg_copy)