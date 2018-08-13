import requests
import config

url = config.URL
WEBPASSWORD = config.WEBPASSWORD
entries = config.entries

num1 = '={0}'.format(entries)
bold = '*'


def genstats():
    r = requests.get(url + '?summary').json()
    domains_blocked = r['domains_being_blocked']
    dns_queries = r['dns_queries_today']
    ads_blocked = r['ads_blocked_today']
    ads_percentage = r['ads_percentage_today']
    message = str(bold + "🌍Queries: " + bold + str(dns_queries) + "\n" +
                  bold + "✋Ads blocked: " + bold + str(ads_blocked) + "\n" +
                  bold + "📊Ads percentage: " + bold + str(ads_percentage) + "%" + "\n" +
                  bold + "🌐Total domains: " + bold + str(domains_blocked))
    return message

def top_it(tops, *args):
    r = requests.get(url + '?' + tops + num1 + '&auth=' + WEBPASSWORD).json()
    if tops == "topItems":
        for y in args[:1]:
            if y == 1:
                try:
                    top_queries = r['top_queries']
                    str1 = ""
                    for x, value in top_queries.items():
                        str1 += str("" if str1 == "" else "") + str(x) + ": " + str(value) + '\n'
                    message = str(bold + "🌍Top Queries:" + bold + "\n" + str1)
                    return message
                except AttributeError:
                    message = str(bold + "🌍Top Queries:" + bold + "\n" + "Is empty")
                    return message
            elif y == 2:
                try:
                    top_ads = r['top_ads']
                    str1 = ""
                    for x, value in top_ads.items():
                        str1 += str("" if str1 == "" else "") + str(x) + ": " + str(value) + '\n'
                    message = str(bold + "⛔Top Ads:" + bold + "\n" + str1)
                    return message
                except AttributeError:
                    message = str(bold + "⛔Top Ads:" + bold + "\n" + "Is empty")
                    return message
    else:
        try:
            top_sources = r['top_sources']
            str1 = ""
            for x, value in top_sources.items():
                str1 += str("" if str1 == "" else "") + str(x) + ": " + str(value) + '\n'
            message = str(bold + "👤Top Clients:" + bold + "\n" + str1)
            return message
        except AttributeError:
            message = str(bold + "👤Top Clients:" + bold + "\n" + "Is empty")
            return message

def check_status(status):
    if status == 'status':
        r = requests.get(url).json()
        cstatus = r['status']
        if cstatus == 'enabled':
            message = str(str(cstatus) + " ✅")
        else:
            message = str(str(cstatus) + " ❌")
    else:
        r = requests.get(url + '?' + status + '&auth=' + WEBPASSWORD).json()
        if status == 'enable':
            cstatus = r['status']
            message = str(str(cstatus) + " ✅")
        else:
            cstatus = r['status']
            message = str(str(cstatus) + " ❌")
    return message


# TODO Tempolary disable pihole : 30sec, 1m, 5m, 30m.
