Basics of reStructuredText
===========================

.. note::
    This section is adapted from the lab wiki of the `Galloway Lab at MIT 
    <https://gallowaylabmit.github.io/protocols/en/latest/contributor_guide.html#basics-of-restructuredtext>`_ <br>
    Link to the `LICENSE<https://github.com/GallowayLabMIT/protocols/blob/latest/LICENSE>`_ is attached. 

reStructuredText (RST) is a *lightweight* markup language. This means that it is not
as cumbersome as languages like HTML and LaTeX, but still has enough power to make
nice looking documents.

There is an `excellent RST primer and reference here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
which should be your primary reference, but here we will cover some of the basics.

One nice feature of the generated website is the ability to view the page source for each page.
If there is a protocol that uses some RST feature that you want to replicate, on the desktop version of the website (e.g. not mobile),
you can click the "View page source" button in the upper right of **any page** on the website to see the RST code that
generated that page. That includes this page, so check out this page's source to see how this guide was written!

.. note::
  There are several whitespace-dependent features of RST. This means that you should configure
  your text editor to insert spaces instead of tabs when you hit the tab button (this is also true
  if you are programming in whitespace-dependent languages like Python).

  Without wading too deeply into the
  `holy war <https://softwareengineering.stackexchange.com/questions/57/tabs-versus-spaces-what-is-the-proper-indentation-character-for-everything-in-e>`_,
  tabs vs spaces **does not mean the difference between pressing the space bar vs hitting tab for indentation**, it refers
  to what character actually gets inserted into the document when you press the tab button.

  Long story short, if your text editor inserts literal tab characters,
  there is possible inconsistency between tools and editors; some may display a single tab character as the width of two spaces, some as
  the width of four spaces, and so on. This causes problems. If you set your editor to insert spaces, you still hit tab, but the editor
  inserts some fixed number of spaces, typically four.

  This setting will depend per editor. In VS code for example, you don't have to do anything; it defaults to inserting spaces, but
  the option looks like this:

  .. image:: img/tabs_vs_spaces.png
    :width: 100%
    :align: center



Simple markup
~~~~~~~~~~~~~

You can add headers by surrounding the header with equal signs, hyphens, tildes, and other special characters.

.. admonition:: Example

  ::

    Section header
    ==============

    Subsection header
    -----------------

Use single asterisks to italicize text. Use double asterisks to bold text. Wrapping double backticks around text renders it in monospace.

.. admonition:: Example

  ::

    *italics* and **bold** and ``monospaced``.

  renders as

  *italics* and **bold** and ``monospaced``.


You can make bullet lists by starting lines with ``*`` or ``#``, and you can make numbered lists by starting lines with ``1.``, ``2.``, etc.

If you are nesting lists, you must surround nesting levels with blank lines.

.. admonition:: Example

  ::

    * Lab activities

      * Axe throwing
      * Pizza party
      * ?????

    * Lab meme sources

      * p53
      * Cloning, so much cloning

    1. Testing
    2. a
    3. numbered
    4. list

  renders as

  * Lab activities

    * Axe throwing
    * Pizza party
    * Other?

  * Lab meme sources

    * p53
    * Cloning, so much cloning

  1. Testing
  2. a
  3. numbered
  4. list


Explicit markup
~~~~~~~~~~~~~~~

In RST, an "explicit" block is any block that starts with ``..``. Explicit blocks must be surrounded
on both sides by blank lines, like nested lists. This means that explicit blocks like:

::

  Do the foo, then the bar
  .. note::

    Make sure you don't do the bar, then the foo!

will not render correctly, it must be written:

::

  Do the foo, then the bar

  .. note::

    Make sure you don't do the bar, then the foo!

Admonitions
~~~~~~~~~~~

To call-out a specific part of a protocol, you can use one of the various admonitions.

This project includes the special time estimation admonition, which demonstrates the general principle. Writing:

::

  .. time::

    2 hours

renders as

.. time::

  2 hours

Other directives (code blocks, tables, images, etc) can be fully nested inside these blocks.


Other options commonly used here are ``hint``, ``important``, ``note``, ``tip``, ``deprecated``, and ``warning``, which render as

.. hint::

  Test

.. important::

  Test

.. note::

  Test

.. tip::

  Test

.. deprecated:: 2021.11.24

   Test

.. warning::

  Test

Code
~~~~

To insert a codeblock, start an empty line with ``::``, followed by an indented block that will be rendered as code.

.. admonition:: Example

  The above code example of the time estimation admonition was written as:

  ::

    ::

      .. time::

        2 hours


Tables
~~~~~~

See the `table documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables>`_ for more details,
but in brief, most of the time you can use the "simple" table layout.

In the simple table layout, you simply surround the desired table text with equal signs to set off different columns.

.. admonition:: Example

  ::

    ================= ===========================
    Ingredient         Amount per 1L final volume
    ================= ===========================
    Tryptone 			12 g
    Yeast extract		24 g
    Glycerol			4 mL
    Deionized water		900 mL
    ================= ===========================

  renders as

  ================= ===========================
  Ingredient         Amount per 1L final volume
  ================= ===========================
  Tryptone 			12 g
  Yeast extract		24 g
  Glycerol			4 mL
  Deionized water		900 mL
  ================= ===========================


References and links
~~~~~~~~~~~~~~~~~~~~~

To reference a standalone hyperlink, you can just simply write it directly in the rst file, no special markup required.

If you want to add link text, use the following syntax:

.. admonition:: Example

  ::

    https://example.org or `Link text <https://example.org>`_

  renders as:

  https://example.org or `Link text <https://example.org>`_

If you want to specifically link to other protocols/recipes files, you use the special `doc` syntax:

.. admonition:: Example

  ::

    :doc:`This <contributor_guide>` is a link to this very document!

  renders as:

  :doc:`This <contributor_guide>` is a link to this very document!

as you can see, this is very similar to the external hyperlink, except it has the special ``:doc:`` before it, which tells Sphinx
that the document is included in this repository.

If you want to reference a specific subsection of a document, you can set a label and set a reference to it. This is best explained by the
`documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role>`_, noting that labels that you create are
global and shared across the entire repository!


Images
~~~~~~

To include an image, you can specify it as follows. Typically, you want to align center
and make the image fill the available horizontal space, so a common image call would be:

::

  .. image:: image_location/image_filename.png
    :width: 100%
    :align: center



Math
~~~~

You can write arbitrary LaTeX-formatted math by using the math directive. The math must be
separated from the directive by a blank line, followed by an indented math block.

.. admonition:: Example

  ::

    .. math::

        E = mc^2

  renders as

  .. math::

      E = mc^2
