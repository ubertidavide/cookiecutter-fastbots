import logging

from fastbots import Task, Bot, Page, Payload

from pages.search_page import SearchPage
from core import config


# Define a TestTask class, which is a subclass of the Task class
class TestTask(Task):

    # Main task code to be executed when running the script
    def run(self, bot: Bot) -> bool:
        # Log information about the current action
        logging.info('DO THINGS')

        # load all needed data in the pages interactions (es. login password loaded from a file using pandas)
        bot.payload.input_data = {'username': 'test', 'password': 'test', 'element_name': config.EXAMPLE_INPUT}

        # Open the search page, perform actions, and go forward
        page: Page = SearchPage(bot=bot)

        # For every page found, perform actions and go forward
        while page:
            page = page.forward()

        # For default, the task will succeed
        return True

    # Method executed on bot success, with its payload
    def on_success(self, payload: Payload):
        logging.info(f'SUCCESS {payload.downloads}')

    # Method executed on bot failure
    def on_failure(self, payload: Payload):
        logging.info(f'FAILED {payload.output_data}')

# Check if the script is executed as the main program
if __name__ == '__main__':
    # Start the above TestTask
    TestTask()()