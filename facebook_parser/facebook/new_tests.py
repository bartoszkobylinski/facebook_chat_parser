import unittest

from pathlib import Path
from new_classes import FacebookChat, Participant


class TestFacebookChat(unittest.TestCase):

    def setUp(self):
        self.facebook_chat = FacebookChat("test_file_pl_0.json")

    def test_if_variable_is_instance_of_facebook_chat_class(self):
        self.assertIsInstance(self.facebook_chat, FacebookChat)

    def test_if_messages_are_extended(self):
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_folder = list(file_folder.glob("**/test_file_pl*.json"))
        for file in file_folder:
            a = FacebookChat(file)
            a.extend_class_messages_by_instance_messages()
        self.assertEqual(len(self.facebook_chat.MESSAGES), 101996)

    def test_if_title_is_get(self):
        self.facebook_chat.get_chat_title()
        self.assertEqual(self.facebook_chat.TITLE, "Alina Barkowa")

    def test_if_participants_are_added(self):
        self.facebook_chat.get_chat_participants()
        self.assertEqual(self.facebook_chat.PARTICIPANTS, ['Alina Barkowa', 'Bartek Kobylinski'])

    def test_if_title_and_participant_are_set_when_more_than_one_file_to_upload(self):
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_folder = list(file_folder.glob("**/test_file_pl*.json"))
        for file in file_folder:
            a = FacebookChat(file)
            a.get_chat_title()
            a.get_chat_participants()
        self.assertEqual(self.facebook_chat.TITLE, 'Alina Barkowa')
        self.assertEqual(self.facebook_chat.PARTICIPANTS, ['Alina Barkowa', 'Bartek Kobylinski'])

    def tearDown(self):
        del self.facebook_chat


class TestParticipant(unittest.TestCase):

    def setUp(self):
        file_folder = Path('/home/bart/PythonProjects/fb/facebook_parser/facebook')
        file_to_open = file_folder/"miriam_text.json"
        self.facebook_chat = FacebookChat(file_to_open)
        print(f"that is: {self.facebook_chat.get_chat_title()}")
        self.facebook_chat.extend_class_messages_by_instance_messages()
        print(f"that is: {self.facebook_chat.get_chat_title()}")
        self.facebook_chat.correct_messages_decoding()

    def test_instantiation(self):
        participants = self.facebook_chat.PARTICIPANTS
        for participant in participants:
            print(participant)
            new_participant = Participant(participant)
            new_participant.messages
            if participant == "Alina Barkowa":
                self.assertEqual(len(new_participant.messages), 63242)
            elif participant == "Bartek Kobylinski":
                self.assertEqual(len(new_participant.messages), 38856)

    def test_get_participant_messages_number(self):
        participant = Participant("Bartek Kobylinski")
        participant.messages
        messages_length = participant.get_messages_number()
        self.assertEqual(messages_length, 38805)

    def tearDown(self):
        del self.facebook_chat


if __name__ == '__main__':
    unittest.main()
