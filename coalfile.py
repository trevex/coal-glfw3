from coal import CoalFile
from util import download, unzip

class GLFW3File(CoalFile):
    version = "3.1.2"
    def prepare(self):
        download('https://github.com/glfw/glfw/releases/download/3.1.2/glfw-3.1.2.zip')
