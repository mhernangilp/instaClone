import subprocess

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

def downloadData():
    print("Select target account:")
    targetUsr = str(input().strip())
    targetUsr = "luisglez._"                   # << delete in future
    print("Downloading please wait...\n")
    subprocess.run(["instaloader", "--fast-update", targetUsr], capture_output=True)
    print("---Data downloaded successfully---")
    return targetUsr


def downloadDataLogin():
    print("Where is your downloadUser.txt:")
    response = str(input().strip())
    response = "../../yehe.txt"                  # << delete in future
    print("Select target account:")
    targetUsr = str(input().strip())
    targetUsr = "luisglez._"                   # << delete in future
    print("Downloading please wait...\n")
    with open(response) as fp:
        line = fp.readline()
        usr = str(line.strip())
    subprocess.run(["instaloader", "--login=" + usr, "--fast-update", targetUsr], capture_output=True)
    print("---Data downloaded successfully---")
    return usr, targetUsr


def instaloader():
    print("Choose an option for the download of target's pictures:")
    print("1.- Without login");
    print("2.- With login (needed if target's account is private and better photo quality)")
    resp = int(input().strip())
    if resp == 1:
        return "", downloadData()
    else:
        return downloadDataLogin()


usrLoginDir, targetUsr = instaloader()
print(usrLoginDir)
print(targetUsr)
