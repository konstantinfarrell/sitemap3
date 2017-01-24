def clean_link(link, domain):
    """ Returns a cleaned url if it is worthwhile.
    Otherwise returns None.
    """
    avoid = ['.exe', '.pdf', '.png', '.jpg', '.iso', '.bat', '.gz']
    avoid_in_url = ['javascript:', 'mailto:', 'Javascript:', ]
    if link is not None:
        for a in avoid:
            if link.lower().endswith(a):
                return None
        for a in avoid_in_url:
            if a in link:
                return None
        if link.count('http') > 1:
            return None
        if not link.startswith('//'):
            if link.startswith('/') or link.startswith(domain) or not link.startswith('http'):
                if not (link.startswith('http') or link.startswith('/')):
                    link = '/{}'.format(link)
                if link.startswith('/'):
                    link = '{}{}'.format(domain, link)
                if '?' in link and 'asp?' not in link:
                    link = link.split('?')[0]
                return link


def write_text_sitemap(results, output='sitemap.txt'):
    with open(output, 'w') as f:
        f.write(str('\n'.join(results)))
