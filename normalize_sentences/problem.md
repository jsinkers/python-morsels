<div class="container content-wrapper">

      




      

      
<div class="row">
    <div class="col-md-8">
        <h1 class="display-3">normalize_sentences</h1>
    </div>
</div>

<div class="row">
  <div class="col-md-8">

<p>Hiya!</p>
<p>When I write text in a fixed-width font (code, markdown, etc.), <a href="https://twitter.com/treyhunner/status/982434283091570688">I use two spaces after sentences</a>.  This can lead to inconsistencies when I copy text from elsewhere or I collaborate on a project with someone who isn't a 2-spacer.</p>
<p>So this week I'd like you to write a function, <code>normalize_sentences</code>, which accepts a string of text and makes sure there are two spaces between the sentences.</p>
<p>Your function should work like this:</p>
<pre><code>&gt;&gt;&gt; normalize_sentences("I am. I was. I will be.")
'I am.  I was.  I will be.'
&gt;&gt;&gt; normalize_sentences("Hello? Yes, this is dog!")
'Hello?  Yes, this is dog!'
</code></pre>
<p>Your function should treat <code>.</code>, <code>?</code>, and <code>!</code> as sentence-ending characters.</p>

## Bonus 1

<p>For the first bonus, I'd like you to make sure your function doesn't add unnecessary extra spaces if there are already two spaces between some sentences.  Your function should also ensure that paragraph breaks and other whitespace is maintained as it was.</p>
<pre><code>&gt;&gt;&gt; normalize_sentences("I am.  I was. I will be.")
'I am.  I was.  I will be.'
&gt;&gt;&gt; normalize_sentences("I said.  She said.\n\nThey said. We said.")
'I said.  She said.\n\nThey said.  We said.'
</code></pre>

## Bonus 2

<p>For the second bonus, I'd like you to make sure <code>normalize_sentences</code> doesn't make a sentence break after an abbreviation or a decimal number:</p>
<pre><code>&gt;&gt;&gt; normalize_sentences("I sold $5.50 worth of various fruits (i.e. apples).")
'I sold $5.50 worth of various fruits (i.e. apples).'
</code></pre>

## Bonus 3

<p>For the third bonus I'd like you to see if you can get <code>normalize_sentences</code> working with strings like this one:</p>
<pre><code>&gt;&gt;&gt; normalize_sentences("Have you used searched for Dr. Seuss on google.com?")
'Have you used searched for Dr. Seuss on google.com?'
</code></pre>
<p>A hint: regular expressions may come in handy when solving these.</p>
<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/b64cb2e50c84448badb57c8fdeb79445/tests/">can be found here</a>.
You'll need to write your function in a module named normalize_sentences.py next to the test file.
To run the tests you'll run "python test_normalize_sentences.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>


  </div>
</div>
