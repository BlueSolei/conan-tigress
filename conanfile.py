import os
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class TigressConan(ConanFile):
    name = "tigress"
    version = "3.1"
    license = "<Put the package license here>"
    author = "Shaul Fridman <shaul.fridman@gmail.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Tigress is a diversifying virtualizer/obfuscator for the C language"
    topics = ("obfuscator",)
    settings = "os", "arch"
    exports = "*.zip"

    def configure(self):
        s = self.settings
        supportedEnv = (s.os == "Linux" and s.arch == "x86_64") or (
            s.os == "Linux" and s.arch == "armv7") or (s.os == "Macos" and s.arch == "x86_64")
        if not supportedEnv:
            raise ConanInvalidConfiguration(
                f"Tigress only supported oss are Darwin-x86_64, Linux-armv7, Linux-x86_64. This machine os: {s.os}-{s.arch}.")

    def build(self):
        zip_name = f"tigress-{self.version}-bin.zip"
        tools.unzip(zip_name, keep_permissions=True)
        os.unlink(zip_name)

    def package(self):
        self.copy("*", src="tigress", dst="bin", keep_path=True, )
        self.copy("**/*", src="tigress", dst="bin", keep_path=True)

    def package_info(self):
        bin = os.path.join(self.package_folder, "bin", self.version)
        self.env_info.PATH.append(bin)
        self.env_info.TIGRESS_HOME = bin
