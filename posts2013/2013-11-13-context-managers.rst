===========================================
Managing Connections with Context Managers
===========================================

:date: 2013-11-14 12:00
:tags: python
:category: blog
:slug: managing-connections-with-context-managers
:status: draft

The purpose of this is to show how easy it is to write context managers

Recently I was asked to write a context manager. It was my first experience writing one, . This really nice example made it possible for me to stop being simply a user of context managers, and instead become an author. So I've decided to share my newfound ability.

In any case, the goal of this particular context manager is to not only wrap up a database connection in a function, but to do it in such a way that when the use of the function is completed, Python would close the connection automatically at the end of a code block. This kind of behavior is a common use case for context managers.

Below is a simple yet heavily commented example of how to write a context manager. 

.. code-block:: python
    :linenos:

    # connections.py
    
    # contextlib is in Python's standard library as of Python 2.x.
    import contextlib

    # This is a mythical connection library to a mythical database that
    #   requires a `.close()` method.
    import holidaylib
    
    @contextlib.contextmanager
    def holidaylib_conn(dsn):
        try:
            # Establish the connection
            conn = holidaylib.connect(dsn)
            
            # Yield the result. When the context manager is closed, this means 
            #   the execution returns to right after this spot.
            yield conn
            
            # THIS IS WHERE CODE EXECUTION RETURNS UPON CLOSING OF THE BLOCK
            
        except holidaylib.OOPS as e:
            # Do special error handling here as needed, and ideally log the 
            #   problem.
            pass

        finally:
            # Close the connection on errors.
            conn.close()
            
            # re-raise the error so it can be handled by the rest
            # of the project
            raise e
            
        # Close the connection for valid use of library
        conn.close()
        
What allows us to do is write code like this:

.. code-block:: python

    from connections import holidaylib_connector
    
    # This statement does the following:
    #   1. Set up the connection per line 14 in connections.py
    #   2. Yields the result per line 18 in connections.py
    with holidaylib_connector("...") as conn:
    
        # Use the returned `conn` object to get data
        toys = conn.get_toys()
        
        # As this code block ends, return from the yield
        # This returns us to line 21 WHICH IS IN ALL CAPS

    # Iterate through the results
    for toy in toys:
    
        # Display the results
        print("I want ", toy.title)

What I really like about these two code samples is that together they explain the way that Python's `context managers` work. As a bonus, they also provide a not-so-bad reference for how to write a generator using the `yield` keyword.

Many thanks go to FW.