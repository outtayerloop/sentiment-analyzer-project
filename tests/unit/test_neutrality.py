from services import extractor_service as ex
from tests import fake_constants_service as fct

expected_sentiment = fct.get_neutrality_label()


def test_basic_neutral_sentence_without_punctuation():
    """
    Test if basic neutral input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'This is a book'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_neutral_sentence_with_punctuation_emphasis():
    """
    Test if basic neutral input with an exclamation point
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'This is a book!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_basic_neutral_sentence_with_capitalization_emphasis():
    """
    Test if basic neutral input with the word with the most impact capitalized
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'This is a BOOK'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_booster_words():
    """
    Test if a neutral input with neutral booster words
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'A real book, indeed a book'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_booster_words_with_capitalization_emphasis():
    """
    Test if a neutral input with capitalized neutral booster words
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'A REAL book, INDEED a book'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_slang_without_punctuation_emphasis_handling():
    """
    Test if a neutral input with slang
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Today is today afaik'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_slang_with_punctuation_emphasis_handling():
    """
    Test if a neutral input with slang and an exclamation point
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Today is today afaik!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_slang_with_punctuation_and_capitalization_emphasis_handling():
    """
    Test if a neutral input with capitalized slang and an exclamation point
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Today is TODAY AFAIK!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_sentence_with_time_notion_without_punctuation():
    """
    Test if a neutral input with time influence marker
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Sentiment analysis has been developped for some years'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_sentence_with_time_notion_with_punctuation_emphasis():
    """
    Test if a neutral input with time influence marker and an exclamation point
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Sentiment analysis has been developped for some years!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_sentence_with_time_notion_with_capitalization_emphasis():
    """
    Test if a neutral input with capitalized time influence marker
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Sentiment analysis has been developped FOR SOME YEARS!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_neutral_sentence_without_punctuation():
    """
    Test if a qualified neutral input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'The book was neither a chair, neither a table'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_neutral_sentence_with_punctuation_emphasis():
    """
    Test if a qualified neutral input and an exclamation point
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'The book was neither a chair, neither a table!'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_qualified_neutral_sentence_with_capitalization_emphasis():
    """
    Test if a capitalized qualified neutral input with
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'The book was NEITHER a chair, NEITHER a table'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_mixed_negation_sentence():
    """
    Test if a mixed neutral negation input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'The plot was a plot, but the characters are fictive and the dialog is a written script'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_neutral_emoticons():
    """
    Test if the use of neutral emoticons
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = '\'-\' and :x'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_positivity_negativity_cancel_each_other():
    """
    Test if the use of negative and positive emoticons
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'Hello :( :)'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_empty_sentence():
    """
    Test if an empty input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = ''
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment

def test_rubbish_input_return_neutral():
    """
    Test if rubbish input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = 'hdjkslfjdfkjdlf'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment


def test_only_number_input_return_neutral():
    """
    Test if only number input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = '123456'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment

def test_only_special_caracter_input_return_neutral():
    """
    Test if only special caracter input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = '????!!!!###'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment

def test_neutral_emoticon_input_return_neutral():
    """
    Test if one happy emoticon and sad emoticon input
    makes the extractor output the neutral sentiment label
    """
    neutral_sentence = '😃☹️'
    extracted_sentiment = ex.get_sentiment(neutral_sentence)
    assert extracted_sentiment == expected_sentiment