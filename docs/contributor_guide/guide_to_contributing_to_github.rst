Guide to Contributing to Lab Protocols GitHub
===============================================

This guide explains how to use GitHub to add or update lab protocols and
recipes. It assumes you have never used GitHub before.

The most important rule
------------------------

Do not add protocols directly to the final wiki page yourself.

All protocol changes, recipe changes, and protocol uploads should be submitted
through a pull request. The pull request will be reviewed before the change is
added to the wiki.

What GitHub is doing for this wiki
------------------------------------

GitHub stores the source files for the lab wiki. The wiki pages are written as
`.rst` files, which stands for :doc:`reStructured Text <rst_guide>`

When a change is approved and added to the main branch of the repository,
GitHub rebuilds the website from the files in the `docs` folder.

Common words
------------

===================  ========================================================
Word                 Meaning
===================  ========================================================
Repository           The GitHub project that stores all wiki files.
Repo                 Short for repository.
Branch               A safe working copy where you make changes.
Main                 The official version of the repository.
Commit               A saved change.
Pull request         A request to add your branch changes into `main`.
Review               Comments or approval from another person.
Merge                Adding an approved pull request into `main`.
===================  ========================================================

Where can you find the files?
-----------------------------

===================================  ==========================================
File type                            Location
===================================  ==========================================
Protocol page                        `docs/protocols/category_name/file.rst`
Protocol category page               `docs/protocols/category_name/index.rst`
Recipe page                          `docs/recipes/file.rst`
Protocol template                    `docs/contributor_guide/protocol_template.rst`
Recipe template                      `docs/contributor_guide/recipe_template.rst`
RST writing guide                    `docs/contributor_guide/rst_guide.rst`
===================================  ==========================================

Use an existing category when possible. Examples include `dna_assembly`,
`dna_fragment_generation`, `special_workflow`, and `transformation`.

If your protocol needs a new category, ask Dr. Hu or repo maintainer before
creating a new folder.

File naming rules
------------------

Use simple file names so links are easy to maintain.

* Use lowercase letters.
* Use underscores instead of spaces.
* End every protocol or recipe file with `.rst`.
* Use a descriptive name, for example `gibson_assembly.rst`.
* Avoid special characters such as `#`, `%`, `&`, `?`, and parentheses.

Good examples

::

   colony_pcr.rst
   heat_shock_transformation.rst
   lb_media.rst

Poor examples

::

   Colony PCR final!.rst
   my protocol.docx
   new-protocol(edited).rst

Before you start
-----------------

Make sure you have:

1. A GitHub account.

2. Access to the lab repository, or permission to make a fork.

3. The protocol or recipe information ready.

4. The relevant template open:

   * :doc:`protocol_template`
   * :doc:`recipe_template`

5. The RST guide open if you need formatting help:

   * :doc:`rst_guide`

How to add a new protocol to GitHub using browser
-------------------------------------------------

This is the recommended beginner workflow because it does not require using the
command line.

1. Go to the lab repository on GitHub.

2. Make sure you are signed in.

3. Open `docs/contributor_guide/protocol_template.rst`.

4. Click `Raw`.

5. Copy all of the template text.

6. Go back to the repository file list.

7. Open the folder where the new protocol should go.

   Example:

   ::

   docs/protocols/dna_assembly/

8. Click `Add file`.

9. Click `Create new file`.

10. Type the file name, ending in `.rst`.

    Example:

    ::

    gibson_assembly_troubleshooting.rst

11. Paste the template text into the editor.

12. Replace the template text with your protocol. Make appropriate changes to the template as required.

13. Use the `Preview` tab to check that the page looks reasonable.

14. Scroll to the commit section at the bottom of the page.

15. Write a short commit message.

    Example:

    ::

    Add Gibson assembly troubleshooting protocol

16. Choose the option to create a new branch for the change.

17. Click `Propose changes`.

18. GitHub will take you to a pull request page.

19. Fill out the pull request description.

20. Create the pull request and request review.

.. note::

If GitHub says that you need to fork the repository, that is okay. A fork is
your personal copy of the repository. GitHub will still let you open a pull
request back to the lab repository.

How to edit an existing protocol
---------------------------------

1. Open the protocol file on GitHub.
2. Click the edit button.
3. Make the change.
4. Use the `Preview` tab to check the formatting.
5. Add a short commit message.
6. Commit the change to a new branch.
7. Open a pull request.
8. Request PI review.

Do not edit unrelated files in the same pull request. If you need to fix two
unrelated protocols, make two pull requests.

How to add a recipe
--------------------

Recipes can use the recipe template as the starting point.

1. Open `docs/contributor_guide/recipe_template.rst`.
2. Click `Raw` and copy the template text.
3. Go to `docs/recipes/`.
4. Create a new `.rst` file, or edit the existing recipe file if the new
   recipe belongs on an existing page.
5. Make appropriate changes to the template file as required
6. Paste the template and fill it in.
7. Open a pull request and request PI review.

How to add images
------------------

You can add images to make the protocol easier to follow.

Recommended approach:

1. Put images in an `img` folder in the same directory as the page.
2. Use short file names with lowercase letters and underscores.
3. Link to the image using a relative path.

Example:

::

   .. image:: img/example_gel.png
     :width: 100%
     :align: center

.. warning::

Do not upload confidential information, unpublished data, private notes,
passwords, API keys, personal information, or large raw data files.

What a protocol upload should include
-------------------------------------

A protocol upload should include:

* A clear title.
* A short purpose section.
* Estimated time.
* Safety notes, including PPE and waste disposal.
* Materials and reagents.
* Steps written in order.
* Expected results.
* Troubleshooting notes, when useful.
* Version history - very important!

Use the existing protocol template so that pages stay consistent.

Before opening a pull request
------------------------------

Check the following:

* The file is in the correct folder.
* The file name ends in `.rst`.
* The title matches the protocol name.
* The protocol follows the template structure.
* Safety information is included.
* Version History is included - very important!
* Units are written clearly.
* Tables line up correctly in the preview.
* There are blank lines before lists, tables, and RST directives.
* You did not include private or sensitive information.
* You are only changing files related to this protocol or recipe.

After you open the pull request
--------------------------------

The pull request will be reviewed.

If edits are requested, make the edits on the same branch. The pull request will
update automatically.

The protocol is not part of the official wiki until the pull request is approved
and merged.

Helpful GitHub references
--------------------------

* `Creating new files <https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files>`_
* `Editing files <https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files>`_
* `About pull requests <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_
* `Creating a pull request <https://docs.github.com/articles/creating-a-pull-request>`_
