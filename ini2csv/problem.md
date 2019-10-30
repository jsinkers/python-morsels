# ini2csv.py

I'd like you to create a program, ini2csv.py, which accepts an INI-like file and converts it to a CSV-like file.

The input files will look like this (this is an [EditorConfig](http://editorconfig.org/) file):
```
[*.py]
indent_style = space
indent_size = 4

[*.js]
indent_style = space
indent_size = 2
```

Given that input file, .editorconfig, executing our program like this:

```
$ python ini2csv.py .editorconfig editorconfig.csv
```

Will produce an output file, editorconfig.csv, like this:
```
*.py,indent_style,space
*.py,indent_size,4
*.js,indent_style,space
*.js,indent_size,2
```

## Bonus 1

There's just one bonus this week. For the bonus, I'd like you to accept a --collapsed argument that, when present, will collapse the rows to one row per section.

So this:

```
$ python ini2csv.py --collapsed .editorconfig editorconfig.csv
```

Will result in a editorconfig.csv file that contains this:

```
header,indent_style,indent_size
*.py,space,4
*.js,space,2
```

## Hints

- [Reading command-line arguments](https://stackoverflow.com/a/35421024/2633215)
- [Closing files automatically](https://pythonpedia.com/en/tutorial/928/context-managers-with-statement-#introduction-to-context-managers-and-the-with-statement)
- [Writing CSV files](https://pymotw.com/3/csv/)
- [Parsing INI files](https://docs.python.org/3/library/configparser.html#module-configparser)
- [Parsing command-line flags](http://zetcode.com/python/argparse/)

## Tests

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named ini2csv.py next to the test file. To run the tests you'll run "python test_ini2csv.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.