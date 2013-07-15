523
===
This is a set of python scripts specific to our apartment, but others are welcome to use our work as an example for their home Philips Hue automation.

This requires Python 2.7 and the phue package https://github.com/studioimaginaire/phue

### Usage ###

This is less of a program and more of a library file for helping with integration of your python scripts with philips hue using the phue plugin.

To use this in one of your scripts, simply include the line:

```python
execfile('523.py')
```

at the beginning of your code.  This will register your application with the hue base station and add functions for interacting with lights

### Notes ###

This script is currently not generic, it features settings specific to our apartment, which can serve as implementation examples
