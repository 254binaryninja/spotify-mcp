## Create MCP server for interacting with the Spotify API

from config import sp
from mcp.server.fastmcp import FastMCP

## Create the MCP server

mcp = FastMCP("spotify-mcp-server")

## Create playback tools

@mcp.tool()
def play() -> str:
    """
    Play the current track
    Returns:
        str: A message indicating the result of the operation
    """
    sp.start_playback()
    return "Playing the current track"

@mcp.tool()
def pause() -> str:
    """
    Pause the current track
    """
    sp.pause_playback()
    return "Paused the current track"

@mcp.tool()
def next_track() -> str:
    """
    Skip to the next track
    Returns:
        str: A message indicating the result of the operation
    """
    sp.next_track()
    return "Skipped to the next track"

@mcp.tool()
def previous_track() -> str:
    """
    Return to the previous track
    Returns:
        str: A message indicating the result of the operation
    """
    sp.previous_track()
    return "Skipped to the previous track"

@mcp.tool()
def shuffle() -> str:
    """
    Shuffle the current playlist
    Returns:
        str: A message indicating the result of the operation
    """
    sp.shuffle(True)
    return "Shuffled the current playlist"

@mcp.tool()
def repeat() -> str:
    """
    Repeat the current playlist
    Returns:
        str: A message indicating the result of the operation
    """
    sp.repeat("context")
    return "Repeating the current playlist"

@mcp.tool()
def repeat_off() -> str:
    """
    Turn off repeat
    Returns:
        str: A message indicating the result of the operation
    """
    sp.repeat("off")
    return "Turned off repeat"

@mcp.tool()
def play_album(album_name: str) -> str:
    """
    Play an album by its name

    Args:
        album_name (str): The name of the album to play
    Returns:
        str: A message indicating the result of the operation
    """
    results = sp.search(q=f"album:{album_name}", type="album")
    if results['albums']['items']:
        album_id = results['albums']['items'][0]['id']
        sp.start_playback(context_uri=f"spotify:album:{album_id}")
        return f"Playing album: {album_name}"
    else:
        return f"Album not found: {album_name}"

