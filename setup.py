from setuptools import setup, find_packages

# remember to change this
from pkg import __version__

# fill in your details
setup(
    name="{pkg-name}",
    version=__version__,
    description="{pkg-description}",
    author="{author-name}",
    author_email="{author-email}",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[],
    include_package_data=True
)
