from setuptools import setup, find_packages

version = '0.2'

setup(
    name='plonetheme.unam',
    version=version,
    description='A responsive theme that provides a nice unam.mx like HTML output',
    long_description=open('README.txt').read() + '\n' +
                     open('docs/CHANGES.txt').read(),
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: Theme',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='Any',
    keywords='web zope plone cms diazo responsive unam mexico',
    url='https://github.com/imatem/plonetheme.unam',
    author='Gildardo Bautista',
    author_email='gil.cano@gmail.com',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
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
