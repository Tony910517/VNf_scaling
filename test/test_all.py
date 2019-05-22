import random
from request import Request
from resource import Resource
from SFC_process import VNF_Group
import openstack_setting

disk_value = [10, 20, 30]
ram_value = [1, 2, 4]
vcpu_value = [1, 2, 4]
request_time = 3

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
        request = Request()
        request.resource.set_resource(vcpu, disk, ram)
        requests.append(request)
    return requests


def test():
    nova_client = openstack_setting.openstack_auth()

    for request in set_requests():
        print(request)
        input("input something: ")
        vnf_test1 = VNF_Group(request, name='test1', image_name='cirros')
        vnf_test1.get_vnf_group()
        vnf_test1.vnf_deployment()
        print('*' * 20)
        print(vnf_test1.get_count())
        print('*' * 20)

        openstack_setting.remove_allvm(nova_client)



if __name__ == '__main__':
    test()