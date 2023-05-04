# Automated Test for Contact Form

This is an automated test script for testing the contact form on https://www.example.com/contact. The test script uses the Selenium Python library to interact with the contact form and verify that it is working correctly.

## Requirements

- Python 3
- Selenium library for Python
- Firefox web browser
- Geckodriver executable

## Installation

1. Install Python 3 on your system if it is not already installed. You can download Python from the official website: https://www.python.org/downloads/

2. Install the Selenium library for Python by running the following command in a terminal:

   ```
   pip install selenium
   ```

3. Download and install the Firefox web browser on your system if it is not already installed. You can download Firefox from the official website: https://www.mozilla.org/en-US/firefox/new/

4. Download the Geckodriver executable from the Mozilla Github repository: https://github.com/mozilla/geckodriver/releases. Extract the executable to a directory that is included in your system's PATH environment variable.

## Usage

1. Clone this repository or download the source code to your local machine.

2. Open a terminal and navigate to the directory containing the source code.

3. Run the following command to execute the test script:

   ```
   python test_contact_form.py
   ```

4. The script will launch Firefox and navigate to the contact form page. It will then enter valid data in all the mandatory fields, submit the form, and verify that the form is submitted successfully. It will then execute the additional test cases that have been defined, and output the results to the console.

5. After the script has completed running, you can view the detailed test results in the console output. Additionally, the script will create a screenshot of the contact form page after each test case has been executed, which can be useful for debugging.

## Defined Test Cases

1. Enter valid data in all the mandatory fields, submit the form, and verify that the form is submitted successfully.

2. Enter invalid data in the email field and verify that an error message is displayed.

3. Enter invalid data in the mobile number field and verify that an error message is displayed.

4. Verify that the "Company size" dropdown has at least one option to select.

5. Verify that the "Service" dropdown has at least one option to select.

6. Submit the form with optional fields filled and verify that the form is submitted successfully.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. We welcome any contributions or feedback that can help to improve the automated testing of this contact form.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
