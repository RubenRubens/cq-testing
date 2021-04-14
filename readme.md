![](logo/cq_testing.svg)

A black-boxed testing project to check the trustworthiness of cadquery.

# How to run the tests

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
classified on two categories: passing and failing. Tests under _failing_ are intended to be used to keep
track of bugs that are posted on the CadQuery Github Issues page.

Tests are run using a custom Docker image. The provided dockerfile first clones the cadquery repo
and then installs a developer cadquery version (`conda env create -n cq -f environment.yml`).