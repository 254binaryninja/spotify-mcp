# Spotify MCP Server

The **Spotify MCP Server** is a Model Context Protocol (MCP) server designed to interact with the Spotify API. It provides tools to control Spotify playback, such as playing, pausing, skipping tracks, shuffling playlists, and more. This server is built using the `mcp` framework and `spotipy` library.

## Features

- Play, pause, and skip tracks.
- Shuffle and repeat playlists.
- Play specific albums or tracks by name.
- Built-in tools for seamless Spotify playback control.

## Prerequisites

Before setting up the server, ensure you have the following:

1. Python 3.12 or higher.
2. A Spotify Developer account with a registered application. You will need:
   - `SPOTIFY_CLIENT_ID`
   - `SPOTIFY_CLIENT_SECRET`
3. A `.env` file containing your Spotify credentials.
4. A premium spotify account

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd spotify-mcp-server
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install `uv` for dependency management:
   ```bash
   pip install uv
   ```
   Windows
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

4. Install dependencies using `uv` from the pyproject.toml file:
   ```bash
   uv sync
   ```

5. Create a `.env` file in the project root and add your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

## Usage

1. Start the MCP server:
   ```bash
   python server.py
   ```

2. Use the provided tools to control Spotify playback. For example:
   - `play()`: Start playing the current track.
   - `pause()`: Pause the current track.
   - `next_track()`: Skip to the next track.
   - `play_album("album_name")`: Play a specific album by name.
   - `play_track("track_name")`: Play a specific track by name.

3. Add MCP tools to your MCP client. For example, if you're using Claude:
     Add this at the root of your project
    ```bash
   uv mcp install server.py
   ```
## Example Using Calude Desktop

 Here is the JSON file
  ```
  {
  "mcpServers": {
    "spotify-mcp-server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "~path to project\\spotify-mcp-server\\server.py"
      ]
    }
  }
}
 ```
   

## Troubleshooting

- **Spotify Authentication Failed**: Ensure your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` are correctly set in the `.env` file.
- **Server Not Starting**: Verify that the `__name__` check in `server.py` is correctly set to `__main__`:
  
   ```python
   # if __name__ == "__server__":
   #  mcp.run()
   ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

