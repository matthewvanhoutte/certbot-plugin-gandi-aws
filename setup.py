from setuptools import setup, find_packages 

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='certbot-plugin-gandi-aws',
    version='0.0.1',
    author="Matthew Vanhoutte",
    author_email="bonsaichills@gmail.com",
    description="Certbot plugin for authentication using Gandi LiveDNS and using AWS to store API credentials",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthewvanhoutte/certbot-plugin-gandi-aws",
    packages=find_packages(),
    python_requires=' >=3.5.*',
    install_requires=[
        'certbot',
        'zope.interface',
        'requests>=2.4.2',
    ],
    entry_points={
        'certbot.plugins': [
            'dns = certbot_plugin_gandi_aws.main:Authenticator',
            'dns-gandi = certbot_plugin_gandi_aws.main:Authenticator',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        ],
)
