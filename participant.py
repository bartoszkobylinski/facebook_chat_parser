
from facebook_chat import FacebookChat


class Participant(FacebookChat):

    def __init__(self, name): # total_messages_number=0, total_characters_number=0, total_photos_number=0, total_gifs_number=0):
        self._name = name
        '''
        self._participant_messages_number = total_messages_number
        self._participant_characters_number = total_characters_number
        self._participant_photos_number = total_photos_number
        self._participant_gifs_number = total_gifs_number
        '''
        self._chat_messages = None

    def __str__(self):
        return f"Your name is {self._name}"

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

    def get_words_number_of_participant(self):
        pass



chat = FacebookChat()

for file in ['nie_ten_watek_1.json']:
    '''
    'nie_ten_watek_2.json',
    'nie_ten_watek_3.json',
    'nie_ten_watek_4.json',
    'nie_ten_watek_5.json']
    '''
    chat.file = file
    chat.messages
    participants = chat.get_participants_of_chat()
    print(participants)
    for participant in participants:
        user = Participant(participant)
        print(user.get_messages(chat.messages))
        print(f"That is nu: {user.get_messages_number_of_participant()}")
        gif = user.get_chat_total_gifs_number()
        print(f"that is gifs number: {gif}")