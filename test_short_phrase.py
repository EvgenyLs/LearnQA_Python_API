class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        length = 15
        assert len(phrase) < length, "The phrase too long"
