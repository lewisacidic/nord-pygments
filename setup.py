from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="nord-pygments",
        version="0.0.1-dev.0",
        url="https://github.com/lewisacidic/nord-pygments",
        author="Rich Lewis",
        author_email="opensource[at]richlew.is",
        description="A nord-inspired style for Pygments",
        license="MIT",
        keywords=["pygments", "style", "nord"],
        packages=find_packages(),
        install_requires=["pygments"]
    )
