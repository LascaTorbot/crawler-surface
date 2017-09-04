#!usr/bin/env
from os import listdir
from os.path import isdir, join

import sys
import a
import time

import re

from download import Download
from db import DB


counter = 1
path = "crawlers"

crawlers = [f for f in listdir(path) if isdir(join(path, f))]

for option in crawlers:

    print("%d - %s" % (counter, option))
    counter += 1

#option = int(input(""))

option = 1

a = a.A(path + "." + crawlers[option-1])

next_page = True

number = 0

counter = 91

while next_page is not None and number <= 2500:

    s = DB.select()

    print("[+] Gathering links...")

    links, next_page = a.get_download_links(counter+2)

    print("Next page: " + str(next_page))

    if links is not None:

        print("[+] Downloading list of programs...")

        for link in links:

            flag = True

            #print(link.link)
            # print(link.version)
            # print(link.downloads_total)
            # print(link.downloads_last_week)
            # print(link.info_link)
            
            # if link.link is None:
            #
            #     link.link = "None"
            #
            #     f = open("log.txt", "a")
            #
            #     f.write(str(link.version)+"\n")
            #     f.write(str(link.downloads_total)+"\n")
            #     f.write(str(link.downloads_last_week)+"\n")
            #     f.write(str(link.info_link)+"\n\n")
            #
            #     f.close()
            #
            #     flag = False
            
            if flag:

                h, name, path, save = Download.download(crawlers[option-1], link.link)

                # if h is not False and save is not False:
                #
                #     print("SUCESS")
                #
                #     # TODO -> PROBABLE INFINIT LOOP... MUST CHECK WHY!
                #
                #     data = []
                #     # name, download_link, download_date, origin_website, total_downloads, last_week_downloads, version, hash
                #     data = (name, link.link, time.strftime("%d/%m/%Y - %H:%M:%S"), crawlers[option-1], link.downloads_total,
                #             link.downloads_last_week, link.version, h, path)
                #
                #     DB.insert(data)
                #
                #     number += 1
                #
                # else:
                #
                #     print("File already exists")

        counter += 1


sys.exit("Done :)")
