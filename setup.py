from setuptools import setup, find_packages

version = '1.1.1'

setup(
    name='plonetheme.unam',
    version=version,
    description='A responsive theme that provides a nice unam.mx like HTML output',
    long_description=open('README.txt').read() + '\n' +
                     open('docs/CHANGES.txt').read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    platforms='Any',
    url='https://github.com/imatem/plonetheme.unam',
    author='Gildardo Bautista',
    author_email='gil.cano@gmail.com',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    extras_require={
        'develop': [
            'flake8',
            'jarn.mkrelease',
            'manuel',
            'Sphinx',
            'zest.releaser',
        ],
        'test': [
            'plone.app.testing',
            'unittest2'
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
    )
