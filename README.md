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
## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.