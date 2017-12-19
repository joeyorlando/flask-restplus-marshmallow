from setuptools import setup


setup(
    name="flask-restplus-marshmallow",
    version='0.1.0',
    url="https://github.com/joeyorlando/flask-restplus-marshmallow",
    author="Joey Orlando",
    author_email="joey@100danish.com",
    description="Flask RESTPlus with a twist of marshmallow",
    long_description=open('README.md').read(),
    packages=['flask_restplus_patched']
    zip_safe=False,
    platforms='any',
    install_requires=[
        'flask',
        'flask-marshmallow',
        'webargs',
        'flask-restplus'
    ],
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
