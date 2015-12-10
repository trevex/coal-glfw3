from coal import CoalFile
from util import download, unzip, default_cmake_build
from os import path

class GLFW3File(CoalFile):
    version = "3.1.2"
    zipfile = "glfw-%s.zip" % version
    url = "https://github.com/glfw/glfw/releases/download/%s/%s" % (version, zipfile)
    exports = ["include", "libs"]

    def prepare(self):
        download(self.url, self.zipfile)
        unzip(self.zipfile, 'src')
    def build(self):
        default_cmake_build('src/glfw-%s' % self.version, 'build/')
    def package(self):
        self.cp('src/glfw-%s/include' % self.version, 'include')
        self.cp('build/src/*.a', 'libs/')
        self.cp('build/src/*.lib', 'libs/')
        self.cp('build/src/*.pc', 'libs/pkg_config/')
    def info(self):
        pass
