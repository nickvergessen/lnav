from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps


class LnavConan(ConanFile):
    name = "lnav"
    version = "0.10.2"
    homepage = "https://lnav.org"
    url = "https://github.com/tstack/lnav.git"
    license = "BSD-2-Clause"
    description = (
        "The Log File Navigator, lnav for short, is an advanced "
        "log file viewer for the small-scale"
    )
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*"
    no_copy_source = True
    requires = (
        "bzip2/1.0.8",
        "libarchive/3.6.0",
        "libcurl/7.80.0",
        "ncurses/6.3",
        "pcre/8.45",
        "readline/8.1.2",
        "sqlite3/3.38.0",
        "zlib/1.2.11",
    )
    generators = ("virtualrunenv",)
    default_options = {
        "libarchive:with_bzip2": True,
        "libarchive:with_lz4": True,
        "libarchive:with_lzo": True,
        "libarchive:with_lzma": True,
        "libarchive:with_zstd": True,
        "pcre:with_jit": True,
        "sqlite3:enable_json1": True,
        "sqlite3:enable_soundex": True,
    }

    def generate(self):
        CMakeToolchain(self).generate()
        CMakeDeps(self).generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
