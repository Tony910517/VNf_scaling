

class Resource():

    def __init__(self, vcpu, disk, ram):
        self.vcpu = 0
        self.disk = 0
        self.ram = 0

    def set_resource(self, vcpu, disk, ram):
        self.vcpu = vcpu
        self.disk = disk
        self.ram = ram

    def resource_equal(self, Resource):
        weather_vcup_equal = (Resource.vcpu==self.vcpu)
        weather_disk_equal = (Resource.disk==self.disk)
        weather_ram_equal = (Resource.ram==self.ram)
        if weather_vcup_equal==weather_disk_equal &  weather_ram_equal==1:
            return 1
        else:
            return 0