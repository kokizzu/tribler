from typing import Optional

from ipv8.bootstrapping.dispersy.bootstrapper import DispersyBootstrapper
from ipv8.dht.discovery import DHTDiscoveryCommunity
from ipv8.peer import Peer
from ipv8.peerdiscovery.community import DiscoveryCommunity

from ipv8_service import IPv8

from tribler_core.components.base import Component


class Ipv8Component(Component):
    ipv8: IPv8
    peer: Peer
    bootstrapper: Optional[DispersyBootstrapper]
    peer_discovery_community: Optional[DiscoveryCommunity]
    dht_discovery_community: Optional[DHTDiscoveryCommunity]
