# Unicode Normalization URL Tester

## Introduction

This Python script is designed to test how a server handles Unicode normalization in URLs. It checks whether the server treats URLs with characters in both NFC (Normalization Form C) and NFD (Normalization Form D) the same way. This is important for ensuring consistent user experiences and preventing potential security issues.

## Features

Tests URLs with Unicode characters in both NFC and NFD forms.
User input for base URL.
Easy comparison of server responses to check for correct Unicode normalization handling.

## Installation

Before running the script, ensure you have Python installed on your system. You also need the requests library, which can be installed using pip:

```
pip install requests
```

## Usage

To use the script, follow these steps:

Clone this repository or download the script to your local machine.

Open a terminal or command prompt.

Navigate to the script's directory.

Run the script with Python:

```
python unicodetester.py
```

Enter the base URL when prompted.

The script will display whether the server handles Unicode normalization correctly.

## Contributing

Contributions to this script are welcome! Feel free to fork the repository and submit pull requests.
