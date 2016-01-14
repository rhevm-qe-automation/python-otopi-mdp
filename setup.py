import os
from setuptools import setup

def read(fname):
    return open(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), fname,
            )
        )
    ).read()

setup(
    name="otopi-mdp",
    version="0.1",
    author="Lukas Bednar",
    author_email="lbenar@redhat.com",
    description="Implements parser for otopi machine dialog.",
    license="GPL2",
    keywords="otopi machine dialog",
    url="https://github.com/rhevm-qe-automation/python-otopi-mdp",
    platforms=['linux'],
    packages=['otopimdp'],
    long_description=read('README.md'),
#    install_requires=['otopi'],  # It fails tests
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License 2 (GPL2)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],
)
