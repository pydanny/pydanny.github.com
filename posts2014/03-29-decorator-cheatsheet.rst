================================
The Python Decorator Cheat Sheet
================================

:date: 2014-03-30 12:00
:tags: python, cheatsheet
:category: python
:slug: python-decorator-cheat-sheet
:status: draft

This is a cheat sheet for Python decorators, serving as a place to store decorator templates. I created this because if I go for more than a week without using decorators I have to look them up or noodle around for a bit. By placing this information on my blog it becomes a trivial lookup, either by looking at my blog locally or online.

All templates include tests. For the tests, I'm using Holger Krekel's pytest_ library, which I described in-depth `earlier this year`_. The templates and tests are available in this gist_.

.. _pytest: http://pytest.org/
.. _`earlier this year`: http://pydanny.com/pytest-no-boilerplate-testing.html
.. _gist: 

If you are looking for an in-depth tutorial to gain a full understanding of decorators, I recommend `Graham Dumpleton's excellent articles on the subject`_.

.. _`Graham Dumpleton's excellent articles on the subject`: https://github.com/GrahamDumpleton/wrapt/tree/master/blog

Decorator Function Template
=================================

Template:

.. code-block:: python

    import functools

    def decorator_function(func): # rename as needed
        @functools.wraps(func)
        def _wrapped(*args, **kwargs):
            # Before function call logic goes here
            result = func(*args, **kwargs)
            # After function call logic goes here
            return result
        return _wrapped
        
Test:

.. code-block:: python

    def test_decorator_function():
        
        @decorator_function
        def return_1():
            return 1
            
        assert return_1() == 1
        
Decorator Function with Named Arguments Template
=================================================

Template:

.. code-block:: python

    import functools

    def decorator_named_args_function(value):  # rename as needed
        def _wrapped(func):
            @functools.wraps(func)
            def _returned_wrapper(*args, **kwargs):
                print(value) # the 'value' variable is in scope
                # Before function call logic goes here
                result = func(*args, **kwargs)
                # After function call logic goes here
                return result
            return _returned_wrapper
        return _wrapped
        
Test:

.. code-block:: python

    def test_decorator_named_args_function(capsys):

        @decorator_named_args_function("Hello, world")
        def return_2():
            return 2
    
        # does function return correct value?    
        assert return_2() == 2
    
        # Did the value get printed?
        out, err = capsys.readouterr()
        assert out == "Hello, world\n"

Decorator Function with Optional Arguments Template
===================================================

Template:

.. code-block:: python

    import functools
    
    def decorator_optional_args_function(func=None, value=None): #rename
        def _wrapped(func):
            @functools.wraps(func)
            def _returned_wrapper(*args, **kwargs):
                print(value) # the 'value' variable is in scope
                # Before function call logic goes here
                result = func(*args, **kwargs)
                # After function call logic goes here
                return result
            return _returned_wrapper
        return _wrapped

Test:

.. code-block:: python

    def test_decorator_optional_args_function(capsys):
    
        @decorator_named_args_function("Spam! Spam! Spam!")
        def return_3():
            return 3

        # does function return correct value?    
        assert return_3() == 3

        # Did the value get printed?
        out, err = capsys.readouterr()
        assert out == "Spam! Spam! Spam!\n"


Basic Decorator Class Template
==============================

Template:

.. code-block:: python

    import functools 

    class ClassDecorator(object): # rename as needed
        def __init__(self, func):
            self.wrapped = func
            functools.update_wrapper(self, func)

        def __call__(self, *args, **kwargs):
            # Before function call logic goes here
            result = self.wrapped(*args, **kwargs)
            # After function call logic goes here
            return result

Test:

.. code-block:: python

    def test_ClassDecorator(capsys):
    
        @ClassDecorator
        def return_4():
            return 4

        # does function return correct value?    
        assert return_4() == 4

            
Decorator Class with Named Arguments Template
=============================================

Interestingly enough, I find this much easier to read than the functional implementation of a decorator with named arguments.

Template:

.. code-block:: python

    import functools 

    class ClassDecoratorNamedArguments(object): #rename
        def __init__(self, value):
            # set the 'value' argument as an attribute
            self.value = value

        def __call__(self, func):
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                print(self.value) # the 'value' variable is in self
                # Before function call logic goes here
                result = func(*args, **kwargs)
                # After function call logic goes here
                return result
            return wrapped

Test:

.. code-block:: python

    def test_ClassDecoratorNamedArguments(capsys):
    
        @ClassDecoratorNamedArguments(value="Python")
        def return_5():
            return 5

        # does function return correct value?    
        assert return_5() == 5
        
        # Did the value get printed?
        out, err = capsys.readouterr()
        assert out == "Python\n"

Decorator Class with Optional Arguments Template
=================================================

NOT WORKING YET!

Template:

.. code-block:: python

    import functools 

    class ClassDecoratorOptionalArguments(object): #rename
        def __init__(self, value=None):
            # set the 'value' argument as an attribute
            self.value = value

        def __call__(self, func):
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                print(self.value) # the 'value' variable is in self
                # Before function call logic goes here
                result = func(*args, **kwargs)
                # After function call logic goes here
                return result
            return wrapped


Test:

.. code-block:: python

    def test_ClassDecoratorOptionalArguments(capsys):

        @ClassDecoratorOptionalArguments(value="PEP 0318")
        def return_6():
            return 6

        # does function return correct value?    
        assert return_6() == 6

        # Did the value get printed?
        out, err = capsys.readouterr()
        assert out == "PEP 0318\n"
        
        # Try it again but without the decorator argument.
        @ClassDecoratorOptionalArguments
        def return_7():
            return 7
            
        # does function return correct value?    
        assert return_7() == 7
        
        # Did the value get printed?
        out, err = capsys.readouterr()
        assert out == "None\n"
        
Failing Test:
        
.. parsed-literal::

    ======================================================= FAILURES =======================================================
    _________________________________________ test_ClassDecoratorOptionalArguments _________________________________________

    capsys = <_pytest.capture.CaptureFixture instance at 0x1016e8950>

        def test_ClassDecoratorOptionalArguments(capsys):
    
            @ClassDecoratorOptionalArguments(value="PEP 0318")
            def return_6():
                return 6
    
            # does function return correct value?
            assert return_6() == 6
    
            # Did the value get printed?
            out, err = capsys.readouterr()
            assert out == "PEP 0318\n"
    
            # Try it again but without the decorator argument.
            @ClassDecoratorOptionalArguments
            def return_7():
                return 7
    
            # does function return correct value?
    >       assert return_7() == 7
    E       TypeError: __call__() takes at least 2 arguments (1 given)
        

Any More?
=========

Did I miss any possible argument combinations? Let me know and I'll add them!