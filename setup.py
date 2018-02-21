'''
Created on 25 Jan 2018

@author: mary-katetyrrell
'''

from setuptools import setup


setup(name="SYSINFOTEST", 
      version="0.1",
      description="Basic System Info for COMP30670",
      url="",
      author="Mary-Kate Tyrrell",
      author_email="mary.tyrrell@ucdconnect.ie",
      license="GPL3",
      packages=['SYSINFOTEST'],
      entry_points={'console_scripts':['comp30670_systeminfo=SYSINFOTEST.main:main'],
                    }
      )
