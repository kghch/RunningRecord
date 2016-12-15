## Jog Record
[Demo](http://138.68.18.245:9888/)

It took me one day to complete this. Actually it's not completed, for I didn't put it in a public host.

It only runs on my local computer.

At first, I wanted to use Goole Cloud Platform to run this(and convinient for Google SignIn, but it seems I need to deal with the database problem.
I don't think its simplest environment did support it.

The app is simple.

Requirements:
- Python 2.7
- pip install web.py
- mysql database
- Linux crontab

Run `run.py`, put the `weekly_run_email.py` into the /etc/crontab, do it every Saturday.(Depending on yourself.)

***
