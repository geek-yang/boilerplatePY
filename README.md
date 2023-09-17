# boilerplatePY
#### Starting point of your python project.

This repo provides an empty python project template. It is concise and only contains the basic configurations of a mimimum python package. <br>

To use this template, you can simplt follow the steps below:

- clone this repo
- copy the content to your target repo
- replace package name `boilerplatepy` with your desired package name
(don not forget to update the credentials in `pyproject.toml`, e.g. author's information, etc.)

## Content
The following aspects of creating a new python project is addressed by this boilerplate:
- Package manager: `hatch`
- Testing framework: `pytest`
- Linter: `ruff`
- Formatter: `black`
- CD/CI: `github action`
- Documentation: `mkdocs`

### Setup

To install the package, navigate to the repo and run:

```py
pip install -e .
```

We use `hatch` as our package manager. So please make sure that you have `hatch` installed:

```py
pip install hatch
```

### Testing

`pytest` is used as the testing framework. First install it via `pip`:

```py
pip install pytest
```

Then you should be able to run unit tests using `hatch`:

```py
hatch run test
```

### Linter

`ruff` is used as the linter. First install it via `pip`:

```py
pip install ruff
```
Then you should be able to run linter using `hatch`:

```py
hatch run lint
```

This will also notify you whether some lints are automatically fixable. To fix these issues using `ruff`. simply run:

Then you should be able to run unit tests using `hatch`:

```py
hatch run ruff --fix boilerplatepy
```

### Build documentation

Build documentation.
