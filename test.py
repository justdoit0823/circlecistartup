# -*- coding: utf-8 -*-


import requests
import functools

_test_url_prefix = 'http://127.0.0.1:7777'

def test_block(func):

    @functools.wraps(func)
    def wrapper():
        func_name = func.__name__
        print('start test {0}'.format(func_name))
        ret = func()
        print('finish test {0}'.format(func_name))
        return ret
    return wrapper


@test_block
def test_helloword():

    uri = '/'
    test_url = _test_url_prefix + uri
    ret = requests.get(test_url)
    assert ret.status_code == 200
    assert ret.content == b'Hello world'


def main():
    test_helloword()


if __name__ == '__main__':
    main()
