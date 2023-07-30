# ersilia-precalculation-poc
POC Repository to experiment with pre-calculating outputs for the Ersilia Model Hub

## Requirements
- Linux or MacOS
- python 3.10 installation (recommend using pyenv)

Set up virtual environment with `make install`, and activate it with `source .venv/bin/activate`

## Generating example pre-calculations

### Install Ersilia Model Hub
Install the model hub into this project with `make install-ersilia`

Requirements for the model hub
- git lfs
- docker

### Fetch input data
Manually download the [reference file](https://github.com/ersilia-os/groverfeat/raw/main/data/reference_library.csv) and save it to the root directory of this repo. The file is ~100MB.
