
<div class="row">
    <div class="col-md-8">
        <h1 class="display-3">meetup_date</h1>
        <h5>Assigned from Intermediate Level on 11/11/2019</h5>
    </div>
</div>

<div class="row">
  <div class="col-md-8">
    

<p>Hey!</p>
<p>This week I'd like you to create a function that determines which day of the
month the San Diego Python meetup should be.  The San Diego Python meetup is
on the fourth Thursday of the month (ignoring US holidays, during which we
reschedule it).</p>
<p>Your function should accept year and month arguments and should return a
datetime.date object representing the day of the month for the meetup.</p>
<pre><code>&gt;&gt;&gt; meetup_date(2012, 3)
datetime.date(2012, 3, 22)
&gt;&gt;&gt; meetup_date(2015, 2)
datetime.date(2015, 2, 26)
&gt;&gt;&gt; meetup_date(2018, 6)
datetime.date(2018, 6, 28)
&gt;&gt;&gt; meetup_date(2020, 1)
datetime.date(2020, 1, 23)
</code></pre>

<p>You can do it with just the datetime module, but this problem can definitely
be a bit tricky.</p>

## Bonus 1
<p>For the first bonus, I'd like you to allow your meetup_date function to accept
optional arguments that allow it to be used for other meetups as well. ✔️</p>
<p>The arguments, "nth" and "weekday", will allow callers of your function to
specify which weekday their meetup is held on and which occurrence in the
month it is held (for example the 2nd Tuesday or the first Friday).</p>
<pre><code>&gt;&gt;&gt; print("SD Python:", meetup_date(2015, 8, nth=4, weekday=3))
SD Python: 2015-08-27
&gt;&gt;&gt; print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2))
PyLadies on 4th Wed: 2018-07-25
&gt;&gt;&gt; print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1))
SDJS on 1st Tues: 2012-02-07
</code></pre>

## Bonus 2
<p>For the second bonus, I'd like you to allow the nth argument to be a negative
number, which means it should start counting from the end of the month. ✔️</p>
<pre><code>&gt;&gt;&gt; print("SDHN on last Friday:", meetup_date(2010, 6, nth=-1, weekday=4))
SDHN on last Friday: 2010-06-25
&gt;&gt;&gt; print("-1 != 4 (sometimes):", meetup_date(2020, 1, nth=-1, weekday=4))
-1 != 4 (sometimes): 2020-01-31
</code></pre>

<p>This one is a bit tricky because there are often a couple weekdays with 5
occurrences in a given month.</p>

## Bonus 3

<p>For the third bonus, I'd like you to create a Weekday object that can be used
to more clearly specify days without using magic numbers ✔️:</p>
<pre><code>&gt;&gt;&gt; print("SDJS", meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY))
SDJS 2012-02-07
&gt;&gt;&gt; print("PyLadies", meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY))
PyLadies 2018-07-11
&gt;&gt;&gt; print("SDHN", meetup_date(2010, 6, nth=-1, weekday=Weekday.Friday))
SDHN 2010-06-25
</code></pre>

<p>Automated tests for this week's exercise <a href="https://www.pythonmorsels.com/exercises/a8ce6ad2f64c4804acd52f9a2de464e8/tests/">can be found here</a>.
You'll need to write your function in a module named meetup_date.py next to the test file.
To run the tests you'll run "python test_meetup_date.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.</p>

  </div>
</div>



