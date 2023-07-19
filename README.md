# limitless-python

Python wrapper for the Limitless API

## Limitless? What is Limitless?

Limitless is an organization that provides competitive resources and information across Pokémon TCG, Pokémon VGC and other games.

For more information, check out the [Limitless](https://limitlesstcg.com/) home page.

## Usage

```python

import limitless
limitless.api_token = "..."

# List all tournaments
limitless.Tournament.list()

# List all games
limitless.Game.list()

# Retrieve only VGC tournaments
limitless.Tournament.list(id="VGC") # "VGC" ID retrieved from game list via limitless.Game.list()

# Retrieve standings from specific tournament
limitless.Tournament.get_standings(id="64a347f1fa3294423e4e0d23") # ID retrieved from tournament list via limitless.Tournament.list()
```

The list of API resources that are available via the `limitless` prefix are as follows:

```
Tournament
Game
```

Find more usage documentation at our [wiki](https://github.com/jpbullalayao/limitless-python/wiki). Note, the documentation is still a work in progress!

## Setup

You will need the `pip`, and the `requests` library installed on your machine in order to develop locally. One way to do this is to install a virtual environment that contains your `requests` package. To do this, see the instructions below. This assumes that you already have `pip` installed.

```
$ pip install --user virtualenv
$ cd sendbird-python
$ python -m venv sendbird-python
$ source env/bin/activate
$ pip install requests
```

## Author's Note

Interested in the progress of this project? Feel free to follow the repo for live updates!

If you need to get a hold of me regarding this project, feel free to either:

- email me at professor.ragna@gmail.com
- tweet me @professorragna

If you're interested in helping to fund this project, you can donate to me
