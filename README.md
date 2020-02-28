# robarthur.co.uk

Source of https://www.robarthur.co.uk build with Pelican and published with Github Actions


![Publish Website](https://github.com/robarthur/robarthur.co.uk/workflows/Publish%20Website/badge.svg)

## Getting Started

Clone the repo and activate the environemnt

```
robarthur.co.uk$ python3 -m venv env/
source env/bin/activate
pip install -r requirements.txt
```

### Building the source

```
make clean && make html
```

Build all of the static assets under `output/`

### Running a devserver

```
make devserver
```

Serves up the static content under http://localhost:8000/
