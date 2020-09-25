# Installation guide

## Part 1

After cloning this repository to try out part 1 of the exercise all you have to do is:

```
$ cd part1
# depending on your env you might have to use python3 here
$ python exercise.py

>>> you should now see the expected results...
```

## Part 2

For part 2 however it's recommended to use a virtual environment, I used virtualenv.

```
# make sure you're at the root of the project
$ ls
>>> part1            part2            requirements.txt
$ virtualenv venv # create a virtual environment
>>> created virtual environment output...
$ source venv/bin/activate # activate environment
(venv) $ pip install -r requirements.txt # install packages
>>> Collecting aniso8601==8.0.0
  Using cached aniso8601-8.0.0-py2.py3-none-any.whl (43 kB)
Collecting click==7.1.2
...

(venv) $ cd part2
(venv) $ python app.py
>>> * Serving Flask app "app" (lazy loading) ...
```

the server should now be running on http://0.0.0.0:4996/

# Part 1

The code for this part can be found in the part1 directory. The person and office class can be found in their respective files. And the exercises we were expected to do with those classes can be found in the exercise.py file. Running exercise.py should give you the output shown on the screenshow below

<img src='console_output_part1.png'>
