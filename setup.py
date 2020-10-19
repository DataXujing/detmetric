import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup



def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_des = read("README.rst")
    
platforms = ['linux/Windows']
classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Text Processing',
    'License :: OSI Approved :: Freeware License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',


]

install_requires = [
    'numpy>=1.13.0',
]

    
setup(name='detmetric',
      version='0.1.0',
      description='A package that used in Inter Credit case assign.',
      long_description=long_des,
      py_modules=['detcivar',],
      author = "Xu Jing",  
      author_email = "274762204@qq.com" ,
      url = "https://github.com/DataXujing/detmetric" ,
      license="Freeware License",
      platforms=platforms,
      classifiers=classifiers,
      install_requires=install_requires
      
      )   
      