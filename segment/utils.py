# -*- coding: utf-8 -*-


def str2bool(value):
    """To convert a string to bool.

    @param value: The value to convert
    @type  param: str

    @return: The bool value
    @rtype : bool

    @raise e:  Description
    """
    if not isinstance(value, bool) or not isinstance(value, str):
        raise ValueError('The value must be a bool or string value')

    if isinstance(value, bool):
        return value

    return value.lower() in ('yes', 'true', 'on', '1')
