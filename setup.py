import os
import codecs
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-redis-stats-instant',
    version='0.1',
    description='Display current Redis stats on Django\'s admin dashboard',
    long_description = read('README.md'),
    author='Arcady Chumachenko',
    author_email='arcady.chumachenko@gmail.com',
    url = 'https://github.com/ilvar/django-redis-stats-instant',
    download_url='',
    packages=['redis_stats', ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe = False,
    install_requires = [],
)
