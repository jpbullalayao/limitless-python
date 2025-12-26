# Changelog

## [1.1.0] - 2025-01-27

### Added
- Added pretty printing to `LimitlessObject` responses using JSON formatting with indentation and sorted keys.

## [1.0.1] - 2025-12-26

### Added
- Added `requests` as an install dependency in `setup.py`. The `requests` module will now be automatically installed when users install `limitless-python` via pip, uv, or other package managers.

### Changed
- Updated package description from "Limitless API" to "LimitlessTCG API" in both `README.md` and `setup.py` for better clarity.

### Fixed
- Fixed typo in `api_resource.py`.

## [1.0.0] - 2023-07-17

### Added
- Initial release of `limitless-python`
- Support for listing tournaments via `limitless.Tournament.list()`
- Support for retrieving tournament standings via `limitless.Tournament.get_standings(id="...")`
- Support for listing games via `limitless.Game.list()`

[1.1.0]: https://github.com/jpbullalayao/limitless-python/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/jpbullalayao/limitless-python/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/jpbullalayao/limitless-python/releases/tag/v1.0.0

