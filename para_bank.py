from selenium.webdriver.chrome.webdriver import WebDriver

from element_handler import ElementHandler
from pages import (
    IndexPage,
    AdminPage,
    RegisterPage,
    OpenAccountPage,
    OverviewPage,
    RequestLoanPage,
    FindTransactionsPage,
)


class ParaBank:
    def __init__(self, driver: WebDriver, element_handler: ElementHandler):
        self._driver = driver
        self._element_handler = element_handler
        self.index_page = IndexPage(self._driver, self._element_handler)
        self.admin_page = AdminPage(self._driver, self._element_handler)
        self.register_page = RegisterPage(self._driver, self._element_handler)
        self.open_account_page = OpenAccountPage(self._driver, self._element_handler)
        self.overview_page = OverviewPage(self._driver, self._element_handler)
        self.request_load_page = RequestLoanPage(self._driver, self._element_handler)
        self.find_transactions_page = FindTransactionsPage(
            self._driver, self._element_handler
        )
