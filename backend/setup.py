import os
if os.path.exists("echonet"):
	os.system('python -m pip install wget')
	os.system('python -m pip install pydicom')
else :
	print("Repository  already loaded")
