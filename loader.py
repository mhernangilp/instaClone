import subprocess


class loader:
    def setTargetUsrAndMode(self):
        print("Select target account:")
        self.targetUsr = str(input().strip())
        print("Choose an option for the download of target's pictures:")
        print("1.- Without login")
        print("2.- With login (needed if target's account is private and better photo quality)")
        mode = int(input().strip())
        if mode == 2:
            print("Enter username:")
            self.loginUsr = str(input().strip())
        else:
            self.loginUsr = None

    def downloadData(self, data):
        if self.loginUsr is None:
            shell = ["instaloader", "--fast-update", self.targetUsr]
        else:
            shell = ["instaloader", "--login=" + self.loginUsr, "--fast-update", self.targetUsr]
        if data == 1:
            shell.insert(1, "--stories")
        try:
            subprocess.run(shell, capture_output=True)
        except Exception as e:
            print(e)
        print("---Data downloaded successfully---")

    def loadPosts(self):
        ret = {}
        ls = subprocess.run(["ls", self.targetUsr], capture_output=True)
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

    def loadStories(self):
        ret = []
        ls = subprocess.run(["ls", self.targetUsr], capture_output=True)
        grep = subprocess.run(["grep", "-e", ".jpg", "-e", ".mp4"], capture_output=True, input=ls.stdout)
        jpg = grep.stdout.decode().split()
        for photo in jpg:
            if "profile_pic" not in photo:
                ret.append(photo)
        return ret

    def updateData(self):
        firstRun = self.loadPosts()
        print("\nDownloading posts...\n")
        self.downloadData(0)
        secndRun = self.loadPosts()
        updatedData = [secndRun.copy(), []]
        for date in secndRun:
            if date in firstRun:
                del updatedData[0][date]
        firstRun = self.loadStories()
        print("\nDownloading stories...\n")
        self.downloadData(1)
        secndRun = self.loadStories()
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
        self.updatedData = updatedData
