# Mellstroy Meme Generator

This is a simple Python CLI tool designed to download images from a list of Instagram profiles and create videos from the downloaded images.

## Features

- Download images from specified Instagram profiles.
- Create videos from the downloaded images.

## Requirements

- Python 3.6+
- Required Python packages (can be installed via `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/AlifaghaSalmanov/mellstroy_meme_generator.git
    cd mellstroy_meme_generator
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use this tool, you need to have an Instagram account. Pass your Instagram username and password as arguments.

### Command Line Arguments

- `-u`, `--username`: Instagram username (optional, use when request limits are reached and avoid using your main account).
- `-p`, `--password`: Instagram password (optional, use when request limits are reached and avoid using your main account).
- `-v`, `--video_count`: Number of videos to create from the downloaded images (optional, default is 3).

### Example

```sh
python main.py -v 3
