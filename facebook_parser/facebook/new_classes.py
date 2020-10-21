from pathlib import Path
import json
import re


class FacebookChat:
    """
    class containing information get from file containg facebook messanger chat
    """
    MESSAGES = []
    TITLE = None
    PARTICIPANTS = []

    def __init__(self, file: str = None):
        self.file = file

    def __str__(self):
        return f"""Facebook chat {self._file}"""

    def extend_class_messages_by_instance_messages(self):
        with open(self.file) as file:
            file = json.load(file)
            FacebookChat.MESSAGES.extend(file.get("messages", ''))
    
    def correct_messages_decoding(self):
        for message in FacebookChat.MESSAGES:
            message.update(sender_name=self.correct_string_decoding(message.get('sender_name', '')))
            message.update(content=self.correct_string_decoding(message.get('content', '')))

    def correct_string_decoding(self, string):
        try:
            return string.encode("iso-8859-1").decode("utf-8")
        except UnicodeDecodeError as uni_decode_error:
            return string.encode("utf-8")
    
    
    def get_chat_title(self):
        if not FacebookChat.TITLE:
            with open(self.file) as file:
                file = json.load(file)
                FacebookChat.TITLE = file.get("title", "")
        
    def get_chat_participants(self):
        if not FacebookChat.PARTICIPANTS:
            with open(self.file) as file:
                file = json.load(file)
                for participant in file.get('participants', ''):
                    FacebookChat.PARTICIPANTS.append(participant.get('name',''))

    def find_regex_expresion(self, regex_expression):
        counter = 0
        for message in self.MESSAGES:
            result = re.match(regex_expression, message.get('content', ''))
            if result is not None:
                pass


class Participant(FacebookChat):

    def __init__(self, name):
        self.name = name


    @property
    def messages(self):
        messages = []
        for message in FacebookChat.MESSAGES:
            if message.get("sender_name") == self.name:
                messages.append(message)
        return messages
        






'''  
blabla=["Zadzwoniłeś do Aliny"]
REGEX_EXPR = "@Anna"

files = ['nie_ten_watek_1.json','nie_ten_watek_2.json','nie_ten_watek_3.json','nie_ten_watek_4.json']
file_folder = Path('/home/bart/PythonProjects/fb/')
file_folder = list(file_folder.glob("**/nie_ten_watek_*.json"))

a = FacebookChat(file_folder)
for file in file_folder:
    b = FacebookChat(file)
    b.extend_class_messages_by_instance_messages()
a.correct_messages_decoding()
a.find_regex_expresion(REGEX_EXPR)
#print(a.MESSAGES)
print(f"that is len of a.MESSAGES {len(a.MESSAGES)}")


'''
'''
file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook/')
file_to_open = file_folder/"test_file_pl.json"

with open(file_to_open) as file:
    file = json.load(file)
    messages = file['messages'][:25499]
    file.pop('messages')
    print(file.keys())
    file.update(messages=messages)
    f = open("test_file_pl_1.json", "w")
    file = json.dump(file, fp=f, indent=4)
    f.close()
'''
    
    
    
    

print("koniec")