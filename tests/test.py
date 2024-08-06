import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions


options = ChromeOptions()
options.set_capability('sessionName', 'Amazon login')
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
    WebDriverWait(driver, 10)
    # find email textbox
    email_box = driver.find_element(By.NAME, "email")
    email_box.send_keys('crenzshaw3@gmail.com')
    # click continue
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()
    WebDriverWait(driver, 10)
    password_box = driver.find_element(By.ID, "ap_password")
    password_box.send_keys('Browserstack@321')
    #click signin
    signin_btn = driver.find_element(By.ID, "signInSubmit")
    signin_btn.click()

    WebDriverWait(driver, 30)
    
    signout_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@class="nav-item-signout"]')))

    print(signout_btn)
    if signout_btn:
        # Set the status of test as 'passed' if signout btn appears
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Homepage opens, Signout button appears"}}')
    else:
        # Set the status of test as 'failed' if signout btn not appears
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Login failed, Signout button not appears"}}')
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
finally:
    # Stop the driver
    driver.quit()


















