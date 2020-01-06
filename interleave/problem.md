<h1 class="display-3">interleave</h1>
        
<h5>Assigned from Intermediate Level on 12/30/2019</h5>

<div class="row">
  <div class="col-md-8">
   
<p>Hello!</p>
<p>For this week's problem, I want you to write a function called <code>interleave</code> which accepts two iterables of any type and return a new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).</p>
<p>We are making an assumption here that both iterables contain the same number of elements.</p>
<p>Here's an example:</p>
<pre><code class="pycon">&gt;&gt;&gt; numbers = [1, 2, 3, 4]
&gt;&gt;&gt; interleave(numbers, range(5, 9))
[1, 5, 2, 6, 3, 7, 4, 8]
&gt;&gt;&gt; interleave(numbers, (n**2 for n in nums))
[1, 1, 2, 4, 3, 9, 4, 16]
</code></pre>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, your <code>interleave</code> function should return <a href="https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/">an iterator</a>  ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; i = interleave([1, 2, 3, 4], [5, 6, 7, 8])
&gt;&gt;&gt; next(i)
1
&gt;&gt;&gt; list(i)
[5, 2, 6, 3, 7, 4, 8]
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For second bonus your <code>interleave</code> function should accept any number of arguments ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])
[1, 4, 7, 2, 5, 8, 3, 6, 9]
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, your <code>interleave</code> function should work with iterables of different lengths.
Short iterables should be skipped over once exhausted ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; interleave([1, 2, 3], [4, 5, 6, 7, 8])
[1, 4, 2, 5, 3, 6, 7, 8]
&gt;&gt;&gt; interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])
[1, 4, 6, 2, 5, 7, 3, 8, 9]
</code></pre>
<p><strong>Hints</strong></p>
<p>If you <strong>get stuck</strong> this week, give these hints a try:</p>
<ul>
<li><a href="https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/" title="use the built-in zip function">Looping over multiple things at once</a></li>
<li><a href="https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/" title="use a generator function">Creating an iterator</a></li>
<li><a href="https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/" title="using asterisks to accept unlimited arguments">Any number of arguments</a></li>
<li><a href="https://docs.python.org/3.6/library/functions.html#zip" title="implementation of the built-in zip function">Hint for bonus 3</a></li>
<li><a href="https://docs.python.org/3/library/itertools.html#itertools.zip_longest" title="You might want to use zip_longest with a sentinel value">A tool to help you solve bonus 3</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/db5f9e6add674a26aa384c6fe302400c/tests/">can be found here</a>.
You'll need to write your code in a module named interleave.py next to the test file.
To run the tests you'll run "python test_interleave.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>
  </div>
</div>





