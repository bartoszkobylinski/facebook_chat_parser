import time
from dawi import FacebookChat


class Participant(FacebookChat):
    
    def __init__(self, name,
                total_messages_number=0,
                total_characters_number=0,
                total_photos_number=0,
                total_gifs_number=0):
        self._name = name 
        self._total_messages_number = total_messages_number
        self._total_characters_number = total_characters_number
        self._total_photos_number = total_photos_number
        self._total_gifs_number = total_gifs_number
        self._messages = None


    def __str__ (self):
        return f"Your name is {self._name} and messages {len(self._messages)}"

    
    def get_messages(self, messages):
        if self._messages:
            return self._messages
        else:
            participant_messages = []
            for message in messages:
                if message.get('sender_name') == self._name:
                    participant_messages.append(message)
            self._messages = participant_messages
            return self._messages
    



chat = FacebookChat()

for file in ['nie_ten_watek_1.json','nie_ten_watek_2.json','nie_ten_watek_3.json','nie_ten_watek_4.json','nie_ten_watek_5.json']:
    chat.file = file
    chat.messages
    participants = chat.get_participants_of_chat()
    #print(chat.messages[4:6])
    #print(chat)
    #print(f"that is content {content[56]}")
    for participant in participants:
        a = Participant(participant.get('name',''))
        participant_messages = a.get_messages(chat.set_content()) 
        print(participant_messages[3:4])
        print(a.get_chat_total_gifs_number())
        print(f"that is len {len(participant_messages)}")
        #print(a._messages[4:15])
       
       
