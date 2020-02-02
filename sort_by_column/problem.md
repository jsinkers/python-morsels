# Sort by Column

<p>Hey!</p>
<p>This week I'd like you to write a command-line program, <code>sort_by_column.py</code> that will read a CSV file, sort it by a given column number, and print out the resulting sorted rows.</p>
<p>Given the following CSV file, called <code>colors.csv</code>:</p>
<pre><code class="csv">red,4
blue,3
green,8
purple,1
</code></pre>
<p>Calling <code>sort_by_column.py</code> to sort by the first column and then by the second columns would look like this:</p>
<pre><code class="bash">$ python sort_by_column.py colors.csv 0
blue,3
green,8
purple,1
red,4
$ python sort_by_column.py colors.csv 1
purple,1
blue,3
red,4
green,8
</code></pre>
<p>Note that <code>sort_by_column.py</code> should print out the resulting sorted CSV file, but should not change the original CSV file.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, I'd like you to accept multiple columns to sort by. ✔️</p>
<p>For example given this <code>cars.csv</code> file:</p>
<pre><code class="csv">2011,Volkswagen,Golf
2013,Toyota,Prius
2011,Toyota,Corola
2012,Volkswagen,Golf
2011,Toyota,Prius
</code></pre>
<p>Sorting on the first and third columns would work like this:</p>
<pre><code class="bash">$ python sort_by_column.py cars.csv 0 2
2011,Toyota,Corola
2011,Volkswagen,Golf
2011,Toyota,Prius
2012,Volkswagen,Golf
2013,Toyota,Prius
</code></pre>
<p>And sorting on the first, second, and third columns would work like this:</p>
<pre><code class="bash">$ python sort_by_column.py cars.csv 0 1 2
2011,Toyota,Corola
2011,Toyota,Prius
2011,Volkswagen,Golf
2012,Volkswagen,Golf
2013,Toyota,Prius
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, I'd like you to accept a <code>--with-header</code> argument that will treat the first row as a header by keeping it in place. ✔️</p>
<p>So if <code>cars.csv</code> looked like this:</p>
<pre><code class="csv">Year,Make,Model
2011,Volkswagen,Golf
2013,Toyota,Prius
2011,Toyota,Corola
2012,Volkswagen,Golf
2011,Toyota,Prius
</code></pre>
<p>Our program would allow for this:</p>
<pre><code class="bash">$ python sort_by_column.py cars.csv --with-header 1 2 0
Year,Make,Model
2011,Toyota,Corola
2011,Toyota,Prius
2013,Toyota,Prius
2011,Volkswagen,Golf
2012,Volkswagen,Golf
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, I'd like you to accept an optional column type to allow customizing the way columns are sorted.  The accepted column types should include <code>str</code> (the default) and <code>num</code> (which will sort columns as if they are numeric). ✔️</p>
<p>Given a <code>colors.csv</code> file like this:</p>
<pre><code class="csv">red,4
yellow,3
blue,10
green,8
purple,1
</code></pre>
<p>Sorting based on the second column, numerically should work like this:</p>
<pre><code class="bash">$ python sort_by_column.py colors.csv 1:num
purple,1
yellow,3
red,4
green,8
blue,10
</code></pre>
<p>Note that <code>10</code> would come before <code>3</code> if sorting columns as strings and not as numbers.</p>
<p><strong>Hints</strong></p>
<ul>
<li><a href="https://stackoverflow.com/a/35421024/2633215" title="You can see command-line arguments given to your program with sys.argv">How to access command-line arguments</a></li>
<li><a href="https://stackoverflow.com/a/642169/2633215" title="The int built-in function converts strings to integers">Converting strings to numbers</a></li>
<li><a href="https://twitter.com/treyhunner/status/1217897814690279425" title="Using open in a with block will automatically close your files">Auto-closing files in Python</a></li>
<li><a href="https://pymotw.com/3/csv/index.html" title="csv.reader returns data, row by row, from any iterable of lines">Reading CSV data row-by-row</a></li>
<li><a href="https://treyhunner.com/2020/01/passing-functions-as-arguments/#A_common_example:_key_functions" title="The built-in sorted function can accept a key function which returns the column to sort by">Sorting by a specific column</a></li>
<li><a href="https://stackoverflow.com/q/23665264/2633215" title="If you pass sys.stdoutto csv.writer, it'll write to standard output which will print to your terminal">Printing out CSV data</a></li>
<li><a href="https://treyhunner.com/2019/03/python-deep-comparisons-and-code-readability/#Sorting_by_multiple_attributes_at_once" title="You can sort by multiple columns by making a key function that returns a tuple">Bonus 1: sorting by multiple columns</a></li>
<li><a href="https://stackoverflow.com/questions/8259001/python-argparse-command-line-flags-without-arguments/8259080#8259080" title="It'll be easier to use argparse rather than reading from sys.argv at this point">Bonus 2: Checking for the <code>--with-header</code> CLI argument</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/7cb92f3eea134a0899d0098aa2efbd3a/tests/">can be found here</a>.
You'll need to write your function in a module named sort_by_column.py next to the test file.
To run the tests you'll run "python test_sort_by_column.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>

