# WaterLand

`waterland` is an Python app for calculating the number of 1s islands on a 2D array of 1s and 0s.

## Running with docker

If you have `docker` and `docker compose` installed you can run this app just by One can run the app with using docker by running the following command:

```bash
./run.sh <path_to_file>
```

## Running without docker

If you don't have docker installed you can run the app by following the steps below.

### Requirements

- python3
- git
- pip
- virtualenv

### Installation

1. Setup and activate virtualenv.

    ```bash
    virtualenv -p python3 venv
    source venv/bin/activate
    ```

1. Install the package.

    ```bash
    pip install -e src
    ```

### Usage

```bash
python -m waterland <path_to_file>
```

## Running tests

1. Install package in development mode.

    ```bash
    pip install -e src[dev]
    ```

1. Run tests.

    ```bash
    pytest
    ```
