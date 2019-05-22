import unittest
import pytest
import random
from Request import Request
from Resource import Resource

disk_value = [256, 512, 1024]
ram_value = [1, 4, 8]
vcpu_value = [1, 4, 8, 16]
request_time = 8

def get_random():
    """
    随机生成一个vcpu，disk，ram的随机数
    :return:
    """
    disk_value_len = len(disk_value) -1
    ram_value_len = len(ram_value) -1
    vcpu_value_len = len(vcpu_value)-1
    disk = disk_value[random.randint(0, disk_value_len)]
    ram = ram_value[random.randint(0, ram_value_len)]
    vcpu = vcpu_value[random.randint(0, vcpu_value_len)]
    return vcpu, disk, ram


def set_requests():
    """
    :return: request对象数组
    """
    requests = []
    for i in range(request_time):
        vcpu, disk, ram = get_random()
        resource = Resource(vcpu, disk, ram)
        resource.set_resource(vcpu, disk, ram)
        request = Request(None, resource)
        requests.append(request)
    return requests

def main():
    requests = set_requests()
   # for i in range(request_time):
    #    print(requests[i].resource.vcpu)
    print(requests[1].resource.resource_equal(requests[2].resource))

if __name__ == '__main__':
    main()