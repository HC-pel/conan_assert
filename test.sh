find . -name "conanfile.py" | xargs -L 1 -i conan export {} test/test
conan install . --build=missing
