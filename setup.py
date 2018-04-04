from distutils.core import setup
setup(
  name = 'pypbi',
  packages = ['pypbi'], # this must be the same as the name above
  version = '0.0.2',
  description = 'An Unofficial Python wrapper around PowerBI REST API',
  author = 'Andrey Vykhodtsev',
  author_email = 'vykhand@outlook.com',
  url = 'https://github.com/vykhand/pypbi', # use the URL to the github repo
  download_url = 'https://github.com/vykhand/pypbi/archive/0.0.2.tar.gz', # I'll explain this in a second
  keywords = ['powerbi'], # arbitrary keywords
  install_requires=['pyyaml'],
  classifiers = [],
)