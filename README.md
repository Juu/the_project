## Python3 template

Using pipenv (`pip3 install --user pipenv`)

`pipenv --three` to be sure it's using python3

Run `pipenv shell` to create virtualenv for the application then `pipenv install` to get back dependancies.


### Code

Your code should be in `app/` folder.

You can start your code using `python setup.py start`

TODO : Check for watcher and supervisor to manage application run and logs.

### Configuration

`cp config/env_example config/env`

Edit your env file to fit your needs it's using `python-dotenv` to load it in environment variable.

### Lint

Using `config/pylintrc` from `https://raw.githubusercontent.com/airbnb/binaryalert/master/.pylintrc`

`python setup.py lint`

### Test

Tests are using `unittest`

Just run `python setup.py test` to execute them.

### Bandit

Bandit can check for security issues

`python setup.py bandit`

### Add dependancy

`pipenv install <pip packageName>`
