from setuptools import find_packages, setup

import versioneer

DISTNAME = "Pedestrian Assistant"
AUTHOR = "Darshan Krishnaswamy"
AUTHOR_EMAIL = "darsh797@gmail.com"

INSTALL_REQUIRES = ["numpy >= 1.12", "numba >= 0.38"]

DESCRIPTION = "An object detection neural network that detects and classifies pedestrian traffic lights"


setup(
    name=DISTNAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6",
    packages=find_packages(where="utils", exclude=["tests", "tests.*"]),
    package_dir={"": "utils"},
)
