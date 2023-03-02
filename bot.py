import subprocess
import time

# function to load usr and pwd from file
'''def getCredentials():
    print("Where is allocated your credentials.txt: ")
    response = str(input().strip())
    response = "../../yehe.txt"                  # << delete in future
    with open(response) as fp:
        line = fp.readline()
        usr = str(line.strip())
        line = fp.readline()
        pwd = str(line.strip())
    return usr, pwd
'''

def downloadData(targetUsr):
    print("Downloading please wait...\n")
    subprocess.run(["instaloader", "--fast-update", targetUsr], capture_output=True)
    print("---Data downloaded successfully---")
    return ""


def downloadDataLogin(targetUsr):
    print("Enter username:")
    response = str(input().strip())
    response = "../../yehe.txt"                  # << delete in future
    print("Downloading please wait...\n")
    with open(response) as fp:                 # << ''
        line = fp.readline()                   # << ''
        usr = str(line.strip())                # << ''
    subprocess.run(["instaloader", "--login=" + usr, "--fast-update", targetUsr], capture_output=True)
    print("---Data downloaded successfully---")
    return usr


def instaloader(targetUsr):
    print("Choose an option for the download of target's pictures:")
    print("1.- Without login");
    print("2.- With login (needed if target's account is private and better photo quality)")
    resp = int(input().strip())
    if resp == 1:
        return downloadData(targetUsr)
    else:
        return downloadDataLogin(targetUsr)

def loadData(targetUsr):
    ret = []
    ls = subprocess.run(["ls", targetUsr], capture_output=True)
    grep = subprocess.run(["grep", ".jpg"], capture_output=True, input=ls.stdout)
    ret = grep.stdout.decode().split()
    grep = subprocess.run(["grep", ".txt"], capture_output=True, input=ls.stdout)
    ret += grep.stdout.decode().split()
    return ret


print("Select target account:")
targetUsr = str(input().strip())
targetUsr = "luisglez._"                   # << delete in future
firstRun = loadData(targetUsr)
print(firstRun)
loginUsr = instaloader(targetUsr)
print(loginUsr)
print(targetUsr)
