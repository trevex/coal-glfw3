from coal import CoalFile
from util import download, unzip

class GLFW3File(CoalFile):
    version = "3.1.2"
    zipfile = "glfw-%s.zip" % version
    url = "https://github.com/glfw/glfw/releases/download/%s/%s" % (version, zipfile)
    def prepare(self):
        download(self.url, self.zipfile)
        unzip(self.zipfile, 'src')
