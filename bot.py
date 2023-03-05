from loader import loader
from instagrapi import Client


loader = loader()
loader.setTargetUsrAndMode()
loader.updateData()
print(loader.updatedData)
