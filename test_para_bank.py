import unittest

import requests
import xmltodict
from HTMLTestRunner import HTMLTestRunner

from para_bank import ParaBank
from test_data import ParaBankTestData


class TestParaBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.para_bank = ParaBank()
        cls.para_bank.admin_page.visit()
        cls.para_bank.admin_page.initialize_database(
            ParaBankTestData.initial_amount, ParaBankTestData.minimum_amount
        )

    @classmethod
    def tearDownClass(cls):
        cls.para_bank.quit()

    def setUp(self):
        self.clean_database()
        self.register()

    def test_registration(self):
        response_content = self.get_customer_personal_data(ParaBankTestData.customer_id)
        self.assertEqual(
            ParaBankTestData.first_name, response_content["customer"]["firstName"]
        )
        self.assertEqual(
            ParaBankTestData.last_name, response_content["customer"]["lastName"]
        )
        self.assertEqual(
            ParaBankTestData.address, response_content["customer"]["address"]["street"]
        )
        self.assertEqual(
            ParaBankTestData.city, response_content["customer"]["address"]["city"]
        )
        self.assertEqual(
            ParaBankTestData.state, response_content["customer"]["address"]["state"]
        )
        self.assertEqual(
            ParaBankTestData.zip_code,
            response_content["customer"]["address"]["zipCode"],
        )
        self.assertEqual(
            ParaBankTestData.phone_number, response_content["customer"]["phoneNumber"]
        )
        self.assertEqual(ParaBankTestData.ssn, response_content["customer"]["ssn"])

    def test_logout_and_login(self):
        self.para_bank.index_page.logout()
        self.para_bank.index_page.login(
            ParaBankTestData.username, ParaBankTestData.password
        )

    def test_clean_database(self):
        expected_state_code = 400
        self.clean_database()
        response = requests.get(
            f"http://parabank.parasoft.com/parabank/services/bank/customers/{ParaBankTestData.customer_id}"
        )
        self.assertEqual(response.status_code, expected_state_code)

    def test_open_savings_account(self):
        self.open_new_account()
        response_content = self.get_customer_account_data(ParaBankTestData.customer_id)
        self.assertEqual(
            self.para_bank.open_account_page.new_account_number,
            response_content["accounts"]["account"][1]["id"],
        )
        self.assertEqual("SAVINGS", response_content["accounts"]["account"][1]["type"])
        self.assertEqual(
            ParaBankTestData.minimum_amount,
            response_content["accounts"]["account"][1]["balance"],
        )

    def test_total_amount(self):
        self.para_bank.overview_page.visit()
        self.assertEqual(
            "$" + ParaBankTestData.initial_amount, self.para_bank.overview_page.total
        )

    def test_apply_for_loan(self):
        self.para_bank.request_load_page.visit()
        self.para_bank.request_load_page.request_a_load(
            ParaBankTestData.loan_amount,
            ParaBankTestData.down_payment,
            ParaBankTestData.account_number,
        )
        response_content = self.get_customer_account_data(ParaBankTestData.customer_id)
        self.assertEqual(
            self.para_bank.open_account_page.new_account_number,
            response_content["accounts"]["account"][1]["id"],
        )
        self.assertEqual("LOAN", response_content["accounts"]["account"][1]["type"])
        self.assertEqual(
            ParaBankTestData.loan_amount,
            response_content["accounts"]["account"][1]["balance"],
        )
        self.assertEqual(
            float(ParaBankTestData.initial_amount)
            - float(ParaBankTestData.down_payment),
            float(response_content["accounts"]["account"][0]["balance"]),
        )

    def test_get_transactions_for_date_range(self):
        self.open_new_account()
        print(ParaBankTestData.from_date, ParaBankTestData.to_date)
        self.para_bank.find_transactions_page.visit()
        self.para_bank.find_transactions_page.find_by_date_range(
            ParaBankTestData.from_date, ParaBankTestData.to_date
        )
        self.para_bank.find_transactions_page.click_first_transaction_result()
        response_content = self.get_account_transaction_data(
            ParaBankTestData.account_number
        )
        self.assertEqual(
            self.para_bank.find_transactions_page.transaction_id,
            response_content["transactions"]["transaction"]["id"],
        )

    def register(self) -> None:
        self.para_bank.register_page.visit()
        self.para_bank.register_page.sign_up(
            ParaBankTestData.first_name,
            ParaBankTestData.last_name,
            ParaBankTestData.address,
            ParaBankTestData.city,
            ParaBankTestData.state,
            ParaBankTestData.zip_code,
            ParaBankTestData.phone_number,
            ParaBankTestData.ssn,
            ParaBankTestData.username,
            ParaBankTestData.password,
            ParaBankTestData.confirm,
        )

    def clean_database(self) -> None:
        self.para_bank.admin_page.visit()
        self.para_bank.admin_page.clean()

    def get_customer_personal_data(self, customer_id: str) -> dict:
        response = requests.get(
            f"https://parabank.parasoft.com/parabank/services/bank/customers/{customer_id}"
        )
        return xmltodict.parse(response.content)

    def get_customer_account_data(self, customer_id: str) -> dict:
        response = requests.get(
            f"https://parabank.parasoft.com/parabank/services/bank/customers/{customer_id}/accounts"
        )
        return xmltodict.parse(response.content)

    def get_account_transaction_data(self, account_number: str) -> dict:
        response = requests.get(
            f"https://parabank.parasoft.com/parabank/services/bank/accounts/{account_number}/transactions"
        )
        return xmltodict.parse(response.content)

    def open_new_account(self) -> None:
        self.para_bank.open_account_page.visit()
        self.para_bank.open_account_page.open_new_account(
            ParaBankTestData.account_type, ParaBankTestData.account_number
        )


if __name__ == "__main__":
    unittest.main(
        testRunner=HTMLTestRunner(
            output="reports", report_name="para-bank-html-report", open_in_browser=True
        )
    )
