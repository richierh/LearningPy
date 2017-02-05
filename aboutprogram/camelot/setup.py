#!/usr/bin/env python
import os
import sys
import camelot
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)
README = os.path.join(src_dir, 'readme.txt')
long_description = open(README).read() + '\n\n'
dependencies = os.path.join(src_dir, 'requirements.txt') 
install_requires = open( dependencies ).read().splitlines()
if sys.platform.startswith('win'):
    install_requires.append('winpaths')

setup(
    name = 'Camelot',
    version = camelot.__version__,
    description = 'A python GUI framework on top of Sqlalchemy and Qt, inspired by the Django admin interface. Start building desktop applications at warp speed, simply by adding some additional information to you model definition.',
    long_description = long_description,
    keywords = 'qt pyqt sqlalchemy elixir desktop gui framework',
    author = 'Conceptive Engineering',
    author_email = 'project-camelot@conceptive.be',
    maintainer = 'Conceptive Engineering',
    maintainer_email = 'project-camelot@conceptive.be',  
    url = 'http://www.python-camelot.com',
    include_package_data = True,
    package_data = {
        # If any package contains *.txt files, include them:
        '':['*.txt', '*.rst', '*.html', '*.js', '*.png', '*.doc', '*.GPL'],
        'doc':['*.rst', '*.html', '*.png'],
    },
    options = {
        'extract_messages':{'input_dirs':('camelot',),
                            'output_file':'camelot/art/translations/camelot.pot',
                            'keywords':'ugettext tr _ ugettext_lazy'},
        'init_catalog':{'domain':'camelot',
                        'input_file':'camelot/art/translations/camelot.pot',
                        'output_dir':'camelot/art/translations'},
        'update_catalog':{'domain':'camelot',
                          'input_file':'camelot/art/translations/camelot.pot',
                          'output_dir':'camelot/art/translations'},
    },  
    license = 'GPL, Commercial',
    platforms = 'Linux, Windows, OS X',
    install_requires = install_requires,
    entry_points = {'console_scripts':[
                     'camelot_admin = camelot.bin.camelot_admin:main',
                     'camelot_example = camelot_example.main:main',
                     'camelot_mini_example = camelot_example.mini_main:main',
                    ],
                    'setuptools.installation':[
                     'eggsecutable = camelot_example.main:main',
                    ],                   
                    },
    classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Environment :: Win32 (MS Windows)',
              'Environment :: X11 Applications',
              'Environment :: X11 Applications :: Gnome',
              'Environment :: X11 Applications :: GTK',
              'Environment :: X11 Applications :: KDE',
              'Environment :: X11 Applications :: Qt',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU General Public License (GPL)',
              'License :: Other/Proprietary License',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              'Topic :: Database :: Front-Ends',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Libraries :: Application Frameworks',
              ],         
    packages = find_packages() + ['doc',] )
