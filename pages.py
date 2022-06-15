from abc import ABC, abstractmethod

from selenium.webdriver.chrome.webdriver import WebDriver

from element_handler import ElementHandler
from locators import (
    IndexPageLocators,
    RegisterPageLocators,
    AdminPageLocators,
    OpenAccountPageLocators,
    RequestLoanPageLocators,
    OverviewPageLocators,
    FindTransactionsPageLocators,
)


class Page(ABC):
    @property
    @abstractmethod
    def url(self):
        pass

    def __init__(self, driver: WebDriver, element_handler: ElementHandler):
        self._driver = driver
        self._element_handler = element_handler

    def visit(self) -> None:
        self._driver.get(self.url)


class IndexPage(Page):

    url = "https://parabank.parasoft.com/parabank/index.htm"

    def login(self, username: str, password: str) -> None:
        self._element_handler.send_keys_to_element(IndexPageLocators.username, username)
        self._element_handler.send_keys_to_element(IndexPageLocators.password, password)
        self._element_handler.click_element(IndexPageLocators.login)

    def logout(self) -> None:
        self._element_handler.click_element(IndexPageLocators.logout)


class RegisterPage(Page):

    url = "https://parabank.parasoft.com/parabank/register.htm"

    def sign_up(
        self,
        first_name: str,
        last_name: str,
        address: str,
        city: str,
        state: str,
        zip_code: str,
        phone_number: str,
        ssn: str,
        username: str,
        password: str,
        confirm: str,
    ) -> None:
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.first_name, first_name
        )
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.last_name, last_name
        )
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.address, address
        )
        self._element_handler.send_keys_to_element(RegisterPageLocators.city, city)
        self._element_handler.send_keys_to_element(RegisterPageLocators.state, state)
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.zip_code, zip_code
        )
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.phone_number, phone_number
        )
        self._element_handler.send_keys_to_element(RegisterPageLocators.ssn, ssn)
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.username, username
        )
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.password, password
        )
        self._element_handler.send_keys_to_element(
            RegisterPageLocators.confirm, confirm
        )
        self._element_handler.click_element(RegisterPageLocators.register)


class AdminPage(Page):

    url = "https://parabank.parasoft.com/parabank/admin.htm"

    def clean(self) -> None:
        self._element_handler.click_element(AdminPageLocators.clean)

    def initialize_database(self, initial_balance: str, minimum_balance: str) -> None:
        self._element_handler.click_element(AdminPageLocators.initialize)
        self._element_handler.click_element(AdminPageLocators.data_access_mode)
        self._element_handler.send_keys_to_element(
            AdminPageLocators.initial_balance, initial_balance
        )
        self._element_handler.send_keys_to_element(
            AdminPageLocators.minimum_balance, minimum_balance
        )
        self._element_handler.click_element(AdminPageLocators.submit)


class OpenAccountPage(Page):

    url = "https://parabank.parasoft.com/parabank/openaccount.htm"

    def open_new_account(self, account_type: str, from_account: str) -> None:
        self._element_handler.select_value_from_element(
            OpenAccountPageLocators.account_type, account_type
        )
        self._element_handler.wait_for_timeout()
        self._element_handler.select_value_from_element(
            OpenAccountPageLocators.from_account, from_account
        )
        self._element_handler.click_element(OpenAccountPageLocators.open_new_account)

    @property
    def new_account_number(self) -> None:
        return self._element_handler.get_text_from_element(
            OpenAccountPageLocators.new_account_id
        )


class OverviewPage(Page):

    url = "https://parabank.parasoft.com/parabank/overview.htm"

    @property
    def total(self) -> str:
        return self._element_handler.get_text_from_element(OverviewPageLocators.total)


class RequestLoanPage(Page):

    url = "https://parabank.parasoft.com/parabank/requestloan.htm"

    def request_a_load(
        self, loan_amount: str, down_payment: str, from_account: str
    ) -> None:
        self._element_handler.send_keys_to_element(
            RequestLoanPageLocators.loan_amount, loan_amount
        )
        self._element_handler.send_keys_to_element(
            RequestLoanPageLocators.down_payment, down_payment
        )
        self._element_handler.select_value_from_element(
            RequestLoanPageLocators.from_account, from_account
        )
        self._element_handler.click_element(RequestLoanPageLocators.apply_now)

    @property
    def new_account_number(self) -> None:
        return self._element_handler.get_text_from_element(
            RequestLoanPageLocators.new_account_id
        )


class FindTransactionsPage(Page):

    url = "https://parabank.parasoft.com/parabank/findtrans.htm"

    def find_by_date_range(self, from_date: str, to_date: str) -> None:
        self._element_handler.send_keys_to_element(
            FindTransactionsPageLocators.from_date, from_date
        )
        self._element_handler.send_keys_to_element(
            FindTransactionsPageLocators.to_date, to_date
        )
        self._element_handler.click_element(
            FindTransactionsPageLocators.find_transactions
        )

    def click_first_transaction_result(self) -> None:
        self._element_handler.click_element(
            FindTransactionsPageLocators.first_transaction_result
        )

    @property
    def transaction_id(self) -> str:
        return self._element_handler.get_text_from_element(
            FindTransactionsPageLocators.transaction_id
        )
