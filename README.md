# LCAcollect Shared Config Package

This package contains shared config and utils to be used across LCAcollect backends. It is a Python package, distributed to
PyPI to be consumed from the relevant backends.

# Getting Started

Install the following in your virtual environment:

- Python 3.10
- [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)
- [pre-commit](https://pre-commit.com/#installation)

**Setup local Python environment**

```shell
poetry install
pre-commit install
```

**Run tests**

```shell
pytest tests/
```

# Publishing

Azure Artifacts are being used to
manage [versioning of this package](https://dev.azure.com/arkitema/lca-platform/_artifacts/feed/backend-packages/PyPI/lcaconfig/versions)
. When a new version is ready to be published, remember to update the version by running the following command:
```shell
poetry version minor
```
otherwise the pipeline will fail to publish the package.
Publishing happens automatically on merges to `main` in an Azure Pipeline.



# License

Unless otherwise described, the code in this repository is licensed under the Apache-2.0 License. Please note that some
modules, extensions or code herein might be otherwise licensed. This is indicated either in the root of the containing
folder under a different license file, or in the respective file's header. If you have any questions, don't hesitate to
get in touch with us via [email](mailto:chrk@arkitema.com).