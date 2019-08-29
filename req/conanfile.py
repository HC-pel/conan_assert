from conans import ConanFile

class ReqConan(ConanFile):
    name = "req"
    version = "1.0"
    settings = "os", "arch"

    def requirements(self):
        self.requires("common_req/1.0@test/test")

    def build(self):
        input("Building req, please confirm...")

