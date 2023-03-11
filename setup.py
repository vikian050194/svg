import os

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        if os.geteuid() == 0:
            raise RuntimeError("Install should be as a non-privileged user")


def readme():
    with open("README.md") as f:
        return f.read()


attrs = dict(
    name="svg",
    version="0.7.0",
    description="SVG",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities"
    ],
    url="https://github.com/vikian050194/svg",
    author="Kirill Vinogradov",
    author_email="vikian050194@gmail.com",
    license="MIT",
    packages=find_packages(where=".", exclude=["tests*"], include="*"),
    install_requires=[],
    test_suite="nose.collector",
    tests_require=["nose"],
    cmdclass={
        "develop": PostDevelopCommand,
        "install": PostInstallCommand,
    },
    entry_points = {
        "console_scripts": ["svg=svg.app:run"],
    },
    include_package_data=True,
    zip_safe=False
)

setup(**attrs)
