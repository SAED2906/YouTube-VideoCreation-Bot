# YouTube-VideoCreation-Bot

## Description

The **Reddit-to-YouTube Automata** is an educational project designed to curate popular Reddit posts and transform them into video format, which are then automatically uploaded to YouTube. It's a great tool for individuals looking to stay updated with trending content from Reddit in a video format. 

> **Note:** This tool is for educational purposes only. Always ensure you respect copyrights and content policies of both Reddit and YouTube when using this tool.

## Features

- Automatically fetches top trending posts from specified Reddit subreddits.
- Converts Reddit posts into an engaging video format.
- Automatic uploads to a YouTube channel.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [Disclaimer](#disclaimer)
- [License](#license)

## Installation

1. Clone the repository:
```
git clone https://github.com/your_username/Reddit-to-YouTube-Automata.git
```

2. Navigate into the directory:
```
cd Reddit-to-YouTube-Automata
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Setup your configuration by editing `config.json` (see Configuration section below).
2. Run the automata script:
```
python main.py
```

## Configuration

The `config.json` file contains important settings. Here's a basic setup:

```json
{
    "reddit": {
        "client_id": "YOUR_REDDIT_CLIENT_ID",
        "client_secret": "YOUR_REDDIT_CLIENT_SECRET",
        "subreddits": ["popular", "news"],
        "max_posts": 10
    },
    "youtube": {
        "api_key": "YOUR_YOUTUBE_API_KEY",
        "channel_id": "YOUR_CHANNEL_ID"
    },
    "video_settings": {
        "duration": 60,
        "resolution": "1080p"
    }
}
```

Replace the placeholders (`YOUR_REDDIT_CLIENT_ID`, etc.) with your actual credentials.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests. Ensure that your changes are well-documented.

## Disclaimer

This project is for educational purposes only. Users are responsible for ensuring that the content they gather and publish adheres to the terms of service of both Reddit and YouTube.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

---

Happy automating!
