from setuptools import setup, find_packages
from os import path

# Path of the extension
here = path.abspath(path.dirname(__file__))


# Get description from Readme.md
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='covid',  # Required
    version='1.0',
    description="""
                Real time data extractor - web scrapper for covid19 from john hopkins university
                url: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
                """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Swaroop',
    author_email='swaroopbatk@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Topic : Corona Virus data',
        'License : MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='Data extractor covid19',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests']
    ),
    python_requires='>=3.6',

    # All install packages should go on requirements.txt file
    install_requires=[
    ],
    extras_require={
    },
    package_data={
    },
    data_files=[
    ],

    # Entry Points
    entry_points={
    }
)