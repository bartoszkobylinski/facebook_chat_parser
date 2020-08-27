
from .facebook_chat import FacebookChat


class Participant(FacebookChat):

    def __init__(self, name, fb_chat):
        self.name = name
        self.fb_chat = fb_chat
        self._chat_messages = None

    def __str__(self):
        return f"Your name is {self.name}"

    def get_messages(self, messages):
        if self._chat_messages:
            return self._chat_messages
        else:
            participant_messages = []
            for message in messages:
                if self.correct_string_decoding(
                    message.get('sender_name')) == self._name:
                    message = self.correct_string_decoding(
                        message.get('content', ''))
                    participant_messages.append(message)
            self._chat_messages = participant_messages
            return self._chat_messages

    def get_messages_number_of_participant(self):
        return len(self._chat_messages)

    def get_participants_messages_number(self):
        participant_messages_number = 0
        # print(self.messages.get('participants','blbla'))
        messages = self.fb_chat.get('messages','')
        for message in messages:
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_messages_number += 1
        return participant_messages_number
    
    def get_participant_characters_number(self):
        participant_characters_number = 0
        messages = self.fb_chat.get('messages', '')
        for message in messages:
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_characters_number += len(self.correct_string_decoding(message.get('content',' ')))
        return participant_characters_number

    def get_participant_photos_number(self):
        participant_photos_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_photos_number += len(message.get('photos', ''))
        return participant_photos_number
    
    def get_participant_links_number(self):
        participant_links_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                if message.get('share',''):
                    if message['share'].get('link',''):
                        participant_links_number +=1
        return participant_links_number

    def get_participant_gifs_number(self):
        participant_gifs_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_gifs_number += len(message.get('gifs', ''))
        return participant_gifs_number
