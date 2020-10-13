"""
File with FacebookChat class and all its function
"""
from collections import Counter

class FacebookChat:
    """
    class containing information get from file containg facebook messanger chat
    """

    LENGTH_OF_WORDS = ['four', 'five','six', 'seven','eight','nine','ten']

    def __init__(self,
                 file: str = None,
                 total_fb_chat_participants_number=0,
                 total_fb_chat_messages_number=0,
                 total_fb_chat_characters_number=0,
                 total_fb_chat_photos_number=0,
                 total_fb_chat_links_number=0,
                 total_fb_chat_gifs_number=0,
                 total_fb_chat_reactions_number=0,
                 ):
        self._file = file
        self._total_fb_chat_participants_number = (
            total_fb_chat_participants_number)
        self._total_fb_chat_messages_number = total_fb_chat_messages_number
        self._total_fb_chat_characters_number = total_fb_chat_characters_number
        self._total_fb_chat_photos_number = total_fb_chat_photos_number
        self._total_fb_chat_links_number = total_fb_chat_links_number
        self._total_fb_chat_gifs_number = total_fb_chat_gifs_number
        self._total_fb_chat_reactions_number = total_fb_chat_reactions_number
        self._chat_messages = None

    def __str__(self):
        return f'''Facebook chat from file {self._file} has
                   {self._total_chat_messages_number} messages,
                   {self._total_chat_characters_number} characters,
                   {self._total_chat_photos_number} photos,
                   {self._total_chat_gifs_number} gifs.'''

    @property
    def messages(self):
        if self._chat_messages:
            return self._chat_messages
        else:
            return self.file

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file
        self._total_fb_chat_participants_number = (
            self.get_fb_chat_participants_number())
        self._total_fb_chat_gifs_number += (
            self.get_fb_chat_total_gifs_number())
        self._total_fb_chat_messages_number += (
            len(self.messages.get('messages', '')))
        self._total_fb_chat_characters_number += (
            self.get_fb_chat_total_characters_number())
        self._total_fb_chat_photos_number += (
            self.get_fb_chat_total_photos_number())
        self._total_fb_chat_links_number += (
            self.get_fb_chat_total_links_number())
        self._total_fb_chat_reactions_number += (
            self.get_fb_chat_reactions_number()
        )
        self._chat_messages = None

    def set_content(self):
        return self._chat_messages

    def get_fb_chat_title(self):
        return self.correct_string_decoding(self.messages.get('title', ''))

    def get_fb_chat_participants_number(self):
        return len(self.messages.get('participants', ''))

    def correct_string_decoding(self, string):
        try:
            return string.encode('iso-8859-1').decode('utf-8')
        except UnicodeDecodeError as uni_decode_error:
            return string.encode('utf-8')

    def get_fb_chat_participants(self):
        fb_chat_data = self.messages
        participants = []
        for participant in fb_chat_data['participants']:
            participant = self.correct_string_decoding(participant['name'])
            participants.append(participant)
        return participants

    def get_fb_chat_total_photos_number(self):
        photos_counter = 0
        for photo in self.messages.get('messages', ''):
            photos_counter += len(photo.get('photos', ''))
        return photos_counter

    def get_fb_chat_total_gifs_number(self):
        gifs_counter = 0
        for gif in self.messages.get('messages', ''):
            gifs_counter += len(gif.get('gifs', ''))
        return gifs_counter

    def get_fb_chat_total_characters_number(self):
        total_characters_number = 0
        for message in self.messages.get('messages', ''):
            total_characters_number += len(
                self.correct_string_decoding(message.get('content', '')))
        return total_characters_number

    def get_fb_chat_total_links_number(self):
        total_links_number = 0
        for message in self.messages.get('messages', ''):
            if message.get('share', ''):
                if message['share'].get('link', ''):
                    total_links_number += 1
            else:
                continue
        return total_links_number

    def get_fb_chat_reactions_number(self):
        total_reactions_number = 0
        for message in self.messages.get('messages', ''):
            if message.get('reactions', ''):
                total_reactions_number += len(message.get('reactions', ''))
        return total_reactions_number

    def get_fb_chat_total_words_number(self):
        total_words_number = 0
        for message in self.messages.get('messages', ''):
            message = message.get('content', ' ').split()
            total_words_number += len(message)
        return total_words_number

    def get_fb_chat_total_messages_number(self):
        return len(self.messages.get('messages', ''))

    def find_chat_word_frequency(self, word: str):
        messages_string = ''
        word = word.lower()
        for message in self.messages:
            messages_string = messages_string + (
                self.correct_string_decoding(message.get(
                    'content', ' ')).lower()) + ' '
        messages_string = messages_string.split()
        frequency_counter = Counter(messages_string)
        frequency_counter = frequency_counter.get(word, int(0))
        return frequency_counter

    def get_fb_chat_participants_reaction_stat(self):
        reactions = []
        for message in self.messages.get('messages', ''):
            if message.get('reactions',''):
                for reaction in message.get('reactions',''):
                    reactions.extend(tuple(reaction.keys(), reaction.get(reaction.keys(),'')))
                    if reaction.get('actor','') == self.name:
                        pass

    def determine_chat_word_frequency_by_word_length(self, word_len: int):
        messages = []
        for message in self.messages:
            message = self.correct_string_decoding(
                message.get('content', ' ')).lower()
            message = message.split()
            for word in list(message):
                if len(word) < word_len:
                    message.remove(word)
            messages += message
        frequency_counter = Counter(messages)
        return frequency_counter.most_common(word_len)

    def creating_dict_with_words_occurance_sorted_by_length(self):
        words_dict = {}
        for participant in self.messages.get('participants', ''):
            name = self.correct_string_decoding(participant.get('name', ''))
            words_dict[name] = {}
            for word in self.LENGTH_OF_WORDS:
                words_dict[name][word] = []
        for message in self.messages.get('messages',' '):
            if self.correct_string_decoding(message.get('sender_name',' ')) in words_dict:
                for word in message.get('content','').split():
                    word = self.correct_string_decoding(word).lower()
                    if len(word) == 4:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['four'].append(word)
                    elif len(word) == 5:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['five'].append(word)
                    elif len(word) == 6:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['six'].append(word)
                    elif len(word) == 7:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['seven'].append(word)
                    elif len(word) == 8:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['eight'].append(word)
                    elif len(word) == 9:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['nine'].append(word)
                    elif len(word) > 9:
                        words_dict[self.correct_string_decoding(message.get('sender_name',''))]['ten'].append(word)
        return words_dict

    def get_fb_chat_words(self):
        words_list = []
        for content in self.messages.get('messages',''):
            if content.get('content',''):
                temp_list = self.correct_string_decoding(content['content']).lower().split(' ')
                words_list += temp_list
        
        return Counter(words_list)

