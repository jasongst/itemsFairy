import asyncio
import nodriver as uc

from VintedScraper import VintedScraper

async def main():
    browser = await uc.start()
    vinted_scraper = VintedScraper(browser)
    # Test with jean
    await vinted_scraper.ascrape_vinted("jean levis")

asyncio.run(main())