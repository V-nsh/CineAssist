import os
from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core import Settings
from app.functions.movie_functions import get_movies_by_name, get_movies_by_description, get_movies_by_genre, get_movies_by_cast, get_movies_by_language, get_movies_by_mood, get_movies_by_average_rating, get_movies_by_showtime
from app.functions.payment_functions import create_razorpay_order
import pandas as pd


openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")


# settings
Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=openai_api_key, system_prompt="Your name is FLASH. Greet everyone at the start of every message.")

get_movies_by_name_tool = FunctionTool.from_defaults(fn=get_movies_by_name)
get_movies_by_description_tool = FunctionTool.from_defaults(fn=get_movies_by_description)
get_movies_by_genre_tool = FunctionTool.from_defaults(fn=get_movies_by_genre)
get_movies_by_cast_tool = FunctionTool.from_defaults(fn=get_movies_by_cast)
get_movies_by_language_tool = FunctionTool.from_defaults(fn=get_movies_by_language)
get_movies_by_mood_tool = FunctionTool.from_defaults(fn=get_movies_by_mood)
get_movies_by_average_rating_tool = FunctionTool.from_defaults(fn=get_movies_by_average_rating)
get_movies_by_showtime_tool = FunctionTool.from_defaults(fn=get_movies_by_showtime)
create_razorpay_order_tool = FunctionTool.from_defaults(fn=create_razorpay_order)

agent = ReActAgent.from_tools([ get_movies_by_name_tool, get_movies_by_description_tool, get_movies_by_genre_tool, get_movies_by_cast_tool, get_movies_by_language_tool, get_movies_by_mood_tool, get_movies_by_average_rating_tool, get_movies_by_showtime_tool, create_razorpay_order_tool ], verbose=True)

response = agent.chat("Has john doe starred in any horror movie")

print(response)

# response = agent.chat("What are the showtimes of each of the movies you recommended ?")

# print(response)

# response = agent.chat("Book me a ticket to anyone of them")

# print(response)