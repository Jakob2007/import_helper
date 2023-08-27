
import urllib.request
url = "https://raw.githubusercontent.com/Jakob2007/import_helper/master/import_helper.py"
response = urllib.request.urlopen(url)
module_code = response.read().decode("utf-8")
exec(module_code)

print(module_code)
print(Helper, dir(Helper))

Helper.get_pip()

while True:
	try:
		from selenium import webdriver
		from selenium.webdriver.common.by import By
		import geckodriver_autoinstaller
	except ImportError as e:
		print(f"installing {e.name}")
		Helper.install(e.name)
	else:
		break

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()

url = "https://whatismyipaddress.com/"
driver.get(url)

elem = driver.find_element(By.ID, "ipv4")

print(elem.text)

driver.quit()
