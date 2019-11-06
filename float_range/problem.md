# float_range

<p>This week I'd like you to write a callable object called <code>float_range</code> that acts sort of like the built-in <code>range</code> callable but allows for floating point numbers to be specified.</p>
<p>I say "callable" instead of "function" or "class" because I don't actually care how you implement this thing.
What I care about is that you can call it and loop over the resulting items.</p>
<p>It should work like this:</p>
<pre><code class="pycon">&gt;&gt;&gt; for n in float_range(0.5, 2.5, 0.5):
...     print(n)
...
0.5
1.0
1.5
2.0
&gt;&gt;&gt; list(float_range(3.5, 0, -1))
[3.5, 2.5, 1.5, 0.5]
</code></pre>

<p>Your <code>float_range</code> callable should also allow the step and start arguments to be optional, the same way they are for Python's built-in <code>range</code> callable:</p>
<pre><code class="pycon">&gt;&gt;&gt; for n in float_range(0.0, 3.0):
...     print(n)
...
0.0
1.0
2.0
&gt;&gt;&gt; for n in float_range(3.0):
...     print(n)
...
0.0
1.0
2.0
</code></pre>

<p>I also want you to make sure that calling <code>float_range</code> doesn't create a large list of numbers.
By this I mean that calling <code>float_range</code> should be memory-efficient.
Return an iterator or a generator or some kind of lazy object, not a list.</p>
<p>There are three bonuses this week.
Please make sure to attempt the base problem first before attempting any of the bonuses this week.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, I'd like you to make sure the object you get back when calling <code>float_range</code> has a length ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; len(float_range(0.5, 2.5, 0.5))
4
</code></pre>

<p>A hint for the first bonus: if you were using a generator function before, you're probably going to need to switch to creating a <code>float_range</code> class now instead.</p>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, I'd like you to make sure the object is reversible with the built-in reversed function ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; list(reversed(float_range(0.5, 2.5, 0.5)))
[2.0, 1.5, 1.0, 0.5]
</code></pre>

<p><strong>Bonus 3</strong></p>
<p>For the third bonus, I'd like you to make sure that you can take the object returned from <code>float_range</code> and ask if it's equal to another object returned from <code>float_range</code> ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; a = float_range(0.5, 2.5, 0.5)
&gt;&gt;&gt; b = float_range(0.5, 2.5, 0.5)
&gt;&gt;&gt; c = float_range(0.5, 3.0, 0.5)
&gt;&gt;&gt; a == b
True
&gt;&gt;&gt; a == c
False
</code></pre>

<p>In fact I'd like you to take that a step further and make sure that <code>float_range</code> can be compared to <code>range</code> objects and that it allows other objects to be compared to itself without raising an exception:</p>
<pre><code class="pycon">&gt;&gt;&gt; float_range(5) == range(0, 5)
True
&gt;&gt;&gt; float_range(4) == range(5)
False
</code></pre>

<p><strong>Hints</strong></p>
<p>Here are some hints you can use <strong>when you get stuck</strong> (hover over links to see what they're about):</p>
<ul>
<li><a href="https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/" title="An article I wrote on what callables are">What are callables?</a></li>
<li><a href="https://stackoverflow.com/a/51676957/2633215" title="Writing a range-like function">An example solution</a></li>
<li><a href="https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions" title="Making default values for optional arguments">Managing optional arguments</a></li>
<li><a href="https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/#Generators:_the_easy_way_to_make_an_iterator" title="Creating you own iterators using generators">Returning an iterator</a></li>
<li><a href="https://www.youtube.com/watch?v=ZDa-Z5JzLYM/" title="A video on writing classes in Python">Classes and object-oriented programming</a></li>
<li><a href="https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/" title="A detailed walkthrough of what iterables and iterators are in Python">Understanding iterators in detail</a></li>
<li><a href="https://stackoverflow.com/questions/15114023/using-len-and-def-len-self-to-build-a-class" title="To make an iterable with a length, you'll need a __len__ method">Returning length of custom object</a></li>
<li><a href="https://code.activestate.com/recipes/577624/" title="You'll need to implement a __reversed__ method">A reversible iterable</a></li>
<li><a href="https://stackoverflow.com/a/25176504/98187" title="A discussion comparing the equality of objects">Implementing equality checks</a></li>
</ul>

<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/03a551781d7548539d42897e5e8a1519/tests/">can be found here</a>.
You'll need to write your function in a module named float_range.py next to the test file.
To run the tests you'll run "python test_float_range.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>
