import logging

from fastbots import Bot, Page, EC, WebElement


class ProductPage(Page):

    def __init__(self, bot: Bot, page_name: str = 'product_page'):
        super().__init__(bot, page_name)

    def forward(self) -> None:
        logging.info('DO THINGS')

        # using the locators specified in the file give more flexibility and less code changes
        name_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('name_locator')))
        # store data in the payload section, useful when i need to retrieve data on success
        self.bot.payload['result'] = name_element.text

        return None