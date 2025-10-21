# Changelog

All notable changes to this project will be documented in this file.

## [0.2.1] - 2025-10-19
### Fixed
- Added missing utilities for **Bomb B** and **Mid** sites across all maps in `videos.json`.
- Ensured consistent JSON structure for all map entries (Mirage, Dust, and Inferno).
- Corrected API base URL in `main.py` to properly connect with the Flask backend.
- Corrected video selection display: shows numbered spot names instead of nested dictionary.

## [0.2.0] - 2025-10-18
### Added
- Created API endpoint (`app.py`) for retrieving utilities links by map, side, site and util.
- Integrated `requests` in `main.py` to consume data from the API instead of a local JSON file.

### Documentation
- Updated `README.md` with usage and installation instructions.
- Added `LICENSE` section and clarified repository structure.

## [0.1.0] - 2025-10-18
### Added
- Initial project setup with `main.py`, `videos.json`, and console interface
- Basic JSON structure for Mirage, Dust, and Inferno