![](logo/cq_testing.svg)

A black-boxed testing project to check the results of cadquery.

# How to run the tests

You don't need any installation to use this project. Simply go to the **Actions** tab on github
and check the latest output (you have to see something similar to [this](https://github.com/RubenRubens/cq-testing/runs/1687693936?check_suite_focus=true)). Once there open **Tests 🧪**. That's it.
Notice that some tests have no output due to time limit of 20 seconds to run each test.

# How to use it in your local machine

You need Docker to be installed. Simply clone this repo and use docker compose, like so:

```
$ git clone https://github.com/RubenRubens/cq-testing.git
$ cd cq-testing
$ docker-compose up
```

# How it works

There is a bash script that finds all python files that starts with _test_. Each of those tests are run
using unittest with a timeout of 20 seconds to finish. This way, any code is prevented to run infinitely.

Tests can follow any structure as long as they live in a folder inside _src_. However there is a common
pattern you might find. Tests start with multiple files that create an equal result using different
approaches. Let's use _src/HelloWorld_ as an example. There are two files that create a box: _HW1_ achieve
this using the `.box()` method and _HW2_ does it by creating a rectangle and then extruding it.

**HW1**

```
result = cq.Workplane().box(3, 4, 1, centered=(False,False,False))
```
**HW2**

```
result = cq.Workplane().rect(3, 4, centered=False).extrude(1)
```

A test that import both results and validate the two objects and then compares them using
boolean operations and then measuring the volume. In this case, HW1 result is imported as
`R1` and HW2 as `R2`. So we have to perform the difference of those and check that the volume
is 0. Therefore, we have to test that `R1.cut(R2).val().Volume()` is equal to 0.

Tests are run using a custom Docker image. Docker first clones the cadquery repo and then 
installs a developer cadquery version (`conda env create -n cq -f environment.yml`). This docker
image is then manually upload as github Package.
