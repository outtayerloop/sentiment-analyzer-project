from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from services import constants_service as ct


def get_sentiment(user_input: str) -> str:
    """
    Return a string containing the extracted sentiment from the input text.
    :param user_input: provided input text
    :return: the extracted sentiment (between "positive", "neutral" and "negative")
    """
    analyzer = SentimentIntensityAnalyzer()
    polarities = analyzer.polarity_scores(user_input)
    return __extract(polarities['compound'])


def __extract(compound: float) -> str:
    """
    Return a string containing the extracted sentiment from the provided float compound.
    :param compound: float sentiment score adjusted between -1 and 1
    :return: the extracted sentiment (between "positive", "neutral" and "negative")
    """
    if compound >= ct.get_threshold():
        return ct.get_positivity_label()
    elif compound <= -ct.get_threshold():
        return ct.get_negativity_label()
    else:
        return ct.get_neutrality_label()