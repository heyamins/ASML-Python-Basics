Python 3.9.12 (main, Jun  1 2022, 06:34:44) 
[Clang 12.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> 
= RESTART: /Users/peter/Computrain/_InCompany/ASML/Python with Python Crash Course/Sandbox/turtle.py
Traceback (most recent call last):
  File "/Users/peter/Computrain/_InCompany/ASML/Python with Python Crash Course/Sandbox/turtle.py", line 1, in <module>
    import turtle
  File "/Users/peter/Computrain/_InCompany/ASML/Python with Python Crash Course/Sandbox/turtle.py", line 3, in <module>
    turtle.forward(100)
AttributeError: partially initialized module 'turtle' has no attribute 'forward' (most likely due to a circular import)
>>> 