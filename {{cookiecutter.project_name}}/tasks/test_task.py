import logging

from fastbots import Task, Bot, Page

from pages.search_page import SearchPage
from core import config


# Define a TestTask class, which is a subclass of the Task class
class TestTask(Task):

    # Main task code to be executed when running the script
    def run(self, bot: Bot) -> bool:
        # Log information about the current action
        logging.info('DO THINGS')

        # load all needed data in the pages interactions (es. login password loaded from a file using pandas)
        bot.payload['input_data']['element_name'] = config.EXAMPLE_INPUT

        # Open the search page, perform actions, and go forward
        page: Page = SearchPage(bot=bot).forward()

        # For every page found, perform actions and go forward
        while page:
            page = page.forward()

        # For default, the task will succeed
        return True

    # Method executed on bot success, with its payload
    def on_success(self, payload):
        logging.info(f'SUCCESS {payload}')
    
    # Method executed on bot failure
    def on_failure(self, payload):
        logging.info(f'FAILED {payload}')