# limitless-python

Python wrapper for the LimitlessTCG API

## Limitless? What is Limitless?

Limitless is an organization that provides competitive resources and information across Pokémon TCG, Pokémon VGC and other games.

For more information, check out the [Limitless](https://limitlesstcg.com/) home page.

## Installation

```
$ pip3 install limitless-python
```

## Usage

```python
import limitless
limitless.api_token = "..."

# List all tournaments
limitless.Tournament.list()

# List all games
limitless.Game.list()

# Retrieve only VGC tournaments
limitless.Tournament.list(game="VGC") # "VGC" game retrieved from game list via limitless.Game.list()

# Retrieve standings from specific tournament
limitless.Tournament.get_standings(id="64a347f1fa3294423e4e0d23") # ID retrieved from tournament list via limitless.Tournament.list()
```

The list of API resources that are available via the `limitless` prefix are as follows:

```
Tournament
Game
```

Find more usage documentation at our [wiki](https://github.com/jpbullalayao/limitless-python/wiki). Note, the documentation is still a work in progress!

## Author's Note

Interested in the progress of this project? Feel free to follow the repo for live updates!

If you need to get a hold of me regarding this project, feel free to either:

- email me at professor.ragna@gmail.com
- tweet me [@professorragna](https://twitter.com/professorragna)

If you're interested in helping to fund this project, you can support me [here](https://www.buymeacoffee.com/professorragna). Any and all support is greatly appreciated!
