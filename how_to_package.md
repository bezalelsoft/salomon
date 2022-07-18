# How to run unit tests

```bash
# do only once
pip3 install -e .

# run tests
pytest

```


# How to deploy

https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Run only once:
```shell
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

TODO: generate token in PyPi and store it in laptop... 


## run every time to build package
```sh

python3 -m build

# for test
python3 -m twine upload --repository testpypi dist/*

# TODO: for prod
python3 -m twine upload dist/*

```
