import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def main():
    print("Hello from mcp-crash-course!")
    print("os.getenv('OPENAI_API_KEY'):", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    asyncio.run(main())
