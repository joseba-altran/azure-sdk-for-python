# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import TemplateSpecsClientConfiguration
from .operations import TemplateSpecsOperations
from .operations import TemplateSpecVersionsOperations
from . import models


class TemplateSpecsClient(SDKClient):
    """The APIs listed in this specification can be used to manage Template Spec resources through the Azure Resource Manager.

    :ivar config: Configuration for client.
    :vartype config: TemplateSpecsClientConfiguration

    :ivar template_specs: TemplateSpecs operations
    :vartype template_specs: azure.mgmt.resource.templatespecs.v2019_06_preview.operations.TemplateSpecsOperations
    :ivar template_spec_versions: TemplateSpecVersions operations
    :vartype template_spec_versions: azure.mgmt.resource.templatespecs.v2019_06_preview.operations.TemplateSpecVersionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription Id which forms part of the URI for
     every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = TemplateSpecsClientConfiguration(credentials, subscription_id, base_url)
        super(TemplateSpecsClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.template_specs = TemplateSpecsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.template_spec_versions = TemplateSpecVersionsOperations(
            self._client, self.config, self._serialize, self._deserialize)