from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent
from tribler.core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler.core.components.session import Session
from tribler.core.components.tag.tag_component import TagComponent


# pylint: disable=protected-access


async def test_tag_component(tribler_config):
    components = [MetadataStoreComponent(), KeyComponent(), Ipv8Component(), TagComponent()]
    async with Session(tribler_config, components) as session:
        comp = session.get_instance(TagComponent)
        assert comp.started_event.is_set() and not comp.failed
        assert comp.community
