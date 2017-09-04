#!env/usr/bin
import re
import html
import urllib.request
import urllib.error
import sys
from Program import Program


class Cnet:

    # Define as variaveis de configuracao do cnet

    # Url de inicio
    url = "http://download.cnet.com/s/software/windows/?page=92"

    page_regex = re.compile("http://download\.cnet\.com/[A-Za-z0-9-_./]+/?\"\s")

    # Regex para capturar o link de download do programa
    download_regex = re.compile("http:\/\/files\.downloadnow(-[0-9]+)?\.com/s/[A-Za-z0-9_\-/?=.&]+")
    #download_regex = re.compile("http:\/\/dw\.cbsi\.com\/redir\?ttag=[A-Za-z0-9\.\-_\/&=\?%@:\n]+\"\s")
    #"http://dw.cbsi.com/redir?ttag=download_now_button_click&lop=link&ptid=3000&pagetype=product_detail&astid=2&edid=3&
    # siteid=4&destUrl=http%3A%2F%2Fdownload.cnet.com%2FCCleaner%2F3001-18512_4-10315544.html%3FhasJs%3Dn&onid=18512&oid
    # =3000-18512_4-10315544&rsid=cbsidownloadcomsite&sl=en&sc=us&topicguid=utilities%2Fmaintenance&topicbrcrm=&pid=1566
    # 7649&mfgid=6300943&merid=6300943&ctype=dm&cval=NONE&ltype=dl_dlnow&spi=47e78c42dbf690a6c7588111e9493ce0&devicetype
    # =desktop&pguid=0681e926d31192686fc13259&viewguid=hcAMT92s2mgto@Yl6Erl-1lSogqd5IZ7p0hD"

    # Regex para capturar o link para a pagina com detalhes do programa
    info_regex = re.compile("http:\/\/download\.cnet\.com\/[A-Za-z0-9\.\-_\/&=\?%@:\n]+\"\sdata")

    # Regex para capturar o link para a proxima pagina
    next_regex = re.compile("href=\"/s/software/windows/\?page=[0-9]+(&amp;sort=most-popular)?")

    # Regex para capturar a versao do programa
    version_regex = re.compile("<div\sclass=\"product\-landing\-quick\-specs\-row\-content\">.+</div>")

    # Regex para capturar o numero total/na ultima semana de downloads
    downloads_regex = re.compile("<div\sclass=\"product-landing-quick-specs-row-content\">[0-9,]+</div>")

    def get_links(self, text):

        # download_links = []
        #
        # found = self.download_regex.findall(text)
        # #found2 = self.download2_regex.findall(text)
        #
        # info_links = self.get_info_links(self, text)
        #
        # #print(found2)
        #
        # #sys.exit()
        #
        # counter = 0
        #
        # for url in found:
        #
        #     # Configura o link de download
        #     url = url[13:-1]
        #
        #     #links.append(Program(url, self.get_version(self, text), downloads[counter]))
        #     download_links.append(Program(url, info_links[counter], None, 0, 0))
        #
        #     counter += 1
        #
        # counter = 0

        # for url in found2:
        #
        #     # Configura o link de download
        #     url = url[13:-1]
        #
        #     url = "http://www.reporting-download.com/download/?appid=" + url[42:]
        #
        #     #links.append(Program(url, self.get_version(self, text), downloads[counter]))
        #     download_links.append(Program(url, info_links[counter], None, 0, 0))
        #
        #     counter += 1

        links = []

        found = self.page_regex.findall(text)
        #_, last_week = self.get_downloads(self, "", text, False)

        counter = 0

        for url in found:

            l = self.create_links_list(self, url[:-2])  # Remove space and " chars

            if l is not None:
                l = html.unescape(l)

            links.append(Program(l, url[:-8], "", 0, None))#last_week[counter]))

            counter += 1

        return links

    def next_page(self, text, counter):

        print("Counter: " + str(counter))

        next_regex = re.compile("href=\"/s/software/windows/\?page=" + str(counter) + "(&amp;sort=most-popular)?")

        found = next_regex.search(text)

        try:

            start = found.start()
            end = found.end()

            start += 6
            # end -= 10

            link = "http://download.cnet.com" + text[start:end]
            self.url = "http://download.cnet.com" + text[start:end]

            #print(text)

        except:

            #print(text)

            link = None

        return link

    def get_info_links(self, text):

        found = self.info_regex.findall(text)

        counter = 0

        while counter < len(found):

            found[counter] = found[counter][29:-2]

            counter += 1


        return found

    def get_downloads(self, link, text, flag):

        found = self.downloads_regex.findall(text)

        if found is not None:

            return found[0][53:-6], found[1][53:-6]

        else:

            return None

    def get_version(self, text):

        found = self.version_regex.search(text)

        try:

            start = found.start()
            end = found.end()

            start += 53
            end -= 6

            version = text[start:end]

        except:

            version = None

        return version

    def create_links_list(self, url):

        text = self.get_resource(self, url)

        if text is not None:

            found = self.download_regex.search(text)

            if found is None:

                f = open("FAILED_TO_FIND_LINK", "a")

                f.write(url + "\n\n")

                f.close()

                link = None

                # # Save error
                #
                # found = None  # self.download_regex_2.search(text)
                #
                # if found is None:
                #
                #     return None
                #
                # else:
                #
                #     link = found.group()
                #
                #     return link

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
