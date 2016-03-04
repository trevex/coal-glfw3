from coal import CoalFile
from util import download, unzip, default_cmake_build, cp, pkg_config, Info, abspath
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
        cp('src/glfw-%s/include' % self.version, 'include')
        cp('build/src/*.a', 'libs/')
        cp('build/src/*.lib', 'libs/')
        cp('build/src/*.pc', 'libs/pkgconfig/')
    def info(self, generator):
        generator.add_library(pkg_config('glfw3', path='libs/pkgconfig'))
        generator.add_link_dir('libs/')
        generator.add_include_dir('include/')
