# API Tests with Python

This is a python code that will test HTTP/HTTPS (GET/POST/PUT/DELETE) requests. It loops through the YAML file `url.yaml` for the API URL then run the status check (`200`)on them.

**Dependencies:** [PyTest](https://docs.pytest.org/en/7.1.x/getting-started.html#install-pytest), [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation), [Requests](https://requests.readthedocs.io/en/latest/).

How to run: After installing the dependencies and updating the yaml file with the API url, you can run the test using the command below.

```command
pytest API.yaml
```

**Future View:**

- The status check can be specified in the YAML file for more dynamic test on the API.

- The requests data can be passed in through an environment variable or a file which can be securely passed doing runtime to secure sensitive data/tokens.
