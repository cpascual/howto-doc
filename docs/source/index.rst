.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:

Goals of documenting
====================

-  Usability: define an API
-  Maintainability: allow other developers (or yourself in a few months
   time) to understand the purpose of each object and how to use it
-  Reviewability: facilitate high-level revision of your code (if the
   code is well documented, a reviewer does not need to pay attention to
   the implementation details to get an idea of the high-level logic
   behind the code)

Mechanisms used for documenting
===============================

The documentation of the code should be done at various levels:

-  **high-level descriptions in dedicated doc pages**. Most python
   projects use `sphinx <https://www.sphinx-doc.org>`__ to generate
   them.
-  **API documentation in docstrings** (tools such as the `sphinx
   autoapi extension <https://pypi.org/project/sphinx-autoapi/>`__
   may parse your docstrings and generate browsable API references)
-  **typing hints** can be used as a great complement to docstrings to
   define an API. They may be used by documentation generators.
-  **low-level code comments** to communicate implementation details to
   other developers (not usually part of generated browsable docs)

Sphinx
======

Sphinx is a tool to generate documentation from a document sources
written in the
`reStructuredText <ttps://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
markup language (more details below).

The sources of documentation in ``.rst`` format are normally committed
to the same repository as the code itself, within a ``docs/source`` dir
in the root of the python project (e.g., next to the ``pyproject.toml``
file).

The configuration of the sphinx tool itself is done in a
``docs/source/conf.py`` file.

To start from scratch you can bootstrap the sphinx structure using `the
sphinx-quickstart
tool <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-quickstart.html>`__.

reStructuredText
================

reStructuredText is the text markup language typically used to write
python documentation with sphinx. It is designed to be human-friendly
when read in its raw form and easy to write with a simple text editor
(although some IDE extensions are often helpful).

See this `intro to reStructuredText
syntax <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__.

This implies that the ``.rst`` source files can be handled with the same
tools as e.g. python source files (e.g. you can use the same git
workflows for reviewing, tracking changes, etc.)

reStructuredText can be parsed and “compiled” (e.g. by sphinx) into
different browsable formats (typically html, pdf, etc.)

reStructuredText is similar to markdown but it is a bit more complex. It
is better suited for multi-file documents (e.g. for cross-referencing
doc elements defined in separate files).

It accepts html tags for complex formatting, **but it is better to avoid
them because they limit the readability**.

Also it is helpful to keep a
`cheatsheet <https://raw.githubusercontent.com/ralsina/rst-cheatsheet/master/rst-cheatsheet.pdf>`__
at hand when writing reStructuredText

.. tip:: rst formatting can be complex, but do not be intimidated.
   Start with simple formatting and investigate the more advanced syntax
   as you need it

Type hinting (as a form of documenting)
=======================================

Python3 introduced type hinting, which serves also other purposes such
as auto-validation of code, but here we consider it from the point of
view of documentation. For example, the following type-hinted code 
provides explicit documentation on the expected types for the function
method arguments and return values.

.. code:: python

   def count_letters(word: str) -> int
       return len(word)


Type hints can also be used to specify the type of a module or class
level variable:

.. code:: python


   greeting: str = "hello"

   class Liquid:
       density: float = 1.034

See the `official docs about type
hinting <https://docs.python.org/3/library/typing.html>`__ to learn
about its syntax.

Docstrings
==========

Docstrings are strings in python code that are used for documenting
python objects.

They are **the most important source of documentation from an API point
of view**.

Formal description is in `PEP257 <https://peps.python.org/pep-0257/>`__
but *in practice* we use:

- for modules: triple double-quotes (``"""``) at the beginning of the
  module
- for classes: triple double-quotes immediately below the ``class``
  statement
- for methods/function: triple double-quotes immediately below the
  ``def`` statement

.. note:: Not all comments are docstrings. Use docstrings for 
   documenting the API, and other comments for adding information
   on implementation details.

Consider the following function:

.. code:: python

   def negate(x:float) -> float:
       """Negates the argument
       
       For example:
    
           >>> negate(3)
           -3
       """
       return -x

Then, on a **python** terminal you can use the ``help()`` function::

   >>> help(negate)

   Help on function negate in module __main__:

   negate(x: float) -> float
       Negates the argument
       
       For example:
       
           >>> negate(3)
           >>> -3

And on **iPython** you can use ``?``::

   In [1]: negate?
   Signature: negate(x: float) -> float
   Docstring:
   Negates the argument

   For example:

       >>> negate(3)
       -3
   File:      ~/<ipython-input-18-c837aa6f0da6>
   Type:      function

Programmatically, the docstring of an object is stored in its
``__doc__`` member:

.. code:: python

   >>> negate.__doc__
   'Negates the argument\n    \n    For example:\n \n        >>> negate(3)\n        >>> -3\n    '

Auto-generating browsable API docs from your code docstrings
------------------------------------------------------------

If you want to autogenerate documentation from your docstrings, you may
use the sphinx ``autoapi`` extension and **write your docstrings using
valid reStructuredText**.

Style and conventions in docstrings
-----------------------------------

.. note:: here I'll use the "native" reStructuredText style. Other popular styles
   are the *numpy* and *google* styles which are supported by the
   `“napoleon” sphinx
   extension <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.htm>`__.

For a function/method I recommend the following template:

.. code:: python

   def <FunctionName>(<ParamName>: <ParamTypeHint>, ...): -> <ReturnTypeHint>
       """<Short summary tile in imperative tense>.

       <Optional multi-line description, possibly with examples and cross-references>

       :param <ParamName>: <Concise but complete parameter description, including default value>
       ...
       :raises <ExceptionType>: <Condition in which this exception is raised>
       ...
       :return: <Concise but complete description of the return value>
       """

.. note:: in some examples of sphinx reStructuredText (e.g. `this <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`__)
   you may see other fields such as ``:type <ParamName>: <ParamType>``
   or ``:rtype: <ReturnType>`` but **they can be ommitted if you use
   type hints** and add ``autodoc_typehints = "description"`` to the sphinx ``conf.py``


Tips to keep in mind when writing docstrings
--------------------------------------------

1.  Use a concise "title phrase" in the string. If you need to provide more details, 
    leave a blank line and provide them in a paragraph below.
2.  The title in a function docstring should be in imperative form (e.g., "Return the path 
    of..." and **not** “Returns the path of...”), and end with a period.
3.  If the docstring is a one-liner, keep the closing quotes in the same line.
4.  Do not reiterate the information that can be obtained from the function signature 
    (the names/types of the args, the return type,...)
5.  When describing a parameter for sphinx autoapi, do not mention the type. This info 
    is already available from the type hints.
6.  When describing a parameter that has a default value, mention it.
7.  Describe your object **from an user point of view**. Do not describe implementation 
    details unless they are relevant for the end-user.
8.  Providing usage examples in code snippets is always very useful (tip: copy the snippet
    from an interactive python session, including the ``>>>`` prompt)
9.  If a parameter or a return value is complex (e.g. a heterogenous tuple or dict) provide
    an accurate description of its members and, if possible, an example.
10. Double-check your docstrings for typos, spelling or grammar issues. And unless agreed 
    otherwise in the project, use English for your docstrings, comments, object names, etc.

Example
-------

See the code of the ``src/myproject/intcalc.py`` file included in this repo as an example:

.. literalinclude:: ../../src/myproject/intcalc.py

Automating doc builds (CI)
==========================

If your project uses sphinx, it is easy to set up your Continuous
Integration (CI) tool (e.g. a Github Actions workflow) to automatically
build the docs for your project on, e.g., each push to your repo.

This serves 2 purposes: 
- check for syntax correctness in your doc sources 
- provide ready-built documentation for each version or release of your code

Example
-------

A very basic workflow for building and uploading the html docs of this project to github artifacts
can be seen in the ``.github/workflows/docs.yml`` 


.. literalinclude:: ../../.github/workflows/docs.yml
   :language: yaml

Further reading
===============

-  `Guide for documenting Python
   code <https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings>`__
