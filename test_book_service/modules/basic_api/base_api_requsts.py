import requests


def post_request(request_url: str, request_json: dict, header: dict):
    """Function for POST request execution

    :param request_url: endpoint where to send the request
    :param request_json: finalized json of the request
    :param header: finalized dict with headers
    :return: response obj
    """
    post_response = requests.post(url=request_url,
                                  json=request_json,
                                  headers=header)
    return post_response


def put_request(request_url: str, request_json: dict, header: dict, param: dict = None):
    """Function for PUT request execution

    :param request_url: endpoint where to send the request
    :param request_json: finalized json of the request
    :param header: finalized dict with headers
    :param param: finalized parameters dict of the request
    :return: response obj
    """
    put_response = requests.put(url=request_url,
                                json=request_json,
                                headers=header,
                                params=param)
    return put_response


def get_request(request_url: str, header: dict, param: dict = None):
    """Function for GET request execution

    :param request_url: endpoint where to send the request
    :param param: finalized parameters dict of the request
    :param header: finalized dict with headers
    :return: response obj
    """
    if param:
        get_response = requests.get(url=request_url,
                                    headers=header,
                                    params=param)
    else:
        get_response = requests.get(url=request_url,
                                    headers=header)
    return get_response


def delete_request(request_url: str, param: dict, header: dict):
    """Function for POST request execution

    :param request_url: endpoint where to send the request
    :param param: finalized parameters dict of the request
    :param header: finalized dict with headers
    :return: response obj
    """
    delete_response = requests.delete(url=request_url,
                                      params=param,
                                      headers=header)
    return delete_response
