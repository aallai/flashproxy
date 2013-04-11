from distutils.core import setup

setup(
    name="Flashproxy",
    version="1.0",
    description="Flashproxy Client Programs",
    url="crypto.stanford.edu/flashproxy",
    py_modules=["flashproxy"],
    scripts=["flashproxy-client", "flashproxy-reg-http", "flashproxy-reg-url", "flashproxy-reg-email"],
)
