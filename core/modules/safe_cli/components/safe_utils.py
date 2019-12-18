#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SafeUtils:
    def __init__(self, logger, safe_interface):
        self.name = self.__class__.__name__
        self.logger = logger
        self.safe_interface = safe_interface

    def setinel_helper(self, address_value):
        """ Sender Helper
        This function calculate the sentinel for an owner within the safe-cli
        :param address_value:
        :return:
        """
        previous_owner = '0x' + ('0' * 39) + '1'
        self.logger.debug0('[ Current Owner with Address to be Removed ]: {0}'.format(str(address_value)))
        self.logger.debug0('[ Current Local Account Owners ]: {0}'.format(self.safe_interface.retrieve_owners()))

        for index, owner_address in enumerate(self.safe_interface.retrieve_owners()):
            if address_value == owner_address:
                self.logger.info('[ Found Owner in Owners ]: {0} with Index {1}'.format(owner_address, index))
                try:
                    sentinel_index = (index - 1)
                    self.logger.debug0('[ SENTINEL Address Index ]: {0}'.format(sentinel_index))
                    if index != 0:
                        current_owner_list = self.safe_interface.retrieve_owners()
                        previous_owner = current_owner_list[(index - 1)]
                    self.logger.info('[ Found PreviousOwner on the list ]: {0}'.format(previous_owner))
                    return previous_owner
                except IndexError:
                    self.logger.error('Sentinel Address not found, returning NULLADDRESS')