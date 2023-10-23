class DeviceGest(object):
    def __init__(self):
        self.device_number = 24500
        self.device_name = 'Concord devices needs to be built'

    def __repr__(self) -> str:
        return "Device object is returned"
    
    def device_local(self):
        device_loc = 23400
        return locals()
    
    def device_code(self):
        device_loc = 22000
        return vars()
    
    def device_pragma(self):
        device_loc = "Device location unknown"
        return vars(self)

if __name__ == "__main__":
    device_obj = DeviceGest()
    print(device_obj.device_local())
    print(device_obj.device_code())
    print(device_obj.device_pragma())