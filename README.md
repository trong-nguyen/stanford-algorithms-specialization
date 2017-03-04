==========
# Practice implementations of various algorithms
==========


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
```

Note
====

This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.

Add to the `[files]` command in `setup.cfg` the following:

```
namespace_packages =
	top_namespace
```

to add `top_namespace` to the top of your packages

More about [namespace_packages](http://stackoverflow.com/questions/1675734/how-do-i-create-a-namespace-package-in-python) and directory structure.

More about using `setup.cfg` [here](http://stackoverflow.com/questions/27077355/how-to-use-setup-cfg-instead-of-setup-py-with-python-2-7), which basically says that `setup.cfg` file does not provide parameters to the `setup.py` function. It is used to supply parameters to the commands that `setup.py` makes available.
Sample of a fully annotated `setup.cfg` [here](https://www.stsci.edu/svn/ssb/stsci_python/stsci.samplepackage/trunk/setup.cfg.sample)