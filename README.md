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
git clone https://github.com/SAED2906/YouTube-VideoCreation-Bot.git
```

2. Navigate into the directory:
```
cd YouTube-VideoCreation-Bot
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Setup your configuration by editing `reddit.py` (see Configuration section below).
2. Run the automata script:
```
python main.py
```

## Configuration

The `reddit.py` file contains important settings. Here's a basic setup:

```
CLIENT_ID = Your_Client_ID
CLIENT_SECRET = Your_Client_Secret
USER_AGENT = Your_User_Agent
SUBREDDIT = The_Subreddit_you_want
```

Replace the placeholders (`Your_Client_ID`, etc.) with your actual credentials.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests. Ensure that your changes are well-documented.

## Disclaimer

This project is for educational purposes only. Users are responsible for ensuring that the content they gather and publish adheres to the terms of service of both Reddit and YouTube.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

---

Happy automating!
