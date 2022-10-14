""" rates app """

import time
from datetime import date
import asyncio


from rates_api_server import rates_api_server
from rates_demo import get_rates_async

async def main() -> None:
  
    with rates_api_server():

        start = time.time()

        rates_data = await get_rates_async(date(2020, 8, 1), date(2020, 8, 20))

        for rate_data in rates_data:
            print(rate_data)

        end = time.time()

        print(f"elapsed: {end - start}")


if __name__ == '__main__':
    asyncio.run(main())
