from setuptools import setup

setup(
    name="SDKeyLogger",
    version="2.0",
    author="Dankhara Shubham",
    author_email="shubham.dankhara.p@gmail.com",
    description="Provides KeyBoard Key Capturing.",
    url="https://github.com/MRSDPY/Key-Logger",
    license="MIT",
    py_modules=["key_logger"],
    install_requires=["keyboard"],
    zip_safe=False,
)