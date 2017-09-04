import hashlib


class Hash:

    BLOCKSIZE = 65536
    hasher = hashlib.md5()

    def md5hash(self, file_name):

        with open(file_name, 'rb') as afile:

            buf = afile.read(self.BLOCKSIZE)

            while len(buf) > 0:

                self.hasher.update(buf)
                buf = afile.read(self.BLOCKSIZE)

        return self.hasher.hexdigest()
