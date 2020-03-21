from setuptools import setup, find_packages
from os import path

# Path of the extension
here = path.abspath(path.dirname(__file__))


# Get description from Readme.md
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='covid-data-api',  # Required
    version='1.3',
    description="""
                Real time data extractor - web scrapper for covid19 from john hopkins university
                url: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
                """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gtkChop/covid19',
    author='Swaroop',
    author_email='',
    license="MIT",
    classifiers=[  # Optional
	"License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='Data extractor covid19',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests']
    ),
    python_requires='>=3.6',

    # All install packages should go on requirements.txt file
    install_requires=[
        'python-dateutil==2.8.1',
        'requests==2.23.0'
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
