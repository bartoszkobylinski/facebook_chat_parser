import unittest
import json
import re
from pathlib import Path
from new_classes import FacebookChat, Participant


class TestFacebookChat(unittest.TestCase):

    def test_if_variable_is_instance_of_facebook_chat_class(self):
        facebook_chat = FacebookChat("test_file_pl_0.json")
        self.assertIsInstance(facebook_chat, FacebookChat)

    def test_if_messages_are_extended(self):
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_folder = list(file_folder.glob("**/test_file_pl*.json"))
        facebook_chat = FacebookChat("test_file_pl_0.json")
        for file in file_folder:
            a = FacebookChat(file)
            a.extend_class_messages_by_instance_messages()
        self.assertEqual(len(facebook_chat.MESSAGES), 101996)

    def test_if_title_is_get(self):
        facebook_chat = FacebookChat("test_file_pl_0.json")
        facebook_chat.get_chat_title()
        self.assertEqual(facebook_chat.TITLE, "Alina Barkowa")

    def test_if_participants_are_added(self):
        facebook_chat = FacebookChat("test_file_pl_0.json")
        facebook_chat.get_chat_participants()
        self.assertEqual(facebook_chat.PARTICIPANTS, ['Alina Barkowa', 'Bartek Kobylinski'])

    def test_if_title_and_participant_are_set_when_more_than_one_file_to_upload(self):
        facebook_chat = FacebookChat()
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_folder = list(file_folder.glob("**/test_file_pl*.json"))
        for file in file_folder:
            a = FacebookChat(file)
            a.get_chat_title()
            a.get_chat_participants()
        self.assertEqual(facebook_chat.TITLE, 'Alina Barkowa')
        self.assertEqual(facebook_chat.PARTICIPANTS, ['Alina Barkowa', 'Bartek Kobylinski'])

class TestParticipant(unittest.TestCase):

    def test_instantiation(self):
        facebook_chat = FacebookChat("test_file_pl_0.json")
        facebook_chat.extend_class_messages_by_instance_messages()
        print(len(facebook_chat.MESSAGES))
        participants = facebook_chat.PARTICIPANTS
        for participant in participants:
            new_participant = Participant(participant)
            new_participant.messages
            if participant == "Alina Barkowa":
                self.assertEqual(len(new_participant.messages), 109992)
            elif participant == "Bartek Kobylinski":
                self.assertEqual(len(new_participant.messages), 68501)

if __name__ == '__main__':
    unittest.main()
