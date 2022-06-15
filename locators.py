from dataclasses import dataclass


@dataclass
class IndexPageLocators:
    username: str = "input[name='username']"
    password: str = "input[name='password']"
    login: str = "input[value='Log In']"
    logout: str = "a[href='/parabank/logout.htm']"


@dataclass
class RegisterPageLocators:
    first_name: str = "[id='customer.firstName']"
    last_name: str = "[id='customer.lastName']"
    address: str = "[id='customer.address.street']"
    city: str = "[id='customer.address.city']"
    state: str = "[id='customer.address.state']"
    zip_code: str = "[id='customer.address.zipCode']"
    phone_number: str = "[id='customer.phoneNumber']"
    ssn: str = "[id='customer.ssn']"
    username: str = "[id='customer.username']"
    password: str = "[id='customer.password']"
    confirm: str = "[id='repeatedPassword']"
    register: str = "input[value='Register']"


@dataclass
class AdminPageLocators:
    initialize: str = "button[value='INIT']"
    clean: str = "button[value='CLEAN']"
    data_access_mode: str = "#accessMode4"
    initial_balance: str = "#initialBalance"
    minimum_balance: str = "#minimumBalance"
    submit: str = "input[value='Submit']"


@dataclass
class OpenAccountPageLocators:
    open_new_account: str = "input[value='Open New Account']"
    account_type: str = "#type"
    from_account: str = "#fromAccountId"
    new_account_id: str = "#newAccountId"


@dataclass
class RequestLoanPageLocators:
    loan_amount: str = "#amount"
    down_payment: str = "#downPayment"
    from_account: str = "#fromAccountId"
    apply_now: str = "input[value='Apply Now']"
    new_account_id: str = "#newAccountId"


@dataclass
class OverviewPageLocators:
    total: str = "#accountTable > tbody > tr:nth-child(2) > td:nth-child(2) > b"


@dataclass
class FindTransactionsPageLocators:
    from_date: str = "input[id='criteria.fromDate']"
    to_date: str = "input[id='criteria.toDate']"
    find_transactions: str = (
        "#rightPanel > div > div > form > div:nth-child(13) > button"
    )
    first_transaction_result: str = "a[href*='/parabank/transaction.htm']"
    transaction_id: str = (
        "#rightPanel > table > tbody > tr:nth-child(1) > td:nth-child(2)"
    )
