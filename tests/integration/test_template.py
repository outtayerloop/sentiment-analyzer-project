from selenium import webdriver
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element

from tests import fake_constants_service as fct
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')

# Chrome driver service initialization
chrome_driver_service = Service(ChromeDriverManager().install())

# Chrome driver initialization
driver = webdriver.Chrome(service=chrome_driver_service)


def test_template_title():
    """
    Test if sending a regular request to the index endpoint route
    returns a template with the expected title
    """
    expected_template_title = 'Sentiment analyzer'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    template_title = driver.title
    assert template_title == expected_template_title


def test_initial_input_area_content():
    """
    Test if sending a regular request to the index endpoint route
    returns a template with an empty input area.
    """
    expected_initial_input_area_content = ''
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    initial_input_area_content = driver.find_element(by=By.ID, value='sentence').text
    assert initial_input_area_content == expected_initial_input_area_content


def test_initial_result_area_content():
    """
    Test if sending a regular request to the index endpoint route
    returns a template with an empty result area.
    """
    expected_initial_result_area_content = ''
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    initial_result_area_content = driver.find_element(by=By.ID, value='result').text
    assert initial_result_area_content == expected_initial_result_area_content


def test_initial_error_message_opacity():
    """
    Test if sending a regular request to the index endpoint route
    returns a template with an invisible error message.
    """
    expected_initial_error_message_opacity = '0'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    initial_error_message_opacity = driver.find_element(by=By.ID, value='error-message')\
        .value_of_css_property('opacity')
    assert initial_error_message_opacity == expected_initial_error_message_opacity


def test_typing_content_key_does_not_trigger_error_message():
    """
    Test if sending a regular request to the index endpoint route and typing a content key different than Back Space
    returns a template with an invisible error message.
    """
    expected_error_message_opacity = '0'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys('x')
    error_message_opacity = driver.find_element(by=By.ID, value='error-message').value_of_css_property('opacity')
    assert error_message_opacity == expected_error_message_opacity


def test_typing_back_space_key_in_initially_empty_input_area_triggers_error_message():
    """
    Test if sending a regular request to the index endpoint route, typing a content key different than Back Space
    then erasing it
    returns a template with a visible error message.
    """
    expected_error_message_opacity = '1'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.BACK_SPACE)
    error_message_opacity = driver.find_element(by=By.ID, value='error-message').value_of_css_property('opacity')
    assert error_message_opacity == expected_error_message_opacity


def test_typing_content_key_and_then_back_space_key_triggers_error_message():
    """
    Test if sending a regular request to the index endpoint route, typing a content key different than Back Space
    then erasing it
    returns a template with a visible error message.
    """
    expected_error_message_opacity = '1'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys('x')
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.BACK_SPACE)
    error_message_opacity = driver.find_element(by=By.ID, value='error-message').value_of_css_property('opacity')
    assert error_message_opacity == expected_error_message_opacity


def test_typing_enter_key_hides_error_message():
    """
    Test if sending a regular request to the index endpoint route, typing a content key different than Back Space
    then erasing it then typing ENTER key
    returns a template with an invisible error message.
    """
    expected_error_message_opacity = '0'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys('x')
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.BACK_SPACE)
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.ENTER)
    error_message_opacity = driver.find_element(by=By.ID, value='error-message').value_of_css_property('opacity')
    assert error_message_opacity == expected_error_message_opacity


def test_typing_space_key_hides_error_message():
    """
    Test if sending a regular request to the index endpoint route, typing a content key different than Back Space
    then erasing it then typing SPACE key
    returns a template with an invisible error message.
    """
    expected_error_message_opacity = '0'
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys('x')
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.BACK_SPACE)
    driver.find_element(by=By.ID, value='sentence').send_keys(Keys.SPACE)
    error_message_opacity = driver.find_element(by=By.ID, value='error-message').value_of_css_property('opacity')
    assert error_message_opacity == expected_error_message_opacity


def test_positive_input_shows_positive_sentiment_label_in_result_area():
    """
    Test if sending a regular request to the index endpoint route, typing a positive sentence then clicking
    on the submit button
    returns a template with the positive sentiment label in the result area.
    """
    expected_result_area_content = fct.get_positivity_label()
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    positive_sentence = 'Hey :)'
    wait_driver = WebDriverWait(driver, 10)  # time out of 10 seconds.
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys(positive_sentence)
    driver.find_element(by=By.ID, value='submit-btn').click()
    wait_driver.until(text_to_be_present_in_element((By.ID, 'result'), expected_result_area_content))


def test_neutral_input_shows_neutral_sentiment_label_in_result_area():
    """
    Test if sending a regular request to the index endpoint route, typing a neutral sentence then clicking
    on the submit button
    returns a template with the neutral sentiment label in the result area.
    """
    expected_result_area_content = fct.get_neutrality_label()
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    wait_driver = WebDriverWait(driver, 10)  # time out of 10 seconds.
    neutral_sentence = 'Hey'
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys(neutral_sentence)
    driver.find_element(by=By.ID, value='submit-btn').click()
    wait_driver.until(text_to_be_present_in_element((By.ID, 'result'), expected_result_area_content))


def test_negative_input_shows_negative_sentiment_label_in_result_area():
    """
    Test if sending a regular request to the index endpoint route, typing a negative sentence then clicking
    on the submit button
    returns a template with the negative sentiment label in the result area.
    """
    expected_result_area_content = fct.get_negativity_label()
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    wait_driver = WebDriverWait(driver, 10)  # time out of 10 seconds.
    negative_sentence = 'Hey :('
    driver.get(url)
    driver.find_element(by=By.ID, value='sentence').send_keys(negative_sentence)
    driver.find_element(by=By.ID, value='submit-btn').click()
    wait_driver.until(text_to_be_present_in_element((By.ID, 'result'), expected_result_area_content))
    driver.quit()  # Must only be put at the end of the last test function of this file, otherwise will throw error.





