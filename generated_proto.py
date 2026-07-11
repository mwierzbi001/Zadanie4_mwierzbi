import ctypes

class SensorReportStructure(ctypes.Structure):
    _fields_ = [
        
        
        ('sensor_id', ctypes.c_int32),
        
        
        
        ('reading', ctypes.c_float),
        
        
        
        ('status_code', ctypes.c_char * 16),
        
        
    ]

class SensorReport:
    def __init__(self, sensor_id, reading, status_code):
        
        self.sensor_id = sensor_id
        
        self.reading = reading
        
        self.status_code = status_code
        

    def serialize(self) -> bytes:
        # Tworzymy surow¹ strukturê ctypes
        struct_instance = SensorReportStructure()

        
        
        struct_instance.sensor_id = self.sensor_id
        
        
        
        struct_instance.reading = self.reading
        
        
        
        struct_instance.status_code = self.status_code.encode('utf-8')
        
        

        # Przekszta³camy strukturê bezpoœrednio w bajty
        return bytes(struct_instance)

    @classmethod
    def deserialize(cls, data: bytes):
        # Odtwarzamy strukturê z bajtów
        struct_instance = SensorReportStructure.from_buffer_copy(data)

        return cls(
            
            
            sensor_id=struct_instance.sensor_id,
            
            
            
            reading=struct_instance.reading,
            
            
            
            status_code=struct_instance.status_code.decode('utf-8').strip('\x00')
            
            
        )