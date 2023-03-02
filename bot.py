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
    ret = {}
    ls = subprocess.run(["ls", targetUsr], capture_output=True)
    grep = subprocess.run(["grep", ".jpg"], capture_output=True, input=ls.stdout)
    jpg = grep.stdout.decode().split()
    for photo in jpg:
        if "profile_pic" in photo:
            jpg.remove(photo)
    grep = subprocess.run(["grep", ".txt"], capture_output=True, input=ls.stdout)
    txt = grep.stdout.decode().split()
    for photo in jpg:
        date = photo.split('_')
        date = date[0] + '_' + date[1]
        if date not in ret:
            ret[date] = [[], ""]
        ret[date][0].append(photo)
    for caption in txt:
        date = caption.split('_')
        date = date[0] + '_' + date[1]
        if date in ret:
            ret[date][1] = caption
    return ret


def updateDataFirstCall():
    print("Select target account:")
    targetUsr = str(input().strip())
    targetUsr = "luisglez._"                   # << delete in future
    firstRun = loadData(targetUsr)
    loginUsr = instaloader(targetUsr)
    secndRun = loadData(targetUsr)
    updatedData = secndRun.copy()
    for date in secndRun:
        if date in firstRun:
            del updatedData[date]
    return updatedData, loginUsr, targetUsr


updatedData, loginUsr, targetUsr = updateDataFirstCall()
print(updatedData)
print(loginUsr)
print(targetUsr)
