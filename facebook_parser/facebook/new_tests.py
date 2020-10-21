import unittest
import json
import re
from pathlib import Path
# from facebook.bla import FacebookChat


class FacebookChat:
    """
    class containing information get from file containg facebook messanger chat
    """
    MESSAGES = []
    TITLE = None

    def __init__(self, file:str = None):
        self.file = file

    def __str__(self):
        return f"""Facebook chat {self._file}"""

    def extend_class_messages_by_instance_messages(self):
        with open(self.file) as file:
            file = json.load(file)
            print(len(file.get('messages', '')))
            self.MESSAGES.extend(file.get("messages", ''))
    
    def correct_messages_decoding(self):
        for message in self.MESSAGES:
            message.update(sender_name=self.correct_string_decoding(message.get('sender_name', '')))
            message.update(content=self.correct_string_decoding(message.get('content', '')))

    def correct_string_decoding(self, string):
        try: 
            return string.encode("iso-8859-1").decode("utf-8")
        except UnicodeDecodeError as uni_decode_error:
            return string.encode("utf-8")

    def find_regex_expresion(self, regex_expression):
        counter = 0
        for message in self.MESSAGES:
            result = re.match(regex_expression, message.get('content',''))
            if result is not None:
                counter +=1
                print(message.get('content',''))
                print(result)
                print(message.get('sender_name',''))    
        print(counter)


class TestFacebookChat(unittest.TestCase):

    def test_if_variable_is_instance_of_facebook_chat_class(self):
        facebook_chat = FacebookChat("test_file_pl.json")
        self.assertIsInstance(facebook_chat, FacebookChat)
    
    def test_if_messages_are_extended(self):
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_folder = list(file_folder.glob("**/test_file_pl*.json"))
        facebook_chat = FacebookChat("test_file_pl.json")
        for file in file_folder:
            a = FacebookChat(file)
            a.extend_class_messages_by_instance_messages()
        self.assertEqual(len(facebook_chat.MESSAGES), 101996)
        
    def 


if __name__ == '__main__':
    unittest.main()
