offregister_mongodb
====================
This package follows the offregister specification for MongoDB

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

## Example config

    {
        "module": "offregister-mongodb",
        "type": "fabric",
        "kwargs": {
            "VERSION": "3.4"
        }
    }

To setup your environment to use this config, follow [the getting started guide](https://offscale.io/docs/getting-started).

## Roadmap

  - Additional users and passwords
  - Custom config
  - Clustering
