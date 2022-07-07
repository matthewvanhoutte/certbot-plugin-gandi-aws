import boto3
from typing import List
from collections import namedtuple


def get_params(params: List[str], kwargs_client=None, kwargs_get_param=None):
    """
    Get AWS SSM Parameters

    Args:
        params (list): Parameters to collect from SSM
        kwargs_client (dict): Any keyword arguments for the client, i.e. region
        kwargs_get_param (dict): Keyword args for the ssm get operation

    Returns:
        values: A namedtuple contains values by param name
    """

    if kwargs_get_param is None:
        kwargs_get_param = {}
    if kwargs_client is None:
        kwargs_client = {}
    client = boto3.client('ssm', **kwargs_client)
    response = client.get_parameters(
        Names=params,
        **kwargs_get_param
    )

    return _get_values(params, response)


def _get_values(params, response):
    """
    Get the values of the parameters and return them as Named Tuple
    """
    _ParamVals = namedtuple('_ParamVals', params)

    vals = {}
    for param in response.get('Parameters'):
        name = param.get('Name')
        val = param.get('Value')
        vals[name] = val

    return _ParamVals(**vals)

