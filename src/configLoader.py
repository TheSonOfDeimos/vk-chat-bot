import json

class ConfigLoader(object) :
    m_keyboard_path = ""
    m_commands_path = ""

    @classmethod
    def initConfig(cls) :
        if cls.m_commands_path != "" :
            return

        file_str = open("/Users/levkargalov/Documents/Projects/Programming/Python/vk-chat-bot/src/config/botConfiguration.json", "r", encoding="UTF-8").read()
        data = json.loads(file_str)
        cls.m_keyboard_path = data['keyboard']
        cls.m_commands_path = data['commands']
    
    @classmethod
    def getKeyboard(cls) :
        cls.initConfig()
        return cls.m_keyboard_path

    @classmethod
    def getCommands(cls) :
        cls.initConfig()
        return cls.m_commands_path