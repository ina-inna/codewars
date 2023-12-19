def domain_name(url):
    if 'www.' in url:
        parts = url.split('www.')
        if len(parts) > 0:
            new_url = parts[1]
            index = new_url.find('.')
            if index != -1:
                return new_url[:index]
            else:
                return ''
        else:
            return ''
    elif '//' in url:
        parts = url.split('//')
        if len(parts) > 0:
            new_url = parts[1]
            index = new_url.find('.')
            if index != -1:
                return new_url[:index]
            else:
                return ''
        else:
            return ''
    else:
        index = url.find('.')
        if index != -1:
            return url[:index]
        else:
            return ''