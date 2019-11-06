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

from .update_resource import UpdateResource


class FormulaFragment(UpdateResource):
    """A formula for creating a VM, specifying an image base and other parameters.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param description: The description of the formula.
    :type description: str
    :param author: The author of the formula.
    :type author: str
    :param os_type: The OS type of the formula.
    :type os_type: str
    :param formula_content: The content of the formula.
    :type formula_content:
     ~azure.mgmt.devtestlabs.models.LabVirtualMachineCreationParameterFragment
    :param vm: Information about a VM from which a formula is to be created.
    :type vm: ~azure.mgmt.devtestlabs.models.FormulaPropertiesFromVmFragment
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'formula_content': {'key': 'properties.formulaContent', 'type': 'LabVirtualMachineCreationParameterFragment'},
        'vm': {'key': 'properties.vm', 'type': 'FormulaPropertiesFromVmFragment'},
    }

    def __init__(self, **kwargs):
        super(FormulaFragment, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.author = kwargs.get('author', None)
        self.os_type = kwargs.get('os_type', None)
        self.formula_content = kwargs.get('formula_content', None)
        self.vm = kwargs.get('vm', None)