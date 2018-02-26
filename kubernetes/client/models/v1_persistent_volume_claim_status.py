# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PersistentVolumeClaimStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_modes': 'list[str]',
        'capacity': 'dict(str, str)',
        'conditions': 'list[V1PersistentVolumeClaimCondition]',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, capacity=None, conditions=None, phase=None):
        """
        V1PersistentVolumeClaimStatus - a model defined in Swagger
        """

        self._access_modes = None
        self._capacity = None
        self._conditions = None
        self._phase = None
        self.discriminator = None

        if access_modes is not None:
          self.access_modes = access_modes
        if capacity is not None:
          self.capacity = capacity
        if conditions is not None:
          self.conditions = conditions
        if phase is not None:
          self.phase = phase

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeClaimStatus.
        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :return: The access_modes of this V1PersistentVolumeClaimStatus.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeClaimStatus.
        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :param access_modes: The access_modes of this V1PersistentVolumeClaimStatus.
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeClaimStatus.
        Represents the actual resources of the underlying volume.

        :return: The capacity of this V1PersistentVolumeClaimStatus.
        :rtype: dict(str, str)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeClaimStatus.
        Represents the actual resources of the underlying volume.

        :param capacity: The capacity of this V1PersistentVolumeClaimStatus.
        :type: dict(str, str)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """
        Gets the conditions of this V1PersistentVolumeClaimStatus.
        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.

        :return: The conditions of this V1PersistentVolumeClaimStatus.
        :rtype: list[V1PersistentVolumeClaimCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1PersistentVolumeClaimStatus.
        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.

        :param conditions: The conditions of this V1PersistentVolumeClaimStatus.
        :type: list[V1PersistentVolumeClaimCondition]
        """

        self._conditions = conditions

    @property
    def phase(self):
        """
        Gets the phase of this V1PersistentVolumeClaimStatus.
        Phase represents the current phase of PersistentVolumeClaim.

        :return: The phase of this V1PersistentVolumeClaimStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1PersistentVolumeClaimStatus.
        Phase represents the current phase of PersistentVolumeClaim.

        :param phase: The phase of this V1PersistentVolumeClaimStatus.
        :type: str
        """

        self._phase = phase

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
