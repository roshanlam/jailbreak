import urllib.request
import socket
import time 
import tarfile, gzip

class Utils:
    def upload(r, name, data):
        soc = r.get_socket()
        soc.sendall("\tWrite %s %s\n"%(name.endcode(), len(data)))
        soc.sendall(data)
        r.read_until("\tiload>")
    def download(file):
        files_to_download = []
        with urrlib.request.urlopen("https://github.com/roshanlam/jailbreak/raw/master/" + file) as url:
            with open(file, "wb+") as f:
                f.write(url.read())
    def extractFromTar(tar, file):
        with tarfile.open(tar, mode="r:gz") as f:
            return f.extractfile(file).read()
    def doesItExist(files):
        files_that_need_to_exist = []
        if not os.path.exists(files_that_need_to_exist):
            download()