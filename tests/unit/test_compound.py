from tests import fake_constants_service as fct
from services import extractor_service as ex


def test_compound_inferior_to_minus_threshold():
    """
    Test if the label of the negative sentiment will be the output
    when compound value is inferior to threshold * (-1).
    """
    expected_sentiment_label = fct.get_negativity_label()
    actual_label = ex.__extract(-fct.get_threshold() - 1)
    assert actual_label == expected_sentiment_label


def test_compound_equal_to_minus_threshold():
    """
    Test if the label of the negative sentiment will be the output
    when compound value is equal to threshold * (-1).
    """
    expected_sentiment_label = fct.get_negativity_label()
    actual_label = ex.__extract(-fct.get_threshold())
    assert actual_label == expected_sentiment_label


def test_compound_equal_to_threshold():
    """
    Test if the label of the positive sentiment will be the output
    when compound value is equal to threshold.
    """
    expected_sentiment_label = fct.get_positivity_label()
    actual_label = ex.__extract(fct.get_threshold())
    assert actual_label == expected_sentiment_label


def test_compound_superior_to_threshold():
    """
    Test if the label of the positive sentiment will be the output
    when compound value is superior to threshold.
    """
    expected_sentiment_label = fct.get_positivity_label()
    actual_label = ex.__extract(fct.get_threshold() + 1)
    assert actual_label == expected_sentiment_label


def test_compound_between_minus_threshold_and_threshold_both_excluded():
    """
    Test if the label of the neutral sentiment will be the output
    when compound value is strictly superior to threshold * (-1)
    and strictly inferior to threshold.
    """
    expected_sentiment_label = fct.get_neutrality_label()
    actual_label = ex.__extract(0)
    assert actual_label == expected_sentiment_label