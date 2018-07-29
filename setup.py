from setuptools import setup
from subprocess import check_output

commit_sha = check_output(['git', 'rev-parse', '--short', 'HEAD']).decode()

setup(name='playx',
      version='0.1-dev-' + commit_sha,
      description='Search and play any song from terminal',
      url='http://github.com/NISH1001/playx',
      author='NISH1001',
      author_email='nishanpantha@gmail.com',
      license='MIT',
      packages=['playx'],
      install_requires=[
        "youtube_dl==2018.3.20",
        "requests==2.18.4",
        "beautifulsoup4==4.6.0"])
