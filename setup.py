from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

_VERSION = '0.1'

setup(
    name='drl-car-racing',
    version=_VERSION,
    description='Teaching a car to drive using deep reinforcement learning.',
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7'
    ],
    url='https://github.com/wriazati/drl-car-racing',
    author='wriazati',
    author_email='wriazati@yahoo.com',
    entry_points={  # Optional
        'console_scripts': [
            'run=:main',
        ],
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    test_suite="test",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=[],
    include_package_data=True,
    license='',
    keywords=''
)