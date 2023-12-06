import logging

from fastbots import Bot, Page, EC, WebElement


# Define a ProductPage class, which is a subclass of the Page class
class ProductPage(Page):

    # Constructor to initialize the ProductPage instance
    # The page_name is used in the locators file; default is 'product_page'
    def __init__(self, bot: Bot, page_name: str = 'product_page'): 
        super().__init__(bot, page_name)

    # Define the forward method for navigating to the next page
    def forward(self) -> None:
        # Log information about the current action
        logging.info('DO THINGS')

        # Use locators specified in the file for flexibility and less code changes
        # name_element: WebElement = self.bot.driver.find_element(*self.__locator__('name_locator'))
        name_element: WebElement = self.bot.wait.until(EC.element_to_be_clickable(self.__locator__('name_locator')))
        
        # Store data in the payload section for future retrieval on success
        self.bot.payload['result'] = name_element.text

        # example of downloading the product png images and rename it (check download folder settings)
        # name_element.click() for example on element download button
        # self.bot.wait_downloaded_file_path("png", new_name_file=self.bot.payload['data']['element_name'])

        # End the chain of page interactions
        return None