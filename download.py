import os
import urllib.request
import urllib.parse
import urllib.error
import hash
import shutil
import re
import glob
import time
import sys


class Download:
    @staticmethod
    def download(source, link):

        try:

            a = urllib.request.urlopen(link)

        except:

            return False, None, None, False

        p = urllib.parse.parse_qs(link)

        try:

            file_name = p["fileName"][0]

        except KeyError:

            file_name = p["filename"][0]

        except:

            file_name = "Unknown"

        c = False

        while not c:

            try:

                tmp_name, h = urllib.request.urlretrieve(link)

                c = True

            except ConnectionResetError:

                print("ConnectionResetError")

                time.sleep(1)

            except urllib.error.ContentTooShortError:

                print("ContentTooShortError")

                f = open("urllib.error.ContentTooShortError.txt", "a")

                f.write(str(link) + "\n\n")

                f.close()

                return False, None, None, False

        # Downloads the file
        try:

            try:

                tmp_name, h = urllib.request.urlretrieve(link)

            except urllib.error.URLError:

                print("URLError")
                return False, None, None, False

            h = hash.Hash()

            file_name_md5 = h.md5hash(tmp_name)

            path = None

            if os.path.exists(os.path.join(os.getcwd(), "Downloads", source, file_name_md5)) is False:
                path = os.path.join(os.getcwd(), "Downloads", source, file_name_md5)
                os.makedirs(path)

            # Checks if the file alredy exists
            if not glob.glob(str(os.getcwd()) + "/Downloads/cnet/*/" + str(file_name_md5)):

                if os.path.getsize(tmp_name) > 128000000:

                    save = False

                    print("FALSE SIZE")

                    destination = None

                    os.remove(tmp_name)

                    if path:

                        os.rmdir(path)

                else:

                    save = True

                    destination = os.path.join(os.getcwd(), "Downloads", source, file_name_md5, file_name)

                    shutil.move(tmp_name, destination)

                    if os.path.exists(tmp_name) is True:

                        os.remove(tmp_name)

            else:

                save = False

                print("FALSE")

                destination = None

                os.remove(tmp_name)

                if path:

                    os.rmdir(path)

            return file_name_md5, None, None, None  # file_name, destination, save

        except urllib.error.HTTPError as e:

            print("FAILED: " + str(e.reason))

            return False, None, None, False
