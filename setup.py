from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pinkfish',
    version='1.3.0',
    description='A backtester and spreadsheet library for security analysis.',
    author='Farrell Aultman',
    author_email='fja0568@gmail.com',
    url='https://github.com/fja05680/pinkfish',
    packages=['pinkfish'],
    include_package_data=True,
    license='MIT',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Distributed Computing',
    ],
    extras_require={
        'talib':  ["talib"],
    }
)
