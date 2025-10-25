# Changelog

All notable changes to this project will be documented in this file.

## [0.2.2] - 2025-10-24
### Added
- Input validation for all menu selections to prevent crashes.
- Back/Exit options in menus for safer navigation.
- Error handling when API returns no videos.
- Clear and numbered video selection list for easier choice.
- Consolidated keys resolving function for API requests.

### Fixed
- Crashes caused by invalid user input (letters, out-of-range numbers).
- Broken menu flow on invalid selections.
- Improved console UI readability with borders and spacing.

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