SPOJ problems' solutions in Python
==================================

My attempt to solve SPOJ's problems, http://www.spoj.com/problems/, in Python.
Solution named in `problem_name.py` in which `problem_name` comes from the URL
at SPOJ, i.e The solution for http://www.spoj.com/problems/TEST/ is named
`test.py` with `test.in` as an input and `test.out` as an expected output. To
run the test, you can do something like:

~~~
$ cat test.in | ./test.py | diff - test.out
~~~

If you don't get any output then test passed. But if you get something printed
then the output from `test.py` doesn't match with expected output. But, I'll
make sure all solutions in this repo are tested and passed.

## TODO

- Add LICENSE, but state the problems belongs to SPOJ or its author.
- Add run_all_tests
- Add problem URL at the top of source code
