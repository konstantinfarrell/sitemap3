import aiohttp
import argparse
import asyncio
import ssl

from urllib.parse import urlsplit

from bs4 import BeautifulSoup

from sitemap.utils import write_text_sitemap, clean_link

# Have these at global scope so they remain shared.
urls = []
results = []


def sitemap(url, verbose=False):
    """ Main mapping function.
    Clears old results, adds the starting url to the pool of urls,
    creates and runs an event loop, writes out if necessary.
    """
    if len(results) > 0:
        del results[:]
    urls.append(url)

    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()

    loop.run_until_complete(asyncio.ensure_future(crawler(urls, results, verbose)))

    return results


async def crawler(urls, results, verbose):
    """ Crawls urls that aren't already in the results list """
    while len(urls) > 0:
        await asyncio.gather(*[asyncio.ensure_future(crawl(url, verbose)) for url in urls if url not in results])


async def crawl(url, verbose):
    """ Moves current url from urls pool to results,
    gets, cleans & parses html content for new urls,
    appends new urls to urls pool.
    """
    results.append(url)
    try:
        urls.remove(url)
    except ValueError:
        pass

    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(url=url, method='GET') as response:
                if response.content_type == 'text/html':
                    content = await response.read()
                    clean_content(content, url, verbose)
    except ssl.SSLError as e:
        pass
    except aiohttp.ClientError as e:
        pass


def clean_content(content, url, verbose):
    """ Parse a webpage for links """
    soup = BeautifulSoup(content, 'html.parser')
    domain = "{0.scheme}://{0.netloc}".format(urlsplit(url))
    for link in [h.get('href') for h in soup.find_all('a')]:
        link = clean_link(link, domain)
        if link is not None:
            if link not in urls and link not in results:
                urls.append(link)
                if verbose:
                    print(link)


def main():
    parser = argparse.ArgumentParser()                  # pragma: no cover
    parser.add_argument(                                # pragma: no cover
        "-u", "--u",                                    # pragma: no cover
        help="Base url of the site to be mapped",       # pragma: no cover
        dest="url"                                      # pragma: no cover
    )                                                   # pragma: no cover
    parser.add_argument(                                # pragma: no cover
        "--w",                                          # pragma: no cover
        help="Write output to file",                    # pragma: no cover
        dest="output"                                   # pragma: no cover
    )                                                   # pragma: no cover
    args = parser.parse_args()                          # pragma: no cover

    if args.output:                                     # pragma: no cover
        out = sitemap(url=args.url)                     # pragma: no cover
        write_text_sitemap(out, args.output)
    elif args.url:                                      # pragma: no cover
        sitemap(url=args.url, verbose=True)             # pragma: no cover
    else:                                               # pragma: no cover
        parser.print_help()                             # pragma: no cover


if __name__ == '__main__':
    main()
