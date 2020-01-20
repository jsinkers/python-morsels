<div class="row">
  <div class="col-md-8">
    
<p>Hello!</p>
<p>This week I'd like you to write a function, <code>condense_csv</code>, which groups CSV text by the first column.</p>
<p>The input CSV text will always contain 3 columns: ID, attribute name, attribute value.</p>
<p>Example:</p>
<pre><code class="pycon">&gt;&gt;&gt; text = """\
... ball,color,purple
... ball,size,4
... ball,notes,it's round
... cup,color,blue
... cup,size,1
... cup,notes,none"""
&gt;&gt;&gt; print(condense_csv(text, id_name='object'))
object,color,size,notes
ball,purple,4,it's round
cup,purple,1,none
</code></pre>
<p>So given a file, <code>songs.txt</code> like this:</p>
<pre><code class="pycon">01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29
</code></pre>
<p>We could get text containing a "condensed" version of this data like this:</p>
<pre><code class="pycon">&gt;&gt;&gt; print(condense_csv(open('songs.txt').read(), id_name='Track'))
Track,Artist,Title,Time
01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
</code></pre>
<p>At first you don't need to worry about our input data containing commas. Just assume all commas are column separators.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, you should handle CSV files that contain data with commas:</p>
<pre><code class="pycon">&gt;&gt;&gt; text = 'A,prop1,"value, with comma"\nA,prop2,value without comma'
&gt;&gt;&gt; print(condense_csv(text, id_name='Name'))
Name,prop1,prop2
A,"value, with comma",value without comma
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, if no <code>id_name</code> argument is specified the <code>condense_csv</code> function should consider the first column as a header and should use the first header as the <code>id_name</code>.</p>
<pre><code class="pycon">&gt;&gt;&gt; text = """\
... object,property,value
... ball,color,purple
... ball,size,4
... ball,notes,it's round
... cup,color,blue
... cup,size,1
... cup,notes,none"""
&gt;&gt;&gt; print(condense_csv(text))
object,color,size,notes
ball,purple,4,it's round
cup,purple,1,none
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, your <code>condense_csv</code> function should allow missing properties and out-of-order properties. All property columns should be presented in the order the property was first seen and missing properties should be represented with an empty string.</p>
<pre><code class="pycon">&gt;&gt;&gt; text = 'A,prop1,x\nA,prop2,y\nB,prop2,z'
&gt;&gt;&gt; print(condense_csv(text, id_name='Name'))
Name,prop1,prop2
A,x,y
B,,z
</code></pre>
<p><strong>Hints</strong></p>
<ul>
<li><a href="https://docs.python.org/3/library/stdtypes.html#str.splitlines" title="Strings have a splitlines method which is better than calling split with \n">Splitting text into lines</a></li>
<li><a href="https://www.hacksparrow.com/python/split-string-method-and-examples.html" title="You can call the string split method with , to split by commas">Getting columns from each row of text</a></li>
<li><a href="https://twitter.com/treyhunner/status/1214946059945988096" title="Strings have a join as well as a split method">Joining together column values</a></li>
<li><a href="https://treyhunner.com/2015/11/counting-things-in-python/" title="Most of the strategies discussed in this post will also work for *grouping* things">Counting occurrences in Python</a></li>
<li><a href="https://pymotw.com/3/csv/index.html" title="Doug Hellman explains Python's csv module">Bonus 1: A tool to help you not reinvent the wheel</a></li>
<li><a href="https://pymotw.com/3/io/#in-memory-streams" title="io.StringIO can take a string and make a fake file-like object">Bonus 1: You might need this for using the previous hint</a></li>
<li><a href="https://treyhunner.com/2019/05/python-builtins-worth-learning/#next" title="You can pass a file or a csv.reader object to built-in next function to get the next row of data">Bonus 2: Getting just the first row</a></li>
<li><a href="https://docs.python.org/3/library/csv.html#csv.DictWriter" title="csv.DictWriter's handles missing values using optional argument restval">Bonus 3: Handling missing properties </a></li>
<li><a href="https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby" title="You can use itertools.groupby to group consecutive values in any iterable">Bonus 3: getting values grouped by identifier</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/001564a426414354b7d0930c1dc49682/tests/">can be found here</a>.
You'll need to write your function in a module named condense_csv.py next to the test file.
To run the tests you'll run "python test_condense_csv.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>

