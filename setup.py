from setuptools import setup

setup(name='tweet_dashboard',
    version='0.1.dev',
    description='Dashboard to display information about tweets and users',
    author='Jeremy Belisle',
    packages=['twitter'],
    install_requires=['django', 'tweepy', 'TwitterSearch'])
