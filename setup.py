from setuptools import setup

if __name__ == "__main__":
    setup(
        author="Rich Lewis",
        author_email="opensource@richlew.is",
        description="A nord-inspired style for Pygments",
        download_url="https://github.com/lewisacidic/nord-pygments/releases",
        entry_points={"pygments.styles": "nord = nord_pygments:Nord"},
        install_requires=["pygments"],
        keywords=["pygments", "style", "nord"],
        license="MIT",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        name="nord-pygments",
        project_urls={
            "Source": "https://github.com/lewisacidic/nord-pygments",
        },
        py_modules=["nord_pygments"],
        url="https://github.com/lewisacidic/nord-pygments",
        version="0.1.0",
        zip_safe=False,
    )
