# import_helper

With this module you can install packages right as you import them
This module is primarily if you want to send your script to someone who isnt familiar with pip like clients or friends.

## Usage
selenium is used as an example here

### Usage 1

> selenium = ih.imp("selenium")
> By = ih.imp_sub_lib(("selenium", "webdriver", "common", "by")).By
> webdriver = ih.imp_sub_lib(("selenium", "webdriver"))

### Usage 2

> try:
>     import selenium
>     from selenium import webdriver
>     from selenium.webdriver.common.by import By
>   except ImportError as e:
>     print(f"installing {e.name}")
>     ih.install(e.name)
>   else:
>     print("import successful")
>     break
