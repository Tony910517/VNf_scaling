

class Resource():

    def __init__(self):
        self.vcpus = 0
        self.disk = 0
        self.ram = 0

    def set_resource(self, vcpu, disk, ram):
        self.vcpus = vcpu
        self.disk = disk
        self.ram = ram

    def resource_equal(self, Resource):
        weather_vcpu_equal = (Resource.vcpus==self.vcpu)
        weather_disk_equal = (Resource.disk==self.disk)
        weather_ram_equal = (Resource.ram==self.ram)
        if weather_vcpu_equal and weather_disk_equal and weather_ram_equal:
            return 1
        else:
            return 0