class TestPhrase:
    def test_phrase(self):
        print("Please, inter the text <15 characters")
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"The length of the phrase is more than 15 characters or equal to 15 characters"
