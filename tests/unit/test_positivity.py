from services import extractor_service as ex
from tests import fake_constants_service as fct

expected_sentiment = fct.get_positivity_label()


def test_basic_positive_sentence_without_punctuation():
    """
    Test if basic positive input
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'This is a wonderful book'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_positive_sentence_with_punctuation_emphasis():
    """
    Test if basic positive input with an exclamation point
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'This is a wonderful book!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_positive_sentence_with_capitalization_emphasis():
    """
    Test if basic positive input with the word with the most impact capitalized
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'This is a WONDERFUL book'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_booster_words():
    """
    Test if a positive input with positive booster words
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'A really good, great book'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_booster_words_with_capitalization_emphasis():
    """
    Test if a positive input with capitalized positive booster words
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'A REALLY good, GREAT book'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_slang_without_punctuation_emphasis_handling():
    """
    Test if a positive input with slang
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Today is gr8'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_slang_with_punctuation_emphasis_handling():
    """
    Test if a positive input with slang and an exclamation point
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Today is gr8!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_slang_with_punctuation_and_capitalization_emphasis_handling():
    """
    Test if a positive input with capitalized slang and an exclamation point
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Today is GR8!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_sentence_with_time_notion_without_punctuation():
    """
    Test if a positive input with time influence marker
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Sentiment analysis has always been good'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_sentence_with_time_notion_with_punctuation_emphasis():
    """
    Test if a positive input with time influence marker and an exclamation point
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Sentiment analysis has always been good!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_sentence_with_time_notion_with_capitalization_emphasis():
    """
    Test if a positive input with capitalized time influence marker
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'Sentiment analysis has ALWAYS BEEN GOOD!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_positive_sentence_without_punctuation():
    """
    Test if a qualified positive input
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'The book was kind of good'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_positive_sentence_with_punctuation_emphasis():
    """
    Test if a qualified positive input and an exclamation point
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'The book was kind of good!'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_positive_sentence_with_capitalization_emphasis():
    """
    Test if a capitalized qualified positive input with
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'The book was KIND OF good'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_mixed_negation_sentence():
    """
    Test if a mixed positive negation input
    makes the extractor output the positive sentiment label
    """
    positive_sentence = 'The plot was boring, but the characters are great and the dialog is not bad'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positive_emoticons():
    """
    Test if the use of positive emoticons
    makes the extractor output the positive sentiment label
    """
    positive_sentence = ':) and :D'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment


def test_happy_emoticon_input_return_positive():
    """
    Test if happy emoticon input
    makes the extractor output the positive sentiment label
    """
    positive_sentence = '😃'
    extracted_sentiment = ex.get_sentiment(positive_sentence)
    assert extracted_sentiment == expected_sentiment