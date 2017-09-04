__author__ = 'MASTER'

import os
import glob

file = glob.glob(os.path.join("/home", "analyst", "Downloads", "cnet", "*", "*"))

print(len(file))

# for _, a, files in os.walk(os.path.join("/home", "analyst", "Downloads", "cnet")):
#
#     print(zip(a, files))
    #for d, f in zip(a, files):

        #print(d+"/"+str(f))

    #for file in files:

        # f = open("downloaded.txt", "r")
        #
        # downloaded = f.read()
        #
        # f.close()
        #
        # list_downloaded = downloaded.split("\n")

        # if file not in list_downloaded:
        #
        #     path = os.path.join("/home", "analyst", "Downloads", "analysis")
        #
        #     #os.makedirs(path)
        #     # Launch the VM
        #     os.system("python3 /home/analyst/Behemot/Control/submit.py -dst %s -src %s -vm 1 -name %s", % (path,)
        #
        #     f = open("downloaded.txt", "a")
        #
        #     f.write(file + "\n")
        #
        #     f.close()
