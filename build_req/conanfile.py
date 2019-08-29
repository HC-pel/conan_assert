from conans import ConanFile

class BuildReqConan(ConanFile):
    name = "build_req"
    version = "1.0"
    settings = "os", "arch"

    def requirements(self):
        self.requires("common_req/1.0@test/test")

    def build_requirements(self):
        self.build_requires("build_req_req/1.0@test/test")

    def build(self):
        input("Building build_req, please confirm...")

