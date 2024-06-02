[![progress-banner](https://backend.codecrafters.io/progress/http-server/52113345-eb45-4679-a634-4688313beec8)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

## README.md

# SimpleHTTPServer

SimpleHTTPServer is a lightweight HTTP server built from scratch in Python. It handles basic HTTP requests such as GET and POST, and provides functionalities like echoing messages, displaying user-agent information, handling file operations, and more.

## Features

- Handles basic HTTP GET and POST requests.
- Echoes messages from the URL.
- Displays user-agent information from request headers.
- Supports file retrieval and creation.
- Handles content encoding for responses.
- Multi-threaded to handle multiple requests concurrently.

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
https://github.com/C0dewordSky/C0dewordSky-http-server-python.git
cd codecrafters-http-server-python
```

## Usage

Run the server with the following command:

```bash
python main.py /path/to/directory
```

The server will start listening on `localhost:4221`.

## Endpoints

### GET /

Returns a simple HTTP 200 OK response.

### GET /echo/<message>

Echoes the `<message>` in the response body.

### GET /user-agent

Returns the user-agent information from the request headers.

### GET /accept-encoding

Returns the accepted encoding from the request headers.

### GET /files/<filename>

Retrieves the specified file from the directory provided as a command-line argument.

### POST /files/<filename>

Creates or overwrites the specified file in the directory provided as a command-line argument with the content sent in the request body.

## Example

To start the server:

```bash
python server.py /path/to/your/files
```

Send a GET request to echo a message:

```bash
curl http://localhost:4221/echo/HelloWorld
```

Send a POST request to create a file:

```bash
curl -X POST -d "This is a test file" http://localhost:4221/files/test.txt
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
