from selenium import webdriver

# Define test cases and steps
# ...

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open the webpage containing the contact form
driver.get("https://www.example.com/contact")

# Enter valid data in all the mandatory fields
driver.find_element_by_name("fullname").send_keys("John Doe")
driver.find_element_by_name("email").send_keys("johndoe@example.com")
driver.find_element_by_name("mobile").send_keys("1234567890")

# Submit the form and verify that the form is submitted successfully
driver.find_element_by_name("submit").click()
assert "Thank you for contacting us!" in driver.page_source

# Test Case 2: Enter invalid data in the email field and verify that an error message is displayed
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("invalidemail")
assert "Please enter a valid email address." in driver.page_source

# Test Case 3: Enter invalid data in the mobile number field and verify that an error message is displayed
driver.find_element_by_name("mobile").clear()
driver.find_element_by_name("mobile").send_keys("invalidmobile")
assert "Please enter a valid mobile number." in driver.page_source

# Test Case 4: Verify that the "Company size" dropdown has at least one option to select
company_size = driver.find_element_by_name("company_size")
options = company_size.find_elements_by_tag_name("option")
assert len(options) > 1

# Test Case 5: Verify that the "Service" dropdown has at least one option to select
service = driver.find_element_by_name("service")
options = service.find_elements_by_tag_name("option")
assert len(options) > 1

# Test Case 6: Submit the form with optional fields filled and verify that the form is submitted successfully
driver.find_element_by_name("message").send_keys("This is a test message.")
driver.find_element_by_name("submit").click()
assert "Thank you for contacting us!" in driver.page_source

# Close the browser
driver.quit()
