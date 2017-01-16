import aiohttp
import argparse
import asyncio
from urllib.parse import urlsplit

from bs4 import BeautifulSoup


async def crawl(url, links=[], not_visited=[]):
    if url not in links:
        links.append(url)
    links, not_visited = await parse_links(url, links, not_visited)

    # Tried this and it was really slow
    await asyncio.wait([asyncio.ensure_future(crawl(link, links, not_visited)) for link in not_visited])

    #for link in not_visited:
    #    try:
    #        await crawl(link, links, not_visited)
    #    except RecursionError:
    #        break
    return links


async def parse_links(url, links, not_visited):
    if url in not_visited:
        not_visited.remove(url)
    response = await get_content(url)
    soup = BeautifulSoup(response, 'html.parser')
    domain = "{0.scheme}://{0.netloc}".format(urlsplit(url))
    for link in [h.get('href') for h in soup.find_all('a')]:
        link = await clean_link(link, domain)
        if link is not None:
            if link not in links:
                links.append(link)
                not_visited.append(link)
                print(link)
    return links, not_visited


async def get_content(url):
    response = await aiohttp.get(url)
    return (await response.text())


async def clean_link(link, domain):
    if link is not None:
        if link.startswith('/') or link.startswith(domain):
            if link.startswith('/'):
                link = '{}{}'.format(domain, link)
            if '?' in link:
                link = link.split('?')[0]
            return link


def sitemap(url, output='sitemap.txt', write=True):
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
    try:
        result = loop.run_until_complete(crawl(url))
    finally:
        loop.close()
    if write:
        with open(output, 'w') as f:
            f.write(str('\n'.join(result)))
    return result


def main():
    parser = argparse.ArgumentParser()                                      # pragma: no cover
    parser.add_argument("url", help="Base url of the site to be mapped")    # pragma: no cover

    args = parser.parse_args()                                              # pragma: no cover

    sitemap(args.url)                                                       # pragma: no cover
