from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='elasticsearchquery',
    version='0.1.1',
    description='Runs queries against AWS elasticsearch deployments.',
    long_description=long_description,
    url='https://github.com/techjacker/elasticsearchquery',
    install_requires=[
        "botocore>=1.10.30",
        "aws-requests-auth>=0.4.1",
        "requests>=2.18.4"
    ],
    tests_require=[
        'pytest'
    ],
    license='MIT',
    author='Andrew Griffiths',
    author_email='mail@andrewgriffithsonline.com',
    packages=['elasticsearchquery'],
    entry_points={
        'console_scripts': [
            'elasticsearchquery = elasticsearchquery.elasticsearchquery:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
)
