from services import extractor_service as ex
from tests import fake_constants_service as fct

expected_sentiment = fct.get_negativity_label()


def test_basic_negative_sentence_without_punctuation():
    """
    Test if basic negative input
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'This is a terrible book'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_negative_sentence_with_punctuation_emphasis():
    """
    Test if basic negative input with an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'This is a terrible book!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_negative_sentence_with_capitalization_emphasis():
    """
    Test if basic negative input with the word with the most impact capitalized
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'This is a TERRIBLE book'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_booster_words():
    """
    Test if a negative input with negative booster words
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'A really bad, horrible book'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_booster_words_with_capitalization_emphasis():
    """
    Test if a negative input with capitalized negative booster words
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'A REALLY bad, HORRIBLE book'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_slang_without_punctuation_emphasis_handling():
    """
    Test if a negative input with slang
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Today sux'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_slang_with_punctuation_emphasis_handling():
    """
    Test if a negative input with slang and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Today sux!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_slang_with_punctuation_and_capitalization_emphasis_handling():
    """
    Test if a negative input with capitalized slang and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Today SUX!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_insult_without_punctuation():
    """
    Test if a negative input with an insult
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Most automated sentiment analysis tools are shit'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_insult_with_punctuation_emphasis():
    """
    Test if a negative input with an insult and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Most automated sentiment analysis tools are shit!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_insult_with_capitalization_emphasis():
    """
    Test if a negative input with a capitalzed insult and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Most automated sentiment analysis tools are SHIT'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_sentence_with_time_notion_without_punctuation():
    """
    Test if a negative input with time influence marker
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Sentiment analysis has never been good'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_sentence_with_time_notion_with_punctuation_emphasis():
    """
    Test if a negative input with time influence marker and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Sentiment analysis has never been good!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_sentence_with_time_notion_with_capitalization_emphasis():
    """
    Test if a negative input with capitalized time influence marker
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'Sentiment analysis has NEVER BEEN GOOD!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_negative_sentence_without_punctuation():
    """
    Test if a qualified negative input
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'The book was kind of bad'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_negative_sentence_with_punctuation_emphasis():
    """
    Test if a qualified negative input and an exclamation point
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'The book was kind of bad!'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_negative_sentence_with_capitalization_emphasis():
    """
    Test if a capitalized qualified negative input with
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'The book was KIND OF bad'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_mixed_negation_sentence():
    """
    Test if a mixed negative negation input
    makes the extractor output the negative sentiment label
    """
    negative_sentence = 'The plot was good, but the characters are uncompelling and the dialog is not great'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_negative_emoticons():
    """
    Test if the use of negative emoticons
    makes the extractor output the negative sentiment label
    """
    negative_sentence = ':( and :\'('
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment


def test_sad_emoticon_input_return_negative():
    """
    Test if sad emoticon input
    makes the extractor output the negative sentiment label
    """
    negative_sentence = '☹️'
    extracted_sentiment = ex.get_sentiment(negative_sentence)
    assert extracted_sentiment == expected_sentiment

