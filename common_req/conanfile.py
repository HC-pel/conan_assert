from conans import ConanFile, tools

class CommonReqConan(ConanFile):
    name = "common_req"
    version = "1.0"

    def requirements(self):
        pass

    def build_requirements(self):
        pass

    def build(self):
        input("Building common_req...")

    def package(self):
        pass

