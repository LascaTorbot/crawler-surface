#!env/usr/bin
from sys import path
import sys
import urllib.request
import urllib.error


class A:

    next_page = ""

    def __init__(self, crawler):

        self.directory = crawler.split('.')
        self.directory = '/'.join(self.directory)
        path.append(path[0] + '/' + self.directory)

        crawler = crawler.split('.')
        crawler = crawler[-1]

        c = crawler.title()

        crawler = __import__(crawler)
        self.crawler = getattr(crawler, c)

    def get_download_links(self, counter):

        link = self.crawler.url

        content = self.get_content(link)

        if content is not None:

            next_page = self.crawler.next_page(self.crawler, content, counter)

            links = self.crawler.get_links(self.crawler, content)

            # for link in links:
            #
            #     content = self.get_content(link.info_link)
            #
            #     if content is not None:
            #
            #         # "True" means: total number of downloads
            #         link.downloads_total, downloads_last_week = self.crawler.get_downloads(self.crawler, link.info_link,
            #                                                                                content, True)
            #
            #         if downloads_last_week is not None:
            #
            #             link.downloads_last_week = downloads_last_week
            #
            #         link.version = self.crawler.get_version(self.crawler, self.get_content(link.info_link))
            #
            #     else:
            #
            #         f = open("info_link.No.Conten.txt", "a")
            #
            #         f.write(str(link.info_link)+"\n")
            #
            #         f.close()
            #
            #         return None, next_page

            return links, next_page

        else:

            return None, None

    @staticmethod
    def get_content(url):

        try:

            response = urllib.request.urlopen(url)

        except urllib.error.URLError:

            f = open("URLError.a.py.txt", "a")

            f.write(str(url)+"\n")

            f.close()

            return None

        data = response.read()

        try:

            text = data.decode("utf-8")

        except ValueError:

            text = data.decode("iso-8859-1")

        return text
