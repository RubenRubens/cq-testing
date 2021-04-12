![](logo/cq_testing.svg)

A black-boxed testing project to check the results of cadquery.

# How to run the tests

You don't need any installation to use this project. Simply go to the **Actions** tab on github
and check the latest output on **testing**. Once there open **Tests 🧪**. That's it.
Notice that some tests have no output due to a time limit of 60 seconds to run each one.

# How to use it in your local machine

You need Docker to be installed. Simply clone this repo and use docker compose, like so:

```
$ git clone https://github.com/RubenRubens/cq-testing.git
$ cd cq-testing
$ docker-compose run passing
$ docker-compose run failing
```

# How it works

There is a bash script that finds all python files that starts with _test_. Each of those tests are run
using unittest with a timeout of 60 seconds. This way, any code is prevented to run infinitely. Tests are
classified on two categories: passing and all.

Tests are run using a custom Docker image. The provided dockerfile first clones the cadquery repo
and then installs a developer cadquery version (`conda env create -n cq -f environment.yml`).