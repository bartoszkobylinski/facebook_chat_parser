
import string
from collections import Counter


class FacebookChat:
    """
    class containing information get from file containg facebook messanger chat
    """
    LENGTH_OF_WORDS = ["four", "five", "six", "seven", "eight", "nine", "ten"]

    def __init__(self, file):
        self.file = file
        self.messages = self.file.get("messages", "")
        self.participants = [self.correct_string_decoding(participant.get("name", ""))
                             for participant in self.file.get("participants", "")]

    def __str__(self):
        return f"""Facebook chat {self._file}"""

    def correct_messages_decoding(self):
        for message in self.messages:
            message.update(sender_name=self.correct_string_decoding(message.get('sender_name', '')))
            message.update(content=self.correct_string_decoding(message.get('content', '')))
            for reaction in message.get("reactions", ""):
                reaction.update(reaction=self.correct_string_decoding(reaction.get("reaction")))
                reaction.update(actor=self.correct_string_decoding(reaction.get("actor")))

    def correct_string_decoding(self, string):
        try:
            return string.encode("iso-8859-1").decode("utf-8")
        except UnicodeEncodeError as uni_encode_error:
            return string.encode("utf-8")
        except UnicodeDecodeError as uni_decode_error:
            return string.encode("utf-8")
        except AttributeError as attr_error:
            return string.decode("utf-8")

    def creating_dict_with_words_occurance_sorted_by_length(self):
        words_dict = {}
        for participant in self.participants:
            name = participant
            words_dict[name] = {}
            for word in FacebookChat.LENGTH_OF_WORDS:
                words_dict[name][word] = []
        for message in self.messages:
            if message.get("sender_name", "") in words_dict:
                for word in message.get("content", '').split():
                    word = word.lower().translate(str.maketrans('', '', string.punctuation))
                    if len(word) < 4:
                        continue
                    elif len(word) == 4:
                        words_dict[message.get("sender_name", "")]["four"].append(word)
                    elif len(word) == 5:
                        words_dict[message.get("sender_name", "")]["five"].append(word)
                    elif len(word) == 6:
                        words_dict[message.get("sender_name", "")]["six"].append(word)
                    elif len(word) == 7:
                        words_dict[message.get("sender_name", "")]["seven"].append(word)
                    elif len(word) == 8:
                        words_dict[message.get("sender_name", "")]["eight"].append(word)
                    elif len(word) == 9:
                        words_dict[message.get("sender_name", "")]["nine"].append(word)
                    elif len(word) > 9:
                        words_dict[message.get("sender_name", "")]["ten"].append(word)
        return words_dict


class Participant(FacebookChat):

    def __init__(self, name, messages):
        self.name = name
        self.messages = messages

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

    def get_participant_reactions_number(self, facebook_messages):
        reactions = []
        for message in facebook_messages:
            if message.get("reactions", ""):
                for reaction in message.get("reactions", ""):
                    if reaction.get("actor", "") == self.name:
                        reactions.append(reaction.get("reaction", ""))
        reactions_number = len(reactions)
        most_common_reaction = Counter(reactions).most_common(1)
        return reactions_number, most_common_reaction
