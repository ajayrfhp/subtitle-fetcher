from setuptools import setup
import sys

setup(name = 'subtitle-fetcher',
      description = 'Python tool to download subtitles.',
      version = '0.1.0',
      author = 'Ajay Prasadh V',
      author_email = 'ajayrfhp1710@gmail.com',
      packages = ['subtitle_downloader'],
      entry_points = {
          'console_scripts': ['subtitle-fetcher=subtitle_downloader:main'],
      },
      url = 'https://github.com/ajayrfhp/subtitle-fetcher/',
      keywords = ['subtitle', 'download', 'utility', 'movie'],
      classifiers = [
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      )
