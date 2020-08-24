
import unittest

from facebook_chat import FacebookChat


class TestFacebookChat(unittest.TestCase):

    def setUp(self):
        self.fb_chat = FacebookChat('test_file_pl.json')

    def test_correct_get_participant_of_chat(self):
        self.assertEqual(
            ['Alina Barkowa', 'Bartek Kobylinski'],
            self.fb_chat.get_participants_of_chat(),
            'list not contain correct participants')

    def test_not_correct_participants_of_chat(self):
        self.assertNotEqual(
            ['oeuntoheunthoe', 'oeuthoneuth'],
            self.fb_chat.get_participants_of_chat(),
            "list don't contain correct participants"
        )

    def test_correct_string_decoding(self):
        test_string = "Zadzwoni\u00c5\u0082e\u00c5\u009b do Gwiazdeczka."
        self.assertEqual(self.fb_chat.correct_string_decoding(test_string),
                         'Zadzwoniłeś do Gwiazdeczka.')
        self.assertNotEqual(self.fb_chat.correct_string_decoding(test_string),
                            'Zadzwoniles do gwiazdeczka')

    def test_get_chat_total_photos_number(self):
        self.assertEqual(2543, self.fb_chat.get_chat_total_photos_number())
        self.assertNotEqual(123, self.fb_chat.get_chat_total_photos_number())

    def test_get_total_gifs_number(self):
        self.assertEqual(116, self.fb_chat.get_chat_total_gifs_number())
        self.assertNotEqual(14, self.fb_chat.get_chat_total_gifs_number())

    def test_get_chat_total_characters_number(self):
        self.assertEqual(2077421,
                         self.fb_chat.get_chat_total_characters_number())
        self.assertNotEqual(14,
                            self.fb_chat.get_chat_total_characters_number())

    def test_get_chat_total_words_number(self):
        self.assertEqual(362337, self.fb_chat.get_chat_total_words_number())
        self.assertNotEqual(152, self.fb_chat.get_chat_total_words_number())
        pass

    def test_find_chat_word_frequency(self):
        self.assertEqual(1, self.fb_chat.find_chat_word_frequency('hala'))
        self.assertEqual(85, self.fb_chat.find_chat_word_frequency('kurwa'))
        self.assertEqual(632, self.fb_chat.find_chat_word_frequency('dobrze'))
        self.assertEqual(102, self.fb_chat.find_chat_word_frequency('tata'))
    
    def test_determine_chat_word_frequency_by_word_length(self):
        self.assertEqual([('nie', 12151), ('ale', 4567), ('jak', 4214)],
                         self.fb_chat.determine_chat_word_frequency_by_word_length(3))


if __name__ == '__main__':
    unittest.main()
