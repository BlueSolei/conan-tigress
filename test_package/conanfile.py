import os
from conans import ConanFile, tools


class TigressTestConan(ConanFile):
    settings = "os", "arch"

    def build(self):
        pass

    def test(self):
        # example of runnig tigress taken from INSTALL file in root of the unzipped tigress
        s = self.settings
        # supported platforms as described by tigress docs
        if s.os == "Macos":
            compilerVersion = "5.1"
            compilerName = "Clang"
            osName = "Darwin"
        else:
            compilerVersion = "4.6"
            compilerName = "Gcc"
            osName = "Linux"

        env = f"{s.arch}:{osName}:{compilerName}:{compilerVersion}"

        cmdTigress = f"tigress --Environment={env} --Transform=Virtualize --Functions=main,fib,fac --out=result.c $TIGRESS_HOME/test1.c"
        cmdBuild = "gcc -o result result.c"
        cmdStrip = "strip result"
        cmdRun = "./result"
        testTigress = [cmdTigress, cmdBuild, cmdStrip, cmdRun]
        for cmd in testTigress:
            self.run(cmd)
