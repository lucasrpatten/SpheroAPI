from setuptools import setup

setup(
    name='sphero_api',
    version='0.0.1',
    description='A python based API to control sphero devices',
    author='lucasrpatten',
    license="MIT",
    url='https://github.com/lucasrpatten/SpheroAPI',
    packages=['sphero_api'],
    install_requires=['bleak>=0.20.2'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
    ],
)
