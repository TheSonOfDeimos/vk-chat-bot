from enum import Enum
from collections import ChainMap
from configLoader import ConfigLoader
import json

class CommandDictionary(object) :
    m_command_map = ChainMap()

    @classmethod
    def commandMap(cls) :   
        cls.commandsFromButtons()
        cls.commandFromList()
        return cls.m_command_map

    @classmethod
    def commandsFromButtons(cls) :
        file_str = open(ConfigLoader.getKeyboard(), "r", encoding="UTF-8").read()
        data = json.loads(file_str)
        for button in data['buttons'][0] :
            cls.m_command_map[button['action']['label']] = button['action']['payload']
    
    @classmethod
    def commandFromList(cls) :
        file_str = open(ConfigLoader.getCommands(), "r", encoding="UTF-8").read()
        data = json.loads(file_str)
        for command in data['user'] :
            cls.m_command_map[command['label']] = command['synonyms']


