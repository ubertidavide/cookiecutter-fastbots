import logging

from fastbots import Task, Bot, Page

from pages import SearchPage


class TestTask(Task):

    # retried n times
    def run(self, bot: Bot) -> bool:
        logging.info('DO THINGS')

        page: Page = SearchPage(bot).forward()

        while page:
            page = page.forward()

        return True

    # success part
    def on_success(self, payload):
        logging.info(f'SUCCESS {payload}')
    
    # failure part
    def on_failure(self, payload):
        logging.info(f'FAILED {payload}')