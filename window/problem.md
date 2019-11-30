# window

<div class="container content-wrapper">
<div class="row">
  <div class="col-md-8">
    

<p>Hello!</p>





<p>This week I'd like you to write a function that returns "windows" of items from a given list.
Your function should take an iterable and a number <code>n</code> and return a list of tuples, each containing "windows" of <code>n</code> consecutive items.
That is, each tuple should contain the current item and the <code>n-1</code> items after it.</p>
<p>Here are some examples:</p>
<pre><code class="pycon">&gt;&gt;&gt; numbers = [1, 2, 3, 4, 5, 6]
&gt;&gt;&gt; window(numbers, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
&gt;&gt;&gt; window(numbers, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
&gt;&gt;&gt; squares = (n**2 for n in numbers)
&gt;&gt;&gt; window(squares, 4)
[(1, 4, 9, 16), (4, 9, 16, 25), (9, 16, 25, 36)]
</code></pre>

<p>Your window function should return an empty list if the given <code>n</code> is 0.
It should also be to accept strings, tuples, and any other iterables.</p>
<p>I recommend solving the base problem before any of the bonuses this week.</p>
<p><strong>Bonus 1</strong></p>
<p>As a bonus, make sure your function returns an iterator instead of a list. ✔️</p>
<pre><code>&gt;&gt;&gt; numbers = [1, 2, 3, 4, 5, 6]
&gt;&gt;&gt; next(window(numbers, 3))
(1, 2, 3)
</code></pre>

<p><strong>Bonus 2</strong></p>
<p>For a more challenging bonus, make your function works with values of <code>n</code> that are longer than the given iterable by filling the tuple with <code>None</code> values. ✔️</p>
<pre><code class="pycon">&gt;&gt;&gt; list(window([1, 2, 3], 6))
[(1, 2, 3, None, None, None)]
</code></pre>

<p><strong>Bonus 3</strong></p>
<p>If you manage to solve all of that in the time you've scheduled for this exercise, there's one more bonus.
Allow a <code>fillvalue</code> keyword argument to be specified to be used instead of <code>None</code> when the window length is longer than the iterable: ✔️</p>
<pre><code class="pycon">&gt;&gt;&gt; list(window([1, 2, 3], 5, fillvalue=0))
[(1, 2, 3, 0, 0)]
</code></pre>

<p>Make sure that <code>fillvalue</code> only works as a named argument though.
Specifying <code>fillvalue</code> as a positional argument wouldn't be as clear and shouldn't be allowed.</p>
<p><strong>Hints</strong></p>
<p>Hints for <strong>when you get stuck</strong> (hover over links to see what they're about):</p>
<ul>
<li><a href="https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/#What_if_we_need_indexes?" title="Looping with and without indexes in Python">Looping with indexes in Python</a></li>
<li><a href="https://treyhunner.com/2019/05/python-builtins-worth-learning/#zip" title="The zip function loops over multiple iterables at once without using indexes">Looping over multiple sequences at a time</a></li>
<li><a href="https://docs.python.org/3/library/collections.html#collections.deque" title="deque objects are inexpensive for adding/removing from both the beginning and end">A queue-like data stricture</a></li>
<li><a href="http://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/" title="How iterators and iterables work in Python">The iterator protocol (what iterators are)</a></li>
<li><a href="https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/" title="Generator functions are the usual way we create functions that return iterators">Creating your own iterators</a></li>
<li><a href="https://treyhunner.com/2018/04/keyword-arguments-in-python/#Keyword-only_arguments_without_positional_arguments" title="This is a Python 3-only feature">Making keyword-only arguments</a></li>
<li><a href="https://docs.python.org/3/library/itertools.html" title="Tools for slicing iterators, chaining iterators together, and more">Helpers for working with iterators</a></li>
</ul>

<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/0b459be16d9443349c8b2e890edb0c08/tests/">can be found here</a>.
You'll need to write your code in a module named window.py next to the test file.
To run the tests you'll run "python test_window.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>



  </div>
</div>

<div class="mt-3">
  <a href="/exercises/0b459be16d9443349c8b2e890edb0c08/submit/" class="btn btn-lg btn-primary">Submit your solution</a>
  
    <a href="/exercises/0b459be16d9443349c8b2e890edb0c08/solution/" class="btn btn-lg btn-link">View solutions</a>
  
</div>







<div class="row mt-2 ng-scope" ng-app="feedback.modal" ng-controller="FeedbackCtrl as $ctrl" ng-init="$ctrl.init(105337, 'window');">
  <div class="col-md-12">
    <hr>
    <p>
      Do you <strong>have feedback</strong> on this exercise?
      Did you find a bug?
    </p>
    <p>
      <a href="#" ng-click="$event.preventDefault(); $ctrl.open()">Please tell us what you think about this exercise.</a>
    </p>
  </div>
  <!-- ngIf: successAlert -->
</div>



    </div>