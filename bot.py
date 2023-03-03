import subprocess
import sys
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

def downloadData(targetUsr, mode):
    print("Downloading please wait...\n")
    shell = ["instaloader", "--fast-update", targetUsr]
    if mode == 1:
        shell.insert(1, "--stories")
    try:
        subprocess.run(shell, capture_output=True)
    except Exception as e:
        print(e)
        sys.exit()
    print("---Data downloaded successfully---")
    return ""


def downloadDataLogin(targetUsr, mode):
    print("Enter username:")
    response = str(input().strip())
    response = "../../yehe.txt"                  # << delete in future
    print("Downloading please wait...\n")
    with open(response) as fp:                 # << ''
        line = fp.readline()                   # << ''
        usr = str(line.strip())                # << ''
    shell = ["instaloader", "--login=" + usr, "--fast-update", targetUsr]
    if mode == 1:
        shell.insert(1, "--stories")
    try:
        subprocess.run(shell, capture_output=True)
    except Exception as e:
        print(e)
        sys.exit()
    print("---Data downloaded successfully---")
    return usr


def instaloader(targetUsr, mode):
    print("Choose an option for the download of target's pictures:")
    print("1.- Without login")
    print("2.- With login (needed if target's account is private and better photo quality)")
    resp = int(input().strip())
    if resp == 1:
        return downloadData(targetUsr, mode)
    else:
        return downloadDataLogin(targetUsr, mode)

def loadPosts(targetUsr):
    ret = {}
    ls = subprocess.run(["ls", targetUsr], capture_output=True)
    grep = subprocess.run(["grep", "-e", ".jpg", "-e", ".mp4"], capture_output=True, input=ls.stdout)
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


def loadStories(targetUsr):
    ret = []
    ls = subprocess.run(["ls", targetUsr], capture_output=True)
    grep = subprocess.run(["grep", "-e", ".jpg", "-e", ".mp4"], capture_output=True, input=ls.stdout)
    jpg = grep.stdout.decode().split()
    for photo in jpg:
        if "profile_pic" not in photo:
            ret.append(photo)
    return ret

def updateDataFirstCall():
    print("Select target account:")
    targetUsr = str(input().strip())
    targetUsr = "luisglez._"                   # << delete in future
    firstRun = loadPosts(targetUsr)
    print("\n.:Download posts:.\n")
    loginUsr = instaloader(targetUsr, 0)
    secndRun = loadPosts(targetUsr)
    updatedData = [secndRun.copy(), []]
    for date in secndRun:
        if date in firstRun:
            del updatedData[0][date]
    firstRun = loadStories(targetUsr)
    print("\n.:Download stories.:\n")
    loginUsr = instaloader(targetUsr, 1)
    secndRun = loadStories(targetUsr)
    updatedData[1] = secndRun.copy()
    for date in secndRun:
        if date in firstRun:
            updatedData[1].remove(date)
    for jpg in updatedData[1]:
        if ".jpg" in jpg:
            date1 = jpg.replace(".jpg", "")
            for mp4 in updatedData[1]:
                if ".mp4" in mp4:
                    date2 = mp4.replace(".mp4", "")
                    if date1 == date2:
                        updatedData[1].remove(jpg)
    return updatedData, loginUsr, targetUsr


updatedData, loginUsr, targetUsr = updateDataFirstCall()
print(updatedData)
print(loginUsr)
print(targetUsr)
