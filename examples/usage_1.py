
import urllib.request
url = "https://raw.githubusercontent.com/Jakob2007/import_helper/master/import_helper.py"
response = urllib.request.urlopen(url)
module_code = response.read().decode("utf-8")
exec(module_code)

Helper.get_pip()

By = Helper.imp_sub_lib(("selenium", "webdriver", "common", "by")).By
webdriver = Helper.imp_sub_lib(("selenium", "webdriver"))
geckodriver_autoinstaller = Helper.imp("geckodriver_autoinstaller")

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()

url = "https://whatismyipaddress.com/"
driver.get(url)

elem = driver.find_element(By.ID, "ipv4")

print(elem.text)

driver.quit()
