==========
# Practice implementations of various algorithms
==========
```


Description
===========

From basic, textbook to advanced

Python, C++, and others


Typical Python module file layout from this [StackOverFlow](http://stackoverflow.com/questions/15237806/python-modules-hierarchy-naming-convention)

```python
/some-parent-directory # This needs to be on sys.path, the name doesnot matter indeed
    /module
        __init__.py  # import module
        # init is loaded when you `import module` or anything below it
        some.py  # import module.some
        implementation.py  # import module.implementation
        files.py  # import module.files
        /submodule
            __init__.py  # import module.submodule
            # init is loaded when you `import module.submodule` or anything below it
            submodule_impl.py  # import module.submodule.submodule_impl
            goes.py  # import module.submodule.goes
            here.py  # import module.submodule.here


Note
====

This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
