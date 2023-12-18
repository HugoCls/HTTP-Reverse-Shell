# HTTP-Reverse-Shell

This project demonstrates a simple Python-based remote command execution server. 

It allows users to execute commands on the server remotely via HTTP GET requests.

## Disclaimer

This server executes commands directly from GET requests, which can be a security risk. 

Use caution when running any code that executes commands remotely.

Do not expose this server to the internet without proper authentication and authorization mechanisms.

## Getting Started

1. **Run the Server**:
    - Ensure Python 3 is installed.
    - Execute the server script using `python3 base64_server.py`.
    - The server will start listening on port 1234 by default.

2. **Executing Commands**:
    - Send a GET request to the server endpoint `/cmd` with a base64-encoded query parameter `command` specifying the command to execute.
    - Example: `http://IP_OR_DOMAIN/cmd?command=YOUR_BASE64_ENCODED_COMMAND`
        - base64encode("whoami") == "d2hvYW1p"
        - base64encode("dir") == "ZGly"

3. **Responses**:
    - If the command execution is successful, the server responds with a `200 OK` status and the output of the command.
   ![Response to dir (Windows 10)](https://github.com/HugoCls/HTTP-Reverse-Shell/blob/main/images/readme1.png)
    - If there's an error during command execution, a `200 OK` status with an error message is returned.

4. **Remote Usage**:
    - Ensure that the server's port 1234 is open to incoming connections.

## Requirements

- Python 3.x
- Libraries: `http.server`, `urllib.parse`, `subprocess`, `base64`

---

Feel free to contribute, improve, or fork this project!
