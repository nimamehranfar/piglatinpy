from src.error import PigLatinError


class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        vowels = ('a', 'e', 'i', 'o', 'u')
        if self.phrase == "":
            return "nil"
        elif self.phrase[0].lower() in vowels:
            if self.phrase[-1] == "y":
                return self.phrase + "nay"
            elif self.phrase[-1] in vowels:
                return self.phrase + "yay"
            else:
                return self.phrase + "ay"
