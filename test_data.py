from dataclasses import dataclass
from datetime import datetime


@dataclass
class ParaBankTestData:
    first_name: str = "Bob"
    last_name: str = "Ross"
    address: str = "123 Street"
    city: str = "Montgomery"
    state: str = "Alabama"
    zip_code: str = "36101"
    phone_number: str = "1234567890"
    ssn: str = "123456789"
    username: str = "username"
    password: str = "12345"
    confirm: str = "12345"
    account_type: str = "1"
    loan_amount: str = "100.00"
    down_payment: str = "50.00"
    account_number: str = "13455"
    customer_id: str = "12434"
    initial_amount: str = "500.00"
    minimum_amount: str = "100.00"
    from_date: str = datetime.today().strftime("%m-%d-%Y")
    to_date: str = datetime.today().strftime("%m-%d-%Y")
