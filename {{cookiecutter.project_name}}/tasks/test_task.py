import logging

from fastbots import Task, Bot, Page

from pages.search_page import SearchPage


class TestTask(Task):

    # main task code
    def run(self, bot: Bot) -> bool:
        logging.info('DO THINGS')

        # open the search page do things and go forward
        page: Page = SearchPage(bot=bot).forward()

        # for every page founded do things and go forward
        while page:
            page = page.forward()

        # for default it will succeed
        return True

    # method executed on bot success, with it's payload
    def on_success(self, payload):
        logging.info(f'SUCCESS {payload}')
    
    # method executed on bot failure
    def on_failure(self, payload):
        logging.info(f'FAILED {payload}')