class Program:

    link = ""
    version = ""
    downloads_total = 0
    downloads_last_week = 0
    info_link = ""

    def __init__(self, link, info_link, version, downloads_total, downloads_last_week):

        self.link = link
        self.info_link = info_link
        self.version = version
        self.downloads_total = downloads_total
        self.downloads_last_week = downloads_last_week