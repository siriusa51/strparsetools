import setuptools


def main():
    with open("README.md", "r") as f:
        long_description = f.read()

    from strparsetools import __version__
    setuptools.setup(
        name="strparsetools",
        version=__version__,
        author="siriusa51",
        author_email="siriusa51@outlook.com",
        description="A string parsing toolset",
        license="MIT License",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/siriusa51/strparsetools",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3",
        packages=["strparsetools"],
    )


if __name__ == '__main__':
    main()
