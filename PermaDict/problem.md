<h1 class="display-3">PermaDict</h1>
<div class="row">
  <div class="col-md-8">
    

<p>Hi there!</p>





<p>This week you're going to create a dictionary-like class that disallows keys
to be updated (they can only be added or removed).</p>
<p>The PermaDict class should allow keys to be added and deleted, just like any
other dictionary:</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
&gt;&gt;&gt; locations['Harry'] = "London"
&gt;&gt;&gt; locations.update({'Russell': "Perth", 'Katie': "Sydney"})
&gt;&gt;&gt; locations['Trey']
'San Diego'
</code></pre>

<p>And your PermaDict class should have keys, values, and items methods and
should be iterable just like a dictionary:</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
&gt;&gt;&gt; list(locations)
['Kojo', 'Tracy']
&gt;&gt;&gt; list(locations.keys())
['Kojo', 'Tracy']
&gt;&gt;&gt; list(locations.values())
['Houston', 'Toronto']
&gt;&gt;&gt; for name, place in locations.items():
...     print(f"{name} in {place}")
...
Kojo in Houston
Tracy in Toronto
</code></pre>

<p>But unlike a dictionary when a value is set and for a key that already exists,
a KeyError exception should be raised:</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict({'David': "Boston"})
&gt;&gt;&gt; locations['David'] = "Amsterdam"
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 5, in __setitem__
KeyError: "'David' already in dictionary."
&gt;&gt;&gt; locations['Asheesh'] = "Boston"
&gt;&gt;&gt; locations.update({'Asheesh': "San Francisco"})
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 5, in update
KeyError: "'Asheesh' already in dictionary."
&gt;&gt;&gt; locations
{'David': 'Boston', 'Asheesh': 'Boston'}
</code></pre>

<p>For the first bonus, I'd like you to add a force_set method to your PermaDict
class which allows keys to be updated without error. ✔️</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict({'David': "Boston"})
&gt;&gt;&gt; locations.force_set('David', "Amsterdam")
&gt;&gt;&gt; locations.force_set('Asheesh', "Boston")
&gt;&gt;&gt; locations.force_set('Asheesh', "San Francisco")
&gt;&gt;&gt; locations
{'David': 'Amsterdam', 'Asheesh': 'San Francisco'}
</code></pre>

<p>For the second bonus, I'd like you to handle an optional "silent" keyword
argument passed to the initializer of your dictionary to allow your dictionary
to silently ignore updates to existing keys. ✔️</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict({'David': "Boston"}, silent=True)
&gt;&gt;&gt; locations['David'] = "Amsterdam"
&gt;&gt;&gt; locations['Asheesh'] = "Boston"
{'David': 'Boston', 'Asheesh': 'Boston'}
</code></pre>

<p>For the third bonus, I'd like your PermaDict class's update method to handle
an optional "force" keyword argument to allow your dictionary's update method
to force update the values for existing keys. ✔️</p>
<pre><code>&gt;&gt;&gt; locations = PermaDict({'David': "Boston"})
&gt;&gt;&gt; locations.update([('David', 'Amsterdam'), ('Asheesh', 'SF')], force=True)
&gt;&gt;&gt; locations
{'David': 'Amsterdam', 'Asheesh': 'SF'}
</code></pre>

<p>A hint for this week: you'll want to use inheritance. You don't want to
implement all these methods from scratch.</p>

<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/8af36190041948ab95acd297841a4ea5/tests/">can be found here</a>.
You'll need to write your function in a module named permadict.py next to the test file.
To run the tests you'll run "python test_permadict.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>



  </div>
</div>

