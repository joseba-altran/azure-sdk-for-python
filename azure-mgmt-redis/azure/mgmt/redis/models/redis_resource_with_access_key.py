# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class RedisResourceWithAccessKey(Resource):
    """
    A redis item in CreateOrUpdate Operation response.

    :param id: Resource Id
    :type id: str
    :param name: Resource name
    :type name: str
    :param type: Resource type
    :type type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param redis_version: RedisVersion parameter has been deprecated. As
     such, it is no longer necessary to provide this parameter and any value
     specified is ignored.
    :type redis_version: str
    :param sku: What sku of redis cache to deploy.
    :type sku: :class:`Sku <azure.mgmt.redis.models.Sku>`
    :param redis_configuration: All Redis Settings. Few possible keys:
     rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
     etc.
    :type redis_configuration: dict
    :param enable_non_ssl_port: If the value is true, then the non-ssl redis
     server port (6379) will be enabled.
    :type enable_non_ssl_port: bool
    :param tenant_settings: tenantSettings
    :type tenant_settings: dict
    :param shard_count: The number of shards to be created on a Premium
     Cluster Cache.
    :type shard_count: int
    :param virtual_network: The exact ARM resource ID of the virtual network
     to deploy the redis cache in. Example format:
     /subscriptions/{subid}/resourceGroups/{resourceGroupName}/Microsoft.ClassicNetwork/VirtualNetworks/vnet1
    :type virtual_network: str
    :param subnet: Required when deploying a redis cache inside an existing
     Azure Virtual Network.
    :type subnet: str
    :param static_ip: Required when deploying a redis cache inside an
     existing Azure Virtual Network.
    :type static_ip: str
    :param provisioning_state: Redis instance provisioning status
    :type provisioning_state: str
    :param host_name: Redis host name
    :type host_name: str
    :param port: Redis non-ssl port
    :type port: int
    :param ssl_port: Redis ssl port
    :type ssl_port: int
    :param access_keys: Redis cache access keys.
    :type access_keys: :class:`RedisAccessKeys
     <azure.mgmt.redis.models.RedisAccessKeys>`
    """ 

    _validation = {
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'redis_version': {'key': 'properties.redisVersion', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'redis_configuration': {'key': 'properties.redisConfiguration', 'type': '{str}'},
        'enable_non_ssl_port': {'key': 'properties.enableNonSslPort', 'type': 'bool'},
        'tenant_settings': {'key': 'properties.tenantSettings', 'type': '{str}'},
        'shard_count': {'key': 'properties.shardCount', 'type': 'int'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'str'},
        'static_ip': {'key': 'properties.staticIP', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'ssl_port': {'key': 'properties.sslPort', 'type': 'int'},
        'access_keys': {'key': 'properties.accessKeys', 'type': 'RedisAccessKeys'},
    }

    def __init__(self, location, sku, id=None, name=None, type=None, tags=None, redis_version=None, redis_configuration=None, enable_non_ssl_port=None, tenant_settings=None, shard_count=None, virtual_network=None, subnet=None, static_ip=None, provisioning_state=None, host_name=None, port=None, ssl_port=None, access_keys=None):
        super(RedisResourceWithAccessKey, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.redis_version = redis_version
        self.sku = sku
        self.redis_configuration = redis_configuration
        self.enable_non_ssl_port = enable_non_ssl_port
        self.tenant_settings = tenant_settings
        self.shard_count = shard_count
        self.virtual_network = virtual_network
        self.subnet = subnet
        self.static_ip = static_ip
        self.provisioning_state = provisioning_state
        self.host_name = host_name
        self.port = port
        self.ssl_port = ssl_port
        self.access_keys = access_keys
