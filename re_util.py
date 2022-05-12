import re
from typing import List



def extract_url(tweet : str) -> List[str]:
    result: List[str] = []

    pattern = re.compile(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+')
    result = re.findall(pattern, tweet)

    return result


def extract_hash(unsearched_string : str) -> List[str]:
    hashes: List[str] = []

    pattern = re.compile(r'\b[0-9a-fA-F]{40}\b')
    result = re.findall(pattern, unsearched_string)
    for sha1 in result:
        if sha1 not in hashes:
            hashes.append(sha1)

    pattern = re.compile(r'\b[0-9a-fA-F]{64}\b')
    result = re.findall(pattern, unsearched_string)
    for sha256 in result:
        if sha256 not in hashes:
            hashes.append(sha256)

    pattern = re.compile(r'\b[0-9a-fA-F]{32}\b')
    result = re.findall(pattern, unsearched_string)
    for md5 in result:
        if md5 not in hashes:
            hashes.append(md5)
    
    return hashes