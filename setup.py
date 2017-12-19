import os
import setuptools

module_path = os.path.join(os.path.dirname(__file__), '__init__.py')
version_line = [line for line in open(module_path) if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-restplus-marshmallow",
    version=__version__,
    url="https://github.com/joeyorlando/flask-restplus-marshmallow",
    author="Joey Orlando",
    author_email="joey@100danish.com",
    description="Flask RESTPlus with a twist of marshmallow",
    long_description=open('README.md').read(),
    py_modules=['__init__'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ]
)
