from src import tools
from asyncio import get_event_loop

get_event_loop().run_until_complete(tools.run_service())
