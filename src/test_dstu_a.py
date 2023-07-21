import unittest
from ua_latin import text_translate_dstu_a


class TestWordTranslate(unittest.TestCase):
    def test_city_name(self):
        source_text = ("Вінниця Запоріжжя")
        expected_translation = ("Vinnycja Zaporižžja")
        actual_translation = text_translate_dstu_a(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_uppercase_one_word(self):
        source_text = "ЛуГанськ"
        expected_translation = "LuĞansjk"
        actual_translation = text_translate_dstu_a(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_j_before_aeu(self):
        source_text = "нехай"
        expected_translation = "nexaj’"
        actual_translation = text_translate_dstu_a(source_text)

        self.assertEqual(actual_translation, expected_translation)

    def test_consonant_before_j(self):
        source_text = "зйомка"
        expected_translation = "z’jomka"
        actual_translation = text_translate_dstu_a(source_text)

        self.assertEqual(actual_translation, expected_translation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
