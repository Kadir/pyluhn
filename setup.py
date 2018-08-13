from distutils.core import setup

setup(
    name='PyLuhn',
    version='0.1',
    license='Public Domain',
    description='Basic Implementation for Luhn Algorithm'
        'Useful for Verifying Credit Cards.',
    package_dir = {'':'src'},
    py_modules=['pyluhn'],
    url='http://github.com/kadir/pyluhn',
    author='Kadir Eksi',
    author_email='kadireksi@sabanciuniv.edu',
    keywords = ['luhn', 'check digit','credit card','luhn mod N'],
    classifiers = [
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)