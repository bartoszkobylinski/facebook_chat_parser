from pathlib import Path
import json
import re
from collections import Counter


class FacebookChat:
    """
    class containing information get from file containg facebook messanger chat
    """
    LENGTH_OF_WORDS = ["four", "five", "six", "seven", "eight", "nine", "ten"]
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
            for message in file.get("messages", ""):
                FacebookChat.MESSAGES.append(message)

    def correct_messages_decoding(self):
        for message in FacebookChat.MESSAGES:
            message.update(sender_name=self.correct_string_decoding(message.get('sender_name', '')))
            message.update(content=self.correct_string_decoding(message.get('content', '')))

    def correct_string_decoding(self, string):
        try:
            return string.encode("iso-8859-1").decode("utf-8")
        except UnicodeEncodeError as uni_encode_error:
            return string.encode("utf-8")
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
                    FacebookChat.PARTICIPANTS.append(
                        self.correct_string_decoding(participant.get('name', '')))

    def creating_dict_with_words_occurance_sorted_by_length(self):
        words_dict ={}
        for participant in FacebookChat.PARTICIPANTS:
            name = participant.get("name","")
            words_dict[name] = {}
            for word in FacebookChat.LENGTH_OF_WORDS:
                words_dict[name][word] = []
        for message in FacebookChat.MESSAGES:
            if message.get("sender_name", "") in words_dict:
                for word in message.get("content", '').split():
                    if len(word) == 4:
                        words_dict[message.get("sender_name","")]["four"].append(word)
                    if len(word) == 5:
                        words_dict[message.get("sender_name","")]["five"].append(word)
                    if len(word) == 6:
                        words_dict[message.get("sender_name","")]["six"].append(word)
                    if len(word) == 7:
                        words_dict[message.get("sender_name","")]["seven"].append(word)
                    if len(word) == 8:
                        words_dict[message.get("sender_name","")]["eight"].append(word)
                    if len(word) == 9:
                        words_dict[message.get("sender_name","")]["nine"].append(word)
                    if len(word) > 9:
                        words_dict[message.get("sender_name","")]["ten"].append(word)
        return words_dict



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

    def get_participant_messages_number(self):
        return len(self.messages)

    def get_participant_characters_number(self):
        participant_characters_number = [
            len(message.get('content', ''))
            for message in self.messages
        ]
        return sum(participant_characters_number)

    def get_participant_photos_number(self):
        participant_photos_number = [
            len(message.get('photos', ''))
            for message in self.messages
        ]
        return sum(participant_photos_number)

    def get_participant_links_number(self):
        link_counter = 0
        for message in self.messages:
            if message.get("share", ""):
                if message['share'].get("link", ""):
                    link_counter += 1
        return link_counter

    def get_participant_gifs_number(self):
        participant_gifs_number = [
            len(message.get('gifs', ''))
            for message in self.messages
        ]
        return sum(participant_gifs_number)

    def get_participant_words_number(self):
        words_counter = 0
        for message in self.messages:
            text = message.get("content", "").split()
            words_counter += len(text)
        return words_counter
    
    def get_participant_reactions_number(self):
        reactions = []
        for message in FacebookChat.MESSAGES:
            if message.get("reactions", ""):
                for reaction in message.get("reactions", ""):
                    if reaction.get("actor", "") == self.name:
                        reactions.append(reaction.get("reaction", ""))
        reactions_number = len(reactions)
        most_common_reaction = Counter(reactions).most_common(1)
        return reactions_number, most_common_reaction

file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook/')
file_to_open = file_folder/"nie_ten_watek_5.json"

a = FacebookChat(file_to_open)
a.extend_class_messages_by_instance_messages()
a.correct_messages_decoding()
a.get_chat_participants()
participants = a.PARTICIPANTS
a.get_chat_title()

for participant in participants:
    print(participant)
    participant = Participant(participant)
    message_num = participant.get_participant_messages_number()
    print(f"that is message number: {message_num}")
    characters_num = participant.get_participant_characters_number()
    print(f"that is characters number: {characters_num}")
    photos_num = participant.get_participant_photos_number()
    print(f"that is photos number: {photos_num}")
    link_num = participant.get_participant_links_number()
    print(f"that is links number: {link_num}")
    gifs_num = participant.get_participant_gifs_number()
    print(f"that is gifs number: {gifs_num}")
    words_num = participant.get_participant_words_number()
    print(f"that is words number: {words_num}")
    print("-----------------------------------------")