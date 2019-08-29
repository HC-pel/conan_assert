from conans import ConanFile

class BuildReqReqConan(ConanFile):
    name = "build_req_req"
    version = "1.0"
    settings = "os", "arch"

    def requirements(self):
        self.requires("common_req/1.0@test/test")

    def build(self):
        input("Building build_req_req, please confirm...")

