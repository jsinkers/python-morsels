# FuzzyString

<div class="container content-wrapper">
<div class="row">
  <div class="col-md-8">
    

<p>Hello!</p>
<p>This week I'd like you to write a <code>FuzzyString</code> class which acts like a string, but does comparisons in a case-insensitive way.</p>
<p>For example:</p>
<pre><code>&gt;&gt;&gt; greeting = FuzzyString('Hey TREY!')
&gt;&gt;&gt; greeting == 'hey Trey!'
True
&gt;&gt;&gt; greeting == 'heyTrey'
False
&gt;&gt;&gt; greeting
'Hey TREY!'
</code></pre>

<p>I'd like you to make sure equality and inequality match case-insensitively at first.
I'd also like you to ensure that the string representations of your class match Python's string objects' default string representations.</p>

## Bonus 1

<p>For the first bonus, try to ensure the other comparison operators work as expected:</p>
<pre><code>&gt;&gt;&gt; o_word = FuzzyString('Octothorpe')
&gt;&gt;&gt; 'hashtag' &lt; o_word
True
&gt;&gt;&gt; 'hashtag' &gt; o_word
False
</code></pre>

## Bonus 2
<p>For the second bonus, ensure your <code>FuzzyString</code> class works with string concatenation and the <code>in</code> operator:</p>
<pre><code>&gt;&gt;&gt; o_word = FuzzyString('Octothorpe')
&gt;&gt;&gt; 'OCTO' in o_word
True
&gt;&gt;&gt; new_string = o_word + ' (aka hashtag)'
&gt;&gt;&gt; new_string == 'octothorpe (AKA hashtag)'
True
</code></pre>

## Bonus 3
<p>For the third bonus, also make your string normalize unicode characters when checking for equality:</p>
<pre><code>&gt;&gt;&gt; ss = FuzzyString('ss')
&gt;&gt;&gt; '\u00df' == ss
True
&gt;&gt;&gt; e = FuzzyString('\u00e9')
&gt;&gt;&gt; '\u0065\u0301' == e
True
&gt;&gt;&gt; '\u0301' in e
True
</code></pre>

<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/9655802abaef47c682555c198ee8b641/tests/">can be found here</a>.
You'll need to write your code in a module named fuzzystring.py next to the test file.
To run the tests you'll run "python test_fuzzystring.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>

  </div>
</div>
    </div>