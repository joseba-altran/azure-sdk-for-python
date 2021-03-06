# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import AzureDigitalTwinsAPIConfiguration
from .operations_async import DigitalTwinModelsOperations
from .operations_async import QueryOperations
from .operations_async import DigitalTwinsOperations
from .operations_async import EventRoutesOperations
from .. import models


class AzureDigitalTwinsAPI(object):
    """A service for managing and querying digital twins and digital twin models.

    :ivar digital_twin_models: DigitalTwinModelsOperations operations
    :vartype digital_twin_models: azure.digitaltwins.core.aio.operations_async.DigitalTwinModelsOperations
    :ivar query: QueryOperations operations
    :vartype query: azure.digitaltwins.core.aio.operations_async.QueryOperations
    :ivar digital_twins: DigitalTwinsOperations operations
    :vartype digital_twins: azure.digitaltwins.core.aio.operations_async.DigitalTwinsOperations
    :ivar event_routes: EventRoutesOperations operations
    :vartype event_routes: azure.digitaltwins.core.aio.operations_async.EventRoutesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://digitaltwins-name.digitaltwins.azure.net'
        self._config = AzureDigitalTwinsAPIConfiguration(credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.digital_twin_models = DigitalTwinModelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.digital_twins = DigitalTwinsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.event_routes = EventRoutesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureDigitalTwinsAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
