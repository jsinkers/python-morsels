<h1 class="display-3">format_fixed_width</h1>
        
<h5>Assigned from Intermediate Level on 01/20/2020</h5>
        
<div class="row">
  <div class="col-md-8">
    
<p>Hey there,</p>
<p>This week I'd like you to write a function, <code>format_fixed_width</code>, that accepts rows of columns (as a list of lists) and returns a fixed-width formatted string representing the given rows.</p>
<p>For example:</p>
<pre><code class="pycon">&gt;&gt;&gt; print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
green  red
blue   purple
</code></pre>
<p>The padding between the columns should be 2 spaces.
Whitespace on the right-hand side of each line should be trimmed and columns should be left-justified.</p>
<p><strong>Bonus #1</strong></p>
<p>For the first bonus, allow the padding for columns to be specified with an optional <code>padding</code> keyword argument:</p>
<pre><code class="pycon">&gt;&gt;&gt; rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
&gt;&gt;&gt; print(format_fixed_width(rows))
Robyn     Henry    Lawrence
John      Barbara  Gross
Jennifer           Bixler
&gt;&gt;&gt; print(format_fixed_width(rows, padding=1))
Robyn    Henry   Lawrence
John     Barbara Gross
Jennifer          Bixler
&gt;&gt;&gt; print(format_fixed_width(rows, padding=3))
Robyn      Henry     Lawrence
John       Barbara   Gross
Jennifer              Bixler
</code></pre>
<p><strong>Bonus #2</strong></p>
<p>For the second bonus, allow column widths to be specified manually with an optional <code>widths</code> keyword argument:</p>
<pre><code class="pycon">&gt;&gt;&gt; rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
&gt;&gt;&gt; print(format_fixed_width(rows, widths=[10, 10, 10]))
Jane                    Austen
Samuel      Langhorne   Clemens
</code></pre>
<p><strong>Bonus #3</strong></p>
<p>For the third bonus, allow column justifications (left or right) to be specified with with an optional <code>alignments</code> keyword argument.
This argument will take lists of <code>'L'</code> and <code>'R'</code> strings representing left and right:</p>
<pre><code class="pycon">&gt;&gt;&gt; print(format_fixed_width(rows, alignments=['R', 'L', 'R']))
  Jane              Austen
Samuel  Langhorne  Clemens
</code></pre>
<p><strong>Hints</strong></p>
<ul>
<li><a href="https://docs.python.org/3/library/functions.html#max" title="You could use the built-in max function to find the longest cell in a given column">Getting the longest string</a></li>
<li><a href="https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/#What_if_we_need_to_loop_over_multiple_things?" title="The built-in zip function allows you to loop over multiple iterables at the same time">Looping over multiple things at the same time</a></li>
<li><a href="https://stackoverflow.com/a/25373954" title="The string ljust method can left-justify a string with a given width">Left-justifying strings</a></li>
<li><a href="https://docs.python.org/3/library/stdtypes.html#str.rstrip" title="The string rstrip method removes whitespace characters from the right-hand side of a string">Removing spaces from the end of a line</a></li>
<li><a href="https://twitter.com/treyhunner/status/1214946059945988096" title="Strings have a join method">Joining rows back together</a></li>
<li><a href="https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/" title="You might want to turn your for loops into comprehensions or generator expressions">A shorthand for creating new lists from old lists</a></li>
<li><a href="https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions" title="You can make function arguments optional by providing a default value">Bonus 1: making optional function arguments</a></li>
<li><a href="https://stackoverflow.com/a/29818422" title="You can multiply strings by numbers in Python to self-concatenate them N times">Bonus 1: making a string of N whitespace characters</a></li>
<li><a href="https://stackoverflow.com/a/31389332" title="The string rjust method can right-justify strings">Bonus 3: Right-justifying strings</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/1698071a221f45b895bb9a9f9de16248/tests/">can be found here</a>.
You'll need to write your function in a module named format_fixed_width.py next to the test file.
To run the tests you'll run "python test_format_fixed_width.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>
