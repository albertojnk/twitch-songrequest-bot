import os

from setuptools import setup

setup(
    name='twitch_songrequest_bot',
    install_requires=['twitchio==1.2.3',
                      'python-dotenv==0.17.1',
                      'Flask==2.0.1',
                      'requests==2.25.1',
                      'pymongo==3.11.4',
                      'google-auth==1.31.0',
                      'google-auth-httplib2==0.1.0',
                      'google-auth-oauthlib==0.4.4',
                      'google-api-python-client==2.8.0',
                      'googleapis-common-protos==1.53.0'],
)