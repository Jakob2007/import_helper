
import subprocess
import platform

# install library
def install(name: str, logging: bool) -> None:
	pl = platform.platform().lower()
	if "windows" in pl:
		command = ("pip", "install", name)
	elif "macos" in pl or "linux" in pl:
		py_version = '.'.join(platform.python_version().split('.')[:2])
		command = (f"pip{py_version}", "install", name)
	else:
		raise Exception(f"Unsupported System: {pl}")
	
	result = subprocess.run(command, capture_output=True)

	if result.returncode != 0:
		raise Exception(
			f"""
Could not install library '{name}' exit status: {result.returncode}
{result.stdout}
{result.stderr}
"""
		)

	if logging:
		print(result.stdout)

# installs the library using pip if neccessary and returns it
def imp(lib_name: str, logging=0) -> None:
	try: 
		if logging >= 1: print(f"start importing {lib_name}")
		lib = __import__(lib_name)
	except ImportError as e:
		if logging >= 1: print(f"failed; installing {e.name}")
		install(e.name, logging=(logging==2))
		
		if logging >= 1: print("retry importing")
		lib = __import__(lib_name)

	if logging == 1: print("done")

	return lib

# installs the library using pip if neccessary and returns the lowest subclass e.g. imp_sub_lib(("selenium", "webdriver", "common", "by")) -> by
def imp_sub_lib(lib_path: tuple, logging=0) -> object:
	imp(lib_path[0], logging)

	node = __import__('.'.join(lib_path))

	for node_name in lib_path[1:]:
		node = getattr(node, node_name)

	return node

if __name__ == "__main__":
	print("Thanks for using my Script\n - Jakob Sauer \033[4mFiverr.com/jakob_2\033[0m")
	
	# test:
	if True:
		try:
			from selenium.webdriver.common.by import By
		except ImportError as e:
			print("befor automatic install:")
			print(e)
		By = imp_sub_lib(("selenium", "webdriver", "common", "by")).By
		print(By.XPATH)
		print("test successful")