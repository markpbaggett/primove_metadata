from setuptools import setup, find_packages

with open("README.rst", "r") as read_me:
    long_description = read_me.read()


setup(
    name="UTK PrimoVE Non-Marc Metadata Mappings",
    description="a documentation generator for descriping mapping and configuration for non-Marc metadata to Primo work at UTK",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/markpbaggett/primove_metadata",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 1.4",
            "sphinxcontrib-napoleon >= 0.7",
            "sphinx-markdown-tables >= 0.0.9",
            "recommonmark >=0.5.0",
            "sphinx-bootstrap-theme >= 0.6.5",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords=["libraries", "exlibris primo", "metadata"],
)