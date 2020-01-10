<h1 class="display-3">EasyDict</h1>
        
<h5>Assigned from Intermediate Level on 01/06/2020</h5>

<div class="row">
  <div class="col-md-8">
<p>Hello!</p>
<p>This week I'd like you to create a class called <code>EasyDict</code> which creates objects that can use key lookups and attribute lookups interchangeably:</p>
<pre><code class="pycon">&gt;&gt;&gt; person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
&gt;&gt;&gt; person.name
'Trey Hunner'
&gt;&gt;&gt; person['location']
'San Diego'
</code></pre>
<p>At first your object should only worry about accessing keys and attributes and accepting a single dictionary as its one optional argument.</p>
<p>For the first bonus, I'd like you to make sure key and attribute assignment to works ✔️:</p>
<p><strong>Bonus 1</strong></p>
<pre><code class="pycon">&gt;&gt;&gt; person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
&gt;&gt;&gt; person.location = "Portland"
&gt;&gt;&gt; person['location']
'Portland'
&gt;&gt;&gt; person['location'] = "San Diego"
&gt;&gt;&gt; person.location
'San Diego'
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, I'd like you to also allow your <code>EasyDict</code> class to accept keyword arguments, I'd like you to make <code>EasyDict</code> objects comparable to each other via equality, and I'd like you to implement a <code>get</code> method that works sort of like the <code>get</code> method on dictionaries ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; person = EasyDict(name="Trey Hunner", location="San Diego")
&gt;&gt;&gt; person.location
'San Diego'
&gt;&gt;&gt; person == EasyDict(name="Trey", location="San Diego")
False
&gt;&gt;&gt; person == EasyDict(name="Trey Hunner", location="San Diego")
True
&gt;&gt;&gt; person.get('profession')
&gt;&gt;&gt; person.get('profession', 'unknown')
'unknown'
&gt;&gt;&gt; person.get('name', 'unknown')
'Trey Hunner'
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, I'd like you to allow your <code>EasyDict</code> class to accept a <code>normalize</code> keyword argument which, if true, will "normalize" the spaces in keys to underscores in attributes ✔️:</p>
<pre><code class="pycon">&gt;&gt;&gt; person = EasyDict(name="Trey Hunner", location="San Diego", normalize=True)
&gt;&gt;&gt; person['company name'] = "Truthful Technology LLC"
&gt;&gt;&gt; person.company_name
'Truthful Technology LLC'
&gt;&gt;&gt; person['company name']
'Truthful Technology LLC'
</code></pre>
<p><strong>Hints</strong></p>
<p>Hints for <strong>when you get stuck</strong> (hover over links to see what they're about):</p>
<ul>
<li><a href="https://stackoverflow.com/a/2466232/2633215" title="Classes store all their attributes in a __dict__ dictionary">One way to create a dictionary-like class</a></li>
<li><a href="https://stackoverflow.com/a/1957793/2633215" title="You can override index/key lookups with a __getitem__ method">How <code>[</code>...<code>]</code> lookups work</a></li>
<li><a href="https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute" title="The __getattr__ method is the easiest way to control what an attribute lookup does on your class">Customizing what attribute lookups (<code>obj.thing</code>) do</a></li>
<li><a href="https://gist.github.com/turicas/1510860" title="You'll want a __setitem__ method">Bonus 1: making <code>x[key] = value</code> work</a></li>
<li><a href="https://treyhunner.com/2018/04/keyword-arguments-in-python/#Keyword-only_arguments_without_positional_arguments" title="making arguments keyword-only">Bonus 2: keyword-only arguments</a></li>
<li><a href="https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes" title="You'll need a __eq__ method">Bonus 2: overriding equality between objects</a></li>
<li><a href="https://docs.python.org/3/library/stdtypes.html#dict.get" title="You'll need to reimplement the dictionary get method yourself">Bonus 2: the <code>get</code> method</a></li>
<li><a href="https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/#UserList/UserDict:_lists_and_dictionaries_that_are_actually_extensible" title="It might help to inherit from collection.UserDict or collections.abc.Mapping">Bonus 3: A helper for making dictionary-like classes</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/687c35b248d14dd1acab9c6f55cdec20/tests/">can be found here</a>.
You'll need to write your class in a module named easydict.py next to the test file.
To run the tests you'll run "python test_easydict.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>
