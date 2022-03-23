from services import extractor_service as ex
from tests import fake_constants_service as fct

import pandas as pd
from sklearn.metrics import accuracy_score


def test_min_80_percent_accuracy():
    """
    Test whether the model accuracy on the test dataset is superior or equal to 80 percent.
    """
    accuracy_threshold = 0.8
    df = pd.read_csv('./tests/unit/data/accuracy_test_data.csv')
    expected_sentiments = __get_expected_sentiments(df)
    sentences = df['text_snippet']
    extracted_sentiments = sentences.apply(lambda sentence: ex.get_sentiment(sentence))
    accuracy = accuracy_score(expected_sentiments, extracted_sentiments)
    assert accuracy >= accuracy_threshold


def __get_expected_sentiments(df: pd.DataFrame) -> pd.Series:
    """
    Return a pandas Series containing the expected sentiments from each row of the provided DataFrame.
    :param df: the pandas DataFrame against which will be tested the sentiment extractor's accuracy
    :return: a pandas Series containing the expected sentiments from each row of the provided DataFrame.
    """
    return df['mean_sentiment_rating'].apply(lambda rating: __get_sentiment_from_rating(rating))


def __get_sentiment_from_rating(rating: float) -> str:
    """
    Return a string containing the extracted sentiment from the provided float rating.
    :param rating: float sentiment score adjusted between -1 and 1
    :return: the extracted sentiment (between "positive", "neutral" and "negative"
    """
    if rating >= fct.get_threshold():
        return fct.get_positivity_label()
    elif rating <= -fct.get_threshold():
        return fct.get_negativity_label()
    else:
        return fct.get_neutrality_label()