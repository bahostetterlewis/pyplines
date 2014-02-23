Pyplines
========

**Unix pipeline syntax in Python!**

To use simply

```python
from pypline import pypline
```

Then decorate generators to use with the pypline!

Examples
--------

```python
#simple filtering of numbers by divisibility
from pypline import pypline
from pypline import display

@pypline
def even(iter):
    '''
    Note - param 1 is needs to take an iterable for this to work! This is the only 
    real requirement
    '''
    for value in iter:
        if value % 2 == 0:
            yield value

@pypline
def divisible(iter, divis_value):
    for value in iter:
        if value % divis_value == 0:
            yield value

#We need a data generator to start the pipeline (any will do!)
#Then we pyp it along to other data consumers
#Finally, display ( a built in pypline consumer) will display images to the terminal
#Finally, pypline members can either take parameters or be parameterless
range(10) | even | divisible(3) | display
```

Convenience Functions
---------------------
* `sort`<br>takes an optional key function (exactly like sorted)
* `display`<br>takes an optional file argument for redirecting