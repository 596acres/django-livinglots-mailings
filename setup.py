from setuptools import setup, find_packages
import os

import livinglots_mailings


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='eric@596acres.org',
    name='django-livinglots-mailings',
    version=livinglots_mailings.__version__,
    description=("A Django app that sends emails base on simple criteria"),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/596acres/django-livinglots-mailings/',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6.0',
        'django-braces>=1.4.0',
        'django-model-utils==2.2.0',
    ],
    packages=find_packages(),
    include_package_data=True,
)
