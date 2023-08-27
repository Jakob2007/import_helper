
import platform
import subprocess
import urllib.request

pl = platform.platform().lower()
if "windows" in pl:
	pip_command = "pip"
elif "macos" in pl or "linux" in pl:
	py_version = '.'.join(platform.python_version().split('.')[:2])
	pip_command = f"pip{py_version}"


class Helper:
	def get_pip() -> None:
		
		result = subprocess.run(pip_command, capture_output=True)
		
		if result.returncode == 0:
			return
		
		print("pip not installed; installing ...")

		url = "https://raw.githubusercontent.com/pypa/get-pip/main/public/get-pip.py"
		response = urllib.request.urlopen(url)
		module_code = response.read().decode("utf-8")
		exec(module_code)

		print("pip installed successfully")

	# install library
	def install(name: str, logging=False) -> None:
		command = (pip_command, "install", name)
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
			print(f"installing {e.name}")
			Helper.install(e.name, logging=(logging==2))
			
			if logging >= 1: print("retry importing")
			lib = __import__(lib_name)

		if logging == 1: print("done")

		return lib

	# installs the library using pip if neccessary and returns the lowest subclass e.g. imp_sub_lib(("selenium", "webdriver", "common", "by")) -> by
	def imp_sub_lib(lib_path: tuple, logging=0) -> object:
		Helper.imp(lib_path[0], logging)

		node = __import__('.'.join(lib_path))

		for node_name in lib_path[1:]:
			node = getattr(node, node_name)

		return node

if __name__ == "__main__":
	print("Thanks for supporting my work\n - Jakob Sauer \033[4mFiverr.com/jakob_2\033[0m")
	