How to use?
===========

You can import jQuery from ``js.jquery`` and ``need`` it where you want
these resources to be included on a page::

  >>> from js.jquery import jquery
  >>> jquery.need()

There is also the slim version (which excludes the ajax and effects modules):

  >>> from js.jquery import jquery_slim
  >>> jquery_slim.need()


.. _`fanstatic`: http://fanstatic.org
