from setuptools import setup

with open("./version") as fd:
    version = fd.read().strip()


setup(
    name="tlds",
    version=version,
    description="Automatically updated list of valid TLDs taken directly from IANA",
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Communications",
    ],
    keywords="tld",
    author="Amir Szekely",
    author_email="kichik@gmail.com",
    url="https://github.com/kichik/tlds",
    license="MIT",
    packages=["tlds"],
    include_package_data=True,
    zip_safe=True,
)
