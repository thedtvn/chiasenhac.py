from setuptools import setup

setup(
   name='chiasenhac.py',
   version="0.0.1",
   description='A light weight Python library for the Chia Sẻ Nhạc',
   author='The DT',
   author_email='duongtuan30306@gmail.com',
   packages=["chiasenhac"],
   install_requires=["aiohttp", "requests"]
)