class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Len of phrase should be less than 15"
