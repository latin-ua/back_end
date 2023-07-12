import unittest
from ua_latin import text_translate


class TestWordTranslate(unittest.TestCase):
    def test_all_letters(self):
        source_text = ("Жебракують філософи при ґанку церкви в Гадячі, "
                       "ще й шатро їхнє п'яне знаємо")
        expected_translation = ("Zhebrakuiut filosofy pry ganku tserkvy v "
                                "Hadiachi, shche y shatro yikhnie piane "
                                "znaiemo")
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_uppercase_one_word(self):
        source_text = "ПаляНиця"
        expected_translation = "PaliaNytsia"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_several_words(self):
        source_text = "Слава Україні!"
        expected_translation = "Slava Ukraini!"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_latin_symbol(self):
        source_text = "Я програмую на Python ^_^"
        expected_translation = "Ya prohramuiu na Python ^_^"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_Yu_symbol(self):
        source_text = "юю"
        expected_translation = "yuiu"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_Ya_symbol(self):
        source_text = "яя"
        expected_translation = "yaia"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_Y_symbol(self):
        source_text = "йой"
        expected_translation = "yoi"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_Yi_symbol(self):
        source_text = "її"
        expected_translation = "yii"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_word_with_Ye_symbol(self):
        source_text = "єє"
        expected_translation = "yeie"
        actual_translation = text_translate(source_text)

        self.assertEqual(actual_translation, expected_translation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
