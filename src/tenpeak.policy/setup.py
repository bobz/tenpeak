from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='tenpeak.policy',
      version=version,
      description="Tenpeak Policy",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='tenpeak men women dating relationships',
      author='bobz',
      author_email='bobz.admin@gmail.com',
      url='http://www.tenpeak.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tenpeak'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
