import os
commit = raw_input("commit contents: ")
echo = os.popen("cd ~/PycharmProjects/new_web&&git add .&&git commit -m '%s'&&git pull&&git push" % commit)
if "dev -> dev" in echo.readlines()[-1]:
    print("success")
