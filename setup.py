from setuptools import setup
from yesno import __version__
__version__ = list(map(str, __version__))
setup(name='yesno',
        version='.'.join(__version__),
        description='Audio recognition using simple machine learning',
        url='http://github.com/theSage21/yesno',
        author='Arjoonn Sharma',
        author_email='arjoonn.94@gmail.com',
        license='MIT',
        packages=['yesno'],
        entry_points = {
            'console_scripts': ['yn=yesno:main'],
            },
        zip_safe=False)
