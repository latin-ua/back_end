import unittest
from ua_latin import word_translate


class TestWordTranslate(unittest.TestCase):
    def test_lowercase_one_word(self):
        source_text = ("Жебракують філософи при ґанку церкви в Гадячі, "
                       "ще й шатро їхнє п'яне знаємо")
        expected_translation = ("Zhebrakuiut filosofy pry ganku tserkvy v "
                                "Hadiachi, shche i shatro ikhnie piane "
                                "znaiemo")
        actual_translation = word_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_uppercase_one_word(self):
        source_text = "ПаляНиця"
        expected_translation = "PaliaNytsia"
        actual_translation = word_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_several_words(self):
        source_text = "Слава Україні!"
        expected_translation = "Slava Ukraini!"
        actual_translation = word_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_latin_symbol(self):
        source_text = "Я програмую на Python ^_^"
        expected_translation = "Ya prohramuiu na Python ^_^"
        actual_translation = word_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
