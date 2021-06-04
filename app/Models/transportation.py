# Class ini digunakan untuk menyimpan data Transportation dari database travelnesia
class Transportation:
    # Constructor ini digunakan untuk inisialiasi data dari class Transportation
    def __init__(self, transport_id, transport, type):
        self.transport_id = transport_id
        self.transport = transport
        self.type = type
