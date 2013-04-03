===============
plonetheme.unam
===============

.. image:: https://travis-ci.org/imatem/plonetheme.unam.png
	:target: https://travis-ci.org/imatem/plonetheme.unam

This is a responsive theme that provides a nice unam.mx like HTML output.


.. contents:: Table of Contents
	:depth: 2


Requirements
------------

    * Plone 4.3.x (http://plone.org/products/plone)
    

Screenshots
------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/imatem/plonetheme.unam/raw/master/src/plonetheme/unam/theme/plonetheme.unam/preview.png

Layout of the site when viewed with a cell phone resolution:

.. image:: https://github.com/imatem/plonetheme.unam/raw/master/screenshot-cel.png

.. image:: https://github.com/imatem/plonetheme.unam/raw/master/screenshot-cel2.png


Installation
------------

Getting the theme
~~~~~~~~~~~~~~~~~~~~

Zip file
++++++++++

If you are an end user, you might enjoy installation via zip file import.

    1. Download a `zip file <https://github.com/imatem/plonetheme.unam/plonetheme.unam.zip>`_ 
        
    2. Upload the theme from the Theming control panel.

Buildout
++++++++++

If you are a developer, you might enjoy installing it via buildout.

Add ``plonetheme.unam`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        ...
        plonetheme.unam

Or, you can add it as a dependency on your own product *setup.py*::

    install_requires=[
        ...
        'plonetheme.unam',
    ],


Enabling the theme
~~~~~~~~~~~~~~~~~~~~

    Activate the theme from the Theming control panel. That's it!


Credits
-------

    * Gildardo Bautista.
      
    * Adriana Ramírez Vigueras.


`beyondskins.responsive <https://github.com/simplesconsultoria/beyondskins.responsive>`_ was used as a start for this theme.
