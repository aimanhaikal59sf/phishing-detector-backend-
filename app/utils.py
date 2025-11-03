from urllib.parse import urlparse
import re
def extract_features(url: str):
    parsed = urlparse(url)
    domain = parsed.netloc or url
    url_length = len(url)
    num_subdomains = max(domain.count('.') - 1, 0)
    has_https = 1 if parsed.scheme == "https" else 0
    has_ip = 1 if re.match(r"^\d{1,3}(?:\.\d{1,3}){3}$", domain.split(':')[0]) else 0
    special_chars = sum(url.count(c) for c in ['@', '?', '-', '=', '_', '.', '#', '%', '&'])
    suspicious_keywords = 1 if any(kw in url.lower() for kw in ['login', 'update', 'secure', 'bank', 'verify']) else 0
    shortened = 1 if any(short in domain for short in ['bit.ly', 'goo.gl', 'tinyurl']) else 0
    uncommon_tld = 1 if re.search(r"\.(xyz|top|club|info|site|icu|online|vip|work|click)$", domain) else 0
    return [url_length, num_subdomains, has_https, has_ip, special_chars, suspicious_keywords, shortened, uncommon_tld]
