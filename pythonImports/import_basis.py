## A standard import
# import hello
# hello.test_function()

## A standard import, but instead of the "hello" module prior to every
## function/variable call, you just use "h"
# import hello as h
# h.test_function

## A standard import, but a module.func() call is renamed to a specified
## function call
# from hello import test_function as t, another_func as a
# t()

## Import everything from a module as is (i.e. prepend the hello 
## module to this script)
# from hello import *
# test_function()

## Prepend a specified function from the module to this script
# from hello import test_function
# test_function()

## Import a module from a specified directory
import sys
sys.path.insert(0, "./some_dir")
from yay import *
woohoo()
