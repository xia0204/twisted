#! /usr/bin/env python
"""
Package installer for Twisted

Copyright (c) 2001 by Twisted Matrix Laboratories
All rights reserved, see LICENSE for details.

$Id: setup.py,v 1.3 2001/07/24 08:42:47 glyph Exp $
"""

import distutils, os, sys
from distutils.core import setup, Extension
from twisted import copyright

#############################################################################
### Call setup()
#############################################################################

setup_args = {
    'name': "Twisted",
    'version': copyright.version,
    'description': "Twisted %s is a framework to build frameworks" % (copyright.version,),
    'author': "Twisted Matrix Laboratories",
    'author_email': "twisted-python@twistedmatrix.com",
    'maintainer': "Glyph Lefkowitz",
    'maintainer_email': "glyph@twistedmatrix.com",
    'url': "http://twistedmatrix.com/",
    'licence': "GNU LGPL",
    'long_description': """
Twisted is a framework to build frameworks. It is expected that one day
the project has expanded to the point that the Twisted Reality framework
(a very small part of the codebase, even now) can seamlessly integrate
with mail, web, DNS, netnews, IRC, RDBMSs, desktop environments, and
your toaster. 
""",
    'packages': [
        'twisted',
        'twisted.internet',
        'twisted.persisted',
        'twisted.pim',
        'twisted.protocols',
        'twisted.python',
        'twisted.reality',
        'twisted.spread',
        'twisted.test',
        'twisted.web',
    ],
}

if hasattr(distutils.dist.DistributionMetadata, 'get_keywords'):
    setup_args['keywords'] = "internet www tcp framework games"

if hasattr(distutils.dist.DistributionMetadata, 'get_platforms'):
    setup_args['platforms'] = "win32 posix"

if sys.platform == 'posix':
    import glob
    setup_args['scripts'] = filter(os.path.isfile, glob.glob('bin/*'))

#'"
# for building C banana...

def extpath(path):
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), path)
    

setup_args['ext_modules'] = [
    Extension("twisted.spread.cBanana", [extpath("twisted/spread/cBanana.c")]),
    ]

apply(setup, (), setup_args)

