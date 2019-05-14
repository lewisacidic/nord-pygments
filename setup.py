from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="nord-pygments",
        version="0.0.1",
        url="https://github.com/lewisacidic/nord-pygments",
        author="Rich Lewis",
        author_email="opensource@richlew.is",
        description="A nord-inspired style for Pygments",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        license="MIT",
        keywords=["pygments", "style", "nord"],
        packages=find_packages(),
        install_requires=["pygments"]
    )
