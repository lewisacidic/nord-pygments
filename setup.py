from setuptools import setup

if __name__ == "__main__":
    setup(
        name="nord-pygments",
        version="0.0.2",
        url="https://github.com/lewisacidic/nord-pygments",
        author="Rich Lewis",
        author_email="opensource@richlew.is",
        description="A nord-inspired style for Pygments",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        license="MIT",
        keywords=["pygments", "style", "nord"],
        py_modules=["nord_pygments"],
        install_requires=["pygments"]
    )
