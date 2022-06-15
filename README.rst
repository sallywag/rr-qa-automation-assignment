rr-qa-automation-assignment
===========================

How to Install
--------------

After installing Python 3, run the following command from the rr-qa-automation-assignment folder to create a virtual environment:

``python -m venv my-environment-name``

To activate the virtual environment (may vary depending on platform):

``source my-environment-name/bin/activate``

To install the dependencies:

``pip install -r requirements.txt``

Chrome driver is included in the project folder for simplicity.

How to Run
----------

From the rr-qa-automation-assignment folder,

To run the tests with HTML reporting, run the file directly:

``python test_para_bank.py``

To run the tests with console output, use the unittest runner:

``python -m unittest -v test_para_bank.py``

Technologies Used
-----------------

This project uses Selenium to interact with the ParaBank site. 
Requests are handled with the Python Requests library.
The xmltodict library is used to convert XML responses to Python dictionaries, to make them easy to work with.
The HTMLTestRunner library is used for the HTML test reports.
The unittest testing framework is used to organize and run the test cases.

To improve readability, I used the Black code formatter and mypy to format my code and add type hints.

Framework and Design
--------------------

I kept the project structure flat given the scope of the assignment.

All Selenium commands are wrapped in the ElementHandler class. A good framework should wrap
its dependencies in an easy to use interface, so you don't have to interact with the 3rd party code directly.

Page objects make use of the ElementHandler class to interact with the pages themselves. 

The ParaBank class encapsulates the page objects so you can import and use them through one class.

The ParaBank class is imported and used to interact with the pages in the unit tests.

All locators for a given page are stored in their own class.

Data for tests is stored in one class for simplicity.

Possible Improvements
---------------------

1. A more explicit folder structure can be created to house the different parts of the project to better organize things for a production environment.
   Tests can go in a tests folder, test data and locators can go in a data folder, utilities like the element handler 
   and possibly a requests handler can go in a utilities folder, pages can go in a dedicated pages folder, and so forth.

2. Data interfaces can be created to enforce a standard in case we want multiple varations of the same test data for different tests.

3. You can furthur break down the Page class into smaller classes to better represent a webpage. A Widget class can be created to represent an element with a locator.
   Various Input classes can be created to represent the different input types you can interact with. A Component class can be created to house groups of related inputs (as in the regestration form).
   A Page can then contain components. This can lead to a very clean interface as follow: ``registration_page.registration_form.first_name = "Value"``

4. The test cases in the TestParaBank class can be split up into their own classes and files to improve readability and reduce coupling.

5. The criteria for test passes and failures can be improved. Right now I'm using a mix of frontend validation and API validation. What constitues a pass and a fail is something
   that should be discussed with the wider team.

6. Unit tests can be added for the various ElementHandler class methods, which can be run against a static test site.

7. Eventually, we can support writing tests in a custom YAML based syntax, if we want to make test creation more accessibile for non technical people.

8. Test results reporting to a program like TestRail could be useful.

9. Custom waits to remove generic timeouts (like I have in the open_new_account method of the OpenAccountPage class).

10. General improvments could include support for multiple browsers, headless test running, improved logging, etc.

CI/CD
-----

The tests in this project could be run every time an update is pushed to a merge request. To ensure basic functionality is not broken by any changes.
These can also be run whenever code is merged into a development or a UAT environment. The tests should only be run after things like code building, linting,
type checking, security & accessibility checking, and unit tests have passed.
