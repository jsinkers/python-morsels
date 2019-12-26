<div class="container content-wrapper">
        <h1 class="display-3">record_calls</h1>        
        <h5>Assigned from Intermediate Level on 12/23/2019</h5>
</div>

<div class="row">
  <div class="col-md-8">
<p>Hi!</p>
<p>This week I'd like you to write a decorator function that will record the number of times a function is called.</p>
<p>Your decorator function should be called <code>record_calls</code> and it'll work like this:</p>
<pre><code class="python">@record_calls
def greet(name):
    """Greet someone by their name."""
    print(f"Hello {name}")
</code></pre>
<p>That <code>record_calls</code>-decorated greet function will now have a <code>call_count</code> attribute that keeps track of the number of times it was called:</p>
<pre><code class="pycon">&gt;&gt;&gt; greet("Trey")
Hello Trey
&gt;&gt;&gt; greet.call_count
1
&gt;&gt;&gt; greet()
Hello world
&gt;&gt;&gt; greet.call_count
2
</code></pre>
<p>Decorator functions are functions which accept another function and return a new version of that function to replace it.</p>
<p>So this should be the same thing as what we typed above:</p>
<pre><code class="python">greet = record_calls(greet)
</code></pre>
<p>If you haven't ever made a decorator function before, you'll want to look up how to make one.</p>
<p>If you've made a decorator function before, you might want to attempt one of the bonuses.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus I'd like you to make sure your decorator function preserves the name and the docstring of the original function. ✔️</p>
<p>So if we ask for help on the function above:</p>
<pre><code class="pycon">&gt;&gt;&gt; help(greet)
</code></pre>
<p>We should see something like this:</p>
<pre><code>Help on function greet in module __main__:

greet(name)
    Greet someone by their name.
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus I'd like you to keep track of a "calls" attribute on our function that records the arguments and keyword arguments provided for each call to our function. ✔️</p>
<pre><code class="pycon">&gt;&gt;&gt; greet("Trey")
Hello Trey
&gt;&gt;&gt; greet.calls[0].args
('Trey',)
&gt;&gt;&gt; greet.calls[0].kwargs
{}
&gt;&gt;&gt; greet(name="Trey")
Hello Trey
&gt;&gt;&gt; greet.calls[1].args
()
&gt;&gt;&gt; greet.calls[1].kwargs
{'name': 'Trey'}
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, add a return_value and an exception attribute to each of the objects in our calls list.
If the function returned successfully, <code>return_value</code> will contain the return value.
Otherwise, exception will contain the exception raised. ✔️</p>
<p>When an exception is raised a special <code>NO_RETURN</code> value should be returned.
Your module should have a <code>NO_RETURN</code> attribute that contains this special value.</p>
<pre><code class="pycon">&gt;&gt;&gt; @record_calls
... def cube(n):
...     return n**3
...
&gt;&gt;&gt; cube(3)
27
&gt;&gt;&gt; cube.calls
[Call(args=(3,), kwargs={}, return_value=27, exception=None)]
&gt;&gt;&gt; cube(None)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 9, in wrapper
  File "&lt;stdin&gt;", line 3, in cube
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
&gt;&gt;&gt; cube.calls[-1].exception
TypeError("unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'")
&gt;&gt;&gt; cube.calls[-1].return_value == NO_RETURN
True
</code></pre>
<p><strong>Hints</strong></p>
<p>Hints for <strong>when you get stuck</strong> (hover over links to see what they're about):</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=FsAPt_9Bf3U" title="A video on writing decorators">A video on decorators</a></li>
<li><a href="https://www.thecodeship.com/patterns/guide-to-python-function-decorators/" title="An explanation of decorators and examples of creating and using them">An article explaining decorators</a></li>
<li><a href="https://stackoverflow.com/q/49839332/2633215" title="You can add an attribute onto a function in Python">Adding attributes to a decorator</a></li>
<li><a href="https://youtu.be/FsAPt_9Bf3U?t=802" title="You can make a class-based decorator with an initializer and a __call__ method">Writing a decorator using a class</a></li>
<li><a href="https://stackoverflow.com/a/309000/2633215" title="functools.wraps can preserve the metadata of the function you're decorating">Preserving metadata of decorated functions</a></li>
<li><a href="https://youtu.be/epKegvx_Jws?t=365" title="typing.NamedTuple creates a friendly tuple-like class without much boilerplate">Creating a lightweight class</a></li>
<li><a href="https://youtu.be/epKegvx_Jws?t=661" title="With dataclasses we can generate a mutable boilerplate class">An even better way to create a lightweight class</a></li>
<li><a href="https://treyhunner.com/2019/03/unique-and-sentinel-values-in-python/#Creating_unique_non-None_placeholders:_why_object()?" title="Creating your own None-like sentinel values">Creating a unique value</a></li>
<li><a href="https://stackoverflow.com/a/40493467/2633215" title="Various ways to use Python's raise statement">Different techniques for raising exceptions</a></li>
</ul>
<p><strong>Tests</strong></p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/tests/">can be found here</a>.
You'll need to write your code in a module named record_calls.py next to the test file.
To run the tests you'll run "python test_record_calls.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>