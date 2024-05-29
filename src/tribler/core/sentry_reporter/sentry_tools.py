""" This a collection of tools for SentryReporter and SentryScrubber aimed to
simplify work with several data structures.
"""
import re
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, TypeVar

from faker import Faker

# Remove the substring like "Sentry is attempting to send 1 pending error messages"
_re_remove_sentry = re.compile(r'Sentry is attempting.*')


@dataclass
class LastCoreException:
    type: str
    message: str


def get_first_item(items, default=None):
    return items[0] if items else default


def get_last_item(items, default=None):
    return items[-1] if items else default


def delete_item(d, key):
    if not d:
        return d

    if key in d:
        del d[key]
    return d


def get_value(d, key, default=None):
    return d.get(key, default) if d else default


def extract_dict(d, regex_key_pattern):
    if not d or not regex_key_pattern:
        return dict()

    matched_keys = [key for key in d if re.match(regex_key_pattern, key)]
    return {key: d[key] for key in matched_keys}


def modify_value(d, key, function):
    if not d or not key or not function:
        return d

    if key in d:
        d[key] = function(d[key])

    return d


T = TypeVar('T')


def distinct_by(items: Optional[List[T]], getter: Callable[[T], Any]) -> Optional[List[T]]:
    """This function removes all duplicates from a list of dictionaries. A duplicate
    here is a dictionary that have the same value of the given key.

    If no key field is presented in the dictionary, then the exception will be raised.

    Args:
        items: list of dictionaries
        getter: function that returns a key for the comparison

    Returns:
        Array of distinct items
    """

    if not items:
        return items

    distinct = {}
    for item in items:
        key = getter(item)
        if key not in distinct:
            distinct[key] = item
    return list(distinct.values())


def format_version(version: Optional[str]) -> Optional[str]:
    if not version:
        return version

    # For the release version let's ignore all "developers" versions
    # to keep the meaning of the `latest` keyword:
    # See Also:https://docs.sentry.io/product/sentry-basics/search/
    if 'GIT' in version:
        return 'dev'

    parts = version.split('-', maxsplit=2)
    if len(parts) < 2:
        return version

    # if version has been produced by deployment tester, then
    if parts[1].isdigit():
        return parts[0]

    # for all other cases keep <version>-<first_part>
    return f"{parts[0]}-{parts[1]}"


def obfuscate_string(s: str, part_of_speech: str = 'noun') -> str:
    """Obfuscate string by replacing it with random word.

    The same random words will be generated for the same given strings.
    """
    faker = Faker(locale='en_US')
    faker.seed_instance(s)
    return faker.word(part_of_speech=part_of_speech)


def order_by_utc_time(breadcrumbs: Optional[List[Dict]], key: str = 'timestamp'):
    """ Order breadcrumbs by timestamp in ascending order.

    Args:
        breadcrumbs: List of breadcrumbs
        key: Field name that will be used for sorting

    Returns:
        Ordered list of breadcrumbs
    """
    if not breadcrumbs:
        return breadcrumbs

    return list(sorted(breadcrumbs, key=lambda breadcrumb: breadcrumb[key]))
