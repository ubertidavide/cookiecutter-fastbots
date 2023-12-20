import logging

from fastbots import Bot, Page, EC, WebElement, Keys

from pages.product_page import ProductPage


# Define a SearchPage class, which is a subclass of the Page class
class SearchPage(Page):

    # Constructor to initialize the SearchPage instance
    # The page_name is used in the locators file; default is 'search_page'
    def __init__(self, bot: Bot, page_name: str = 'search_page'):
        super().__init__(bot, page_name)

    # Define the forward method for navigating to the next page (ProductPage)
    def forward(self) -> ProductPage:
        # Log information about the current action
        logging.info('DO THINGS')

        # Use locators specified in the file for flexibility and less code changes
        search_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('search_locator')))

        # Enter a search query and submit (using the loaded data in the task)
        search_element.send_keys(self.bot.payload.input_data['element_name'])
        search_element.send_keys(Keys.ENTER)

        # Locate the product element and click on it
        #product_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('product_locator')))
        #product_element.click()

        # Continue the chain of interaction on the next page (ProductPage)
        return ProductPage(bot=self.bot)