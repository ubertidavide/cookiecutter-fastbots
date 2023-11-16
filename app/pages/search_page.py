import logging

from fastbots import Bot, Page, EC, WebElement, Keys

from pages import ProductPage


class SearchPage(Page):

    def __init__(self, bot: Bot, page_name: str = 'search_page'):
        super().__init__(bot, page_name)

    def forward(self) -> ProductPage:
        logging.info('DO THINGS')

        # using the locators specified in the file give more flexibility and less code changes
        search_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('search_locator')))
        search_element.send_keys('Selenium with Python Simplified For Beginners')
        search_element.send_keys(Keys.ENTER)

        # product_element: WebElement = self.bot.driver.find_element(*self.__locator__('product_locator'))
        product_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('product_locator')))
        product_element.click()

        return ProductPage(bot=self.bot)