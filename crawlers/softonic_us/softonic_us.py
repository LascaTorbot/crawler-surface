#!env/usr/bin

import re
import html
import urllib.request
import urllib.error

from Program import Program


class Softonic_Us:

    # Define as variaveis de configuracao do softonic

    c = 285

    # Url de inicio
    url = "http://en.softonic.com/windows/top-downloads/284"

    # Regex para capturar o link para a proxima pagina
    # next_regex = re.compile("http://en\.softonic\.com/windows/top\-downloads/%s" % str(c))

    # Regex para capturar todos os links para as PAGINAS dos programas
    page_regex = re.compile("http://[A-Za-z0-9\-]+\.en\.softonic\.com/download")

    # Regex para capturar o link de download
    download_regex = re.compile("http://gsf\-cf\.softonic\.com/[A-Za-z0-9]+/[A-Za-z0-9]+/[A-Za-z0-9]+/[A-Za-z0-9\._"
                                "~\?=&\-;]+")
    download_regex_2 = re.compile("http://[A-Za-z0-9]+\.en\.softonic\.com/universaldownloader\-launch")


    # Regex para a versao do programa
    # version_regex = re.compile("<dd><span>[Vv0-9\.]+</span><spanclass=\"sub-info\">")
    version_regex = re.compile("<span>[Vv0-9\.]+</span>")

    # Regex para capturar o numero de downloads na ultima semana
    last_week_downloads_regex = re.compile("<dlclass=\"list-program-downloads\"><dt>[0-9,]+</dt><dd>Lastweek</dd></dl>")

    # Regex para capturar o numero total de downloads
    total_downloads_regex = re.compile("<dd\sclass=\"value\"\sid=\"overlay-total-downloads\">[0-9,]+</dd>")

    def get_links(self, text):

        links = []

        found = self.page_regex.findall(text)
        _, last_week = self.get_downloads(self, "", text, False)

        counter = 0

        for url in found:

            l = self.create_links_list(self, url)

            if l is not None:

                l = html.unescape(l)

            links.append(Program(l, url[:-8], "", 0, last_week[counter]))

            counter += 1

        return links

    def get_version(self, text):

        text = "".join(text.split('\n'))
        text = "".join(text.split())

        found = self.version_regex.search(text)

        try:

            start = found.start()
            end = found.end()

            start += 6
            end -= 7

            version = text[start:end]

        except:

            version = None

        return version

    def get_downloads(self, link, text, flag):

        week = None
        total = None

        if not flag:

            text = "".join(text.split('\n'))
            text = "".join(text.split())

            # Last Week
            week = self.last_week_downloads_regex.findall(text)

            counter = 0

            while counter < len(week):

                week[counter] = week[counter][38:-27]

                counter += 1

        else:

            #Total number of downloads
            #http://utorrent.en.softonic.com/download_chart_ajax
            link += "download_chart_ajax"

            text = self.get_resource(self, link)

            found_total = self.total_downloads_regex.search(text)

            try:

                start = found_total.start()
                end = found_total.end()

                start += 47
                end -= 5

                total = text[start:end]

            except:

                total = None

        return total, week

    def next_page(self, text):

        next_regex = re.compile("http://en\.softonic\.com/windows/top\-downloads/%s" % str(self.c))

        found = next_regex.search(text)

        try:

            link = found.group()

            self.url = link

            self.c += 1

        except:

            link = None

        return link

    def create_links_list(self, url):

        text = self.get_resource(self, url)

        if text is not None:

            found = self.download_regex.search(text)

            if found is None:

                found = self.download_regex_2.search(text)

                if found is None:

                    return None

                else:

                    link = found.group()

                    return link

            else:

                link = found.group()

        else:

            link = None

        return link

    def get_resource(self, link):

        try:

            response = urllib.request.urlopen(link)

        except urllib.error.URLError:

            f = open("urllib.error.URLError.txt", "a")

            f.write(link + "\n\n")

            f.close()

            return None

        data = response.read()

        text = data.decode("utf-8")

        return text