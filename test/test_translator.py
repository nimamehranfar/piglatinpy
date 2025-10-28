from unittest import TestCase
from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_starting_vowel_ending_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_starting_vowel_ending_vowel(self):
        translator = PigLatinTranslator("apple")
        translation = translator.translate()
        self.assertEqual("appleyay", translation)

    def test_translate_starting_vowel_ending_consonant(self):
        translator = PigLatinTranslator("ask")
        translation = translator.translate()
        self.assertEqual("askay", translation)

