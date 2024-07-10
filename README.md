# Reels Generator

This is a simple Python CLI tool designed to download images from a list of Instagram profiles and create videos from the downloaded images.

inspirations:
- https://www.instagram.com/p/C8GLDFtAmgA/
- https://www.instagram.com/p/C8fXN9Bsqty/
- https://www.instagram.com/p/C9HXi3_onKI/

## Features

- Download images from specified Instagram profiles.
- Create videos from the downloaded images.

## Requirements

- Python 3.9
- Required Python packages (can be installed via `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/AlifaghaSalmanov/reels_generator.git
    cd reels_generator
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Command Line Arguments

- `-u`, `--username`: Instagram username (optional, use when request limits are reached and avoid using your main account).
- `-p`, `--password`: Instagram password (optional, use when request limits are reached and avoid using your main account).
- `-v`, `--video_count`: Number of videos to create from the downloaded images (optional, default is 3).

### Example

```sh
python main.py -v 3
