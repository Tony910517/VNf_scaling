import pytest
import random

class TestClass(object):

    @pytest.fixture(scope="module")
    def static_value(request):
        disk_value = [256, 512, 1024]
        ram_value = [1, 4, 8]
        vcpu_value = [1, 4, 8, 16]
        request_time = 8
        return disk_value, ram_value,vcpu_value,request_time


    def test_get_random(static_value):
        """
        随机生成一个vcpu，disk，ram的随机数
        :return:
        """
        disk_value, ram_value,vcpu_value, request_time = static_value.ehlo()
        disk_value_len = len(disk_value) - 1
        ram_value_len = len(ram_value) - 1
        vcpu_value_len = len(vcpu_value) - 1
        disk = disk_value[random.randint(0, disk_value_len)]
        ram = ram_value[random.randint(0, ram_value_len)]
        vcpu = vcpu_value[random.randint(0, vcpu_value_len)]
        assert request_time == 0
        return vcpu, disk, ram

pytest.main()