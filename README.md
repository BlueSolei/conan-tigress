# Conan package for the Tigress obfuscator

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Create package

- clone this repo
- download [tigress zip file](http://tigress.cs.arizona.edu/cgi-bin/projects/tigress/download.cgi) to the repo root,
  you should have a file name (e.g.) `tigress-3.1-bin.zip`
- set the `version` field in the conanfile.py to the version of the downloaded zip file (here 3.1)
- run `conan create .`
