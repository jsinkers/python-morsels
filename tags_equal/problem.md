<div class="container content-wrapper">

<div class="row">
    <div class="col-md-8">
        <h1 class="display-3">tags_equal</h1>
        
        <h5>Assigned from Intermediate Level on 12/09/2019</h5>
        
    </div>
</div>

<div class="row">
  <div class="col-md-8">
    

<p>Hey friend!</p>
<p>This week's exercise might seem a bit uninteresting at first because it involves working with an HTML-like syntax at a low level.
The purpose this week <em>isn't</em> to familiarize yourself with HTML, but to get some practice with string manipulation in Python.</p>
<p>This week I'd like you to write a function that accepts two strings containing opening HTML tags and returns True if they have the same attributes with the same values.</p>
<p>Some examples of basic tag comparisons I'd like you to handle:</p>
<pre><code class="pycon">&gt;&gt;&gt; tags_equal("&lt;img src=cats.jpg width=20&gt;", "&lt;IMG SRC=Cats.JPG height=40")
True
&gt;&gt;&gt; tags_equal("&lt;img src=dogs.jpg width=99&gt;", "&lt;img src=dogs.jpg width=20&gt;")
False
&gt;&gt;&gt; tags_equal("&lt;p&gt;", "&lt;P&gt;")
True
&gt;&gt;&gt; tags_equal("&lt;b&gt;", "&lt;p&gt;")
False
</code></pre>

<p>This might sound complex and it sort of is.</p>
<p>To make things a little easier:</p>
<ol>
<li>Assume attributes don't have double/single quotes around them and don't contain spaces (until you get bonus 3)</li>
<li>Don't worry about repeated attribute names or value-less attributes.
     Assume there won't be repeats (until you get to bonus 1)</li>
<li>Assume all attributes are key-value pairs (until you get to bonus 2)</li>
<li>Assume attributes have no whitespace around them (key=value and never key = value)</li>
</ol>
<p>But your function must:</p>
<ol>
<li>Ignore order of attributes: the same attribute names/values in different order should be equivalent</li>
<li>Ignore case for both attribute names and values (yes even ignore case for attribute values)</li>
</ol>
<p>I encourage you to try solving this exercise without using the standard library at first.
Everything but the last bonus should be relatively do-able without importing any libraries.</p>
<p>If you get your tests to pass, consider doing some of these bonuses.
Make sure you don't spend too much time trying to get the second or third bonus done though.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, I'd like you to handle duplicate attribute names by allowing the  <em>first</em>  one to "win" (ignoring any before the last) ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; tags_equal("&lt;LABEL FOR=id_email for=id_username&gt;", "&lt;LABEL FOR=id_email&gt;")
True
&gt;&gt;&gt; tags_equal("&lt;LABEL FOR=id_email for=id_username&gt;", "&lt;LABEL FOR=id_username&gt;")
False
</code></pre>

<p><strong>Bonus 2</strong></p>
<p>For the second bonus, I'd like you to allow attributes without a value ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; tags_equal("&lt;OPTION NAME=Hawaii SELECTED&gt;", "&lt;option selected name=hawaii&gt;")
True
&gt;&gt;&gt; tags_equal("&lt;option name=hawaii&gt;", "&lt;option name=hawaii selected&gt;")
False
</code></pre>

<p><strong>Bonus 3</strong></p>
<p>For the third bonus I'd like you to handle single/double quotes around attribute values and attribute values to have spaces in them ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; tags_equal("&lt;input value='hello there'&gt;", '&lt;input value="hello there"&gt;')
True
&gt;&gt;&gt; tags_equal("&lt;input value=hello&gt;", "&lt;input value='hello'&gt;")
True
&gt;&gt;&gt; tags_equal("&lt;input value='hi friend'&gt;", "&lt;input value='hi there'&gt;")
False
</code></pre>

<p>That last bonus may be pretty tricky and I recommend you reach for the standard library if you attempt it.</p>
<p><strong>Hints</strong></p>
<ul>
<li><a href="https://stackoverflow.com/questions/509211/understanding-slice-notation/509295" title="Slicing a string can omit particular characters from it">Getting rid of <code>&lt;</code> and <code>&gt;</code></a></li>
<li><a href="https://stackoverflow.com/a/20985070/2633215" title="The string split method splits a string into a list">Parsing an HTML tag-like string</a></li>
<li><a href="https://treyhunner.com/2019/03/python-deep-comparisons-and-code-readability/#Deep_equality" title="You can use Python's == operator to compare the items in lists">Comparing two lists for equality</a></li>
<li><a href="https://stackoverflow.com/a/50699005/2633215" title="You can sort lists to compare them for equality">Comparing lists while ignoring their element order</a></li>
<li><a href="https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/" title="You might find multiple assignment useful for this problem">Avoiding hard-coded indexes</a></li>
<li><a href="https://gist.github.com/pandeytapan/9649ec827e952f2e9a9a391a5e9632df#file-tags_equal_hints_bonus-1-1-md" title="Grouping items in dictionaries can help remove duplicates">Getting rid of duplicate attributes</a></li>
<li><a href="https://stackoverflow.com/a/38149500/2633215" title="The string partition method always returns a three item tuple">Splitting when a value is missing</a></li>
<li><a href="http://pycon2017.regex.training/" title="A three hour tutorial on regular expressions">Regular expressions to find quoted attributes</a></li>
<li><a href="https://stackoverflow.com/a/34679668/2633215" title="The shlex.split function can split a string in a quote-aware way">A handy tool for quote-aware string splitting</a></li>
<li><a href="https://docs.python.org/3/library/html.parser.html" title="An HTML parser class inherited from html.parser.HTMLParser">Parsing HTMl with the standard library</a></li>
</ul>

<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/24ce703aa77646cc881b0837d5be2391/tests/">can be found here</a>.
You'll need to write your function in a module named tags_equal.py next to the test file.
To run the tests you'll run "python test_tags_equal.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>



  </div>
</div>
