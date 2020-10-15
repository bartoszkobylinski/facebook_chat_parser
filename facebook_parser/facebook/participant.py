
from collections import Counter
from facebook.facebook_chat import FacebookChat


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
                if self.correct_string_decoding(message.get('sender_name')) == self._name:
                    message = self.correct_string_decoding(message.get('content', ''))
                    participant_messages.append(message)
            self._chat_messages = participant_messages
            return self._chat_messages

    def get_messages_number_of_participant(self):
        return len(self._chat_messages)

    def get_participants_messages_number(self):
        participant_messages_number = [
            () for message in self.fb_chat.get('messages', '')
            if self.correct_string_decoding(
                message.get('sender_name', '')) == self.name]
        return len(participant_messages_number)

    def get_participant_characters_number(self):
        participant_characters_number = [
            len(self.correct_string_decoding(message.get('content', '')))
            for message in self.fb_chat.get('messages', '')
            if self.correct_string_decoding(
                message.get('sender_name', '')) == self.name]
        return sum(participant_characters_number)

    def get_participant_photos_number(self):
        participant_photos_number = [
            len(message.get('photos', ''))
            for message in self.fb_chat.get('messages', '')
            if self.correct_string_decoding(
                message.get('sender_name', '')) == self.name]
        return sum(participant_photos_number)

    def get_participant_links_number(self):
        participant_links_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                if message.get('share', ''):
                    if message['share'].get('link', ''):
                        participant_links_number += 1
        return participant_links_number

    def get_participant_gifs_number(self):
        participant_gifs_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_gifs_number += len(message.get('gifs', ''))
        return participant_gifs_number

    def get_participant_words_number(self):
        participant_words_number = 0
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                participant_words_number += len(message.get('content', '').split())
        return participant_words_number

    def get_participant_reactions_number(self):
        reactions = []
        for message in self.fb_chat.get('messages', ''):
            if message.get('reactions', ''):
                for reaction in message.get('reactions', ''):
                    if self.correct_string_decoding(reaction.get('actor', '')) == self.name:
                        reactions.append(self.correct_string_decoding(reaction.get('reaction', '')))
        reactions_number = len(reactions)
        most_common_reaction = Counter(reactions).most_common(1)
        return reactions_number, most_common_reaction

    def get_participant_most_common_reaction(self):
        reactions = []
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                if message.get('reactions'):
                    reaction_list = message.get('reactions', '')
                    for reaction in reaction_list:
                        reaction = self.correct_string_decoding(reaction.get('reaction', ''))
                        reactions.append(reaction)
        reaction_statistic = Counter(reactions)
        return reaction_statistic.most_common(1)

    def get_participant_most_common_words(self, number_of_words):
        participant_words = []
        for message in self.fb_chat.get('messages', ''):
            if self.correct_string_decoding(message.get('sender_name', '')) == self.name:
                for word in message.get('content', '').split():
                    if len(word) > 3:
                        try:
                            participant_words.append(self.correct_string_decoding(word).lower())
                        except AttributeError as err:
                            print(f"Attribute error while {word} something {err}")
        words_counter = Counter(participant_words).most_common(number_of_words)
        return words_counter
