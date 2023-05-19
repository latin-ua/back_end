import unittest
from ua_latin import word_translate


class TestWordTranslate(unittest.TestCase):
    def test_lowercase_one_word(self):
        source_text = "укрзалізниця"
        expected_translation = "ukrzaliznytsia"
        actual_translation = word_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
