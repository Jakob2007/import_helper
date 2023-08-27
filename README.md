# import_helper

With this module you can install packages right as you import them
This module is primarily if you want to send your script to someone who isnt familiar with pip like clients or friends.

## Usage

To use this project directly in your code:
```
import urllib.request
url = "https://raw.githubusercontent.com/Jakob2007/import_helper/master/import_helper.py"
response = urllib.request.urlopen(url)
module_code = response.read().decode("utf-8")
exec(module_code)
```
One-liner:
```
import urllib.request
exec(urllib.request.urlopen("https://raw.githubusercontent.com/Jakob2007/import_helper/master/import_helper.py").read().decode("utf-8"))
```

To automaticially install pip if it is not use:
```
Helper.get_pip()
``` 

(selenium is used as an example here)

### Usage 1
```
selenium = Helper.imp("selenium")
By = Helper.imp_sub_lib(("selenium", "webdriver", "common", "by")).By
webdriver = Helper.imp_sub_lib(("selenium", "webdriver"))
```

### Usage 2
```
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
  except ImportError as e:
    print(f"installing {e.name}")
    Helper.install(e.name)
  else:
    print("import successful")
    break
```