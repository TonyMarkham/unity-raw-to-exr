# Unity RAW To EXR

This is a utility to convert the 16-bit raw heightmap data that Unity's Terrain System exports into a 16-bit EXR format.

## Installation

Run the following to install:

```bash
pip install unity_raw_to_exr
```

## Usage

```python
from unity_raw_to_exr import raw_to_exr

raw_to_exr("tests/terrain-33.raw")

```

## Developing unity_raw_to_exr

To install unity_raw_to_exr, along with the tools that you need to develop and run tests, run the following in your virtualenc (venv):

```bash
pip install -e .[dev]
```

## Other

### Source Distribution

To create a source distribution:

```bash
python setup.py sdist
```

### Update the MANIFEST.in

If working on the development, the venv should already have `check-manifest`

Refer to https://pypi.org/project/check-manifest/

## Acknowledgements

- Mark Smith
  - https://github.com/judy2k/publishing_python_packages_talk
