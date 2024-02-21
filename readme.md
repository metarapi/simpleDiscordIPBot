## Simple current IP update Discord Bot

This is a Python project for a Discord bot that uses the `discord.py` library. The bot responds to certain commands and can provide the public IP address of the machine it's running on, as well as URLs for Foundry VTT and Valheim servers running on the same machine. This is to avoid the problem of not having a static IP available as an option from the ISP.

### Getting Started
To get started with this project, you'll need to have Python and pip installed on your machine.

### Prerequisites

- Python
- pip

### Installation
Clone the repository to your local machine.
Navigate to the project directory.
Install the required packages using pip:

```pip install -r requirements.txt```

### Usage
The main entry point of the application is `main.py`. You can run it with the following command:

```python main.py```

The `getIP.py` script contains a function `get_public_ip` that can be used to get the public IP address of your machine.

The `responses.py` script contains a function `get_response` that the bot uses to respond to user commands.

### Bot Commands
The bot responds to the following commands:

1. `!ip:` Returns the public IP address of the machine the bot is running on.
2. `!foundry:` Returns a URL to the Foundry VTT server running on the machine.
3. `!valheim:` Returns a connection string to the Valheim server running on the machine.

### Docker

This project includes a Dockerfile, which means you can build and run the application in a Docker container. Build the Docker image with:

```docker build -t discord-app .```

### Environment Variables
The project uses environment variables, which are stored in the .env file. Make sure to set your discord API key here for your bot to work.

### Virtual Environment
The project includes a virtual environment in the `env` directory. You can activate the environment with the activate script in the `env\Scripts` directory:

```source env/Scripts/activate```

