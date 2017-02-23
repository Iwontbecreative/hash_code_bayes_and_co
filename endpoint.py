class Endpoint:
    def __init__(self, index, dc_latency, latencies):
        self.index = index
        self.dc_latency = dc_latency
        self.latencies = latencies
        self.requests = []

class Request:
    def __init__(self, index, source, video, qty):
        self.index = index
        self.source = source
        self.video = video
        self.qty = qty

class Video:
    def __init__(self, index):
        self.index = index
        self.requests = []

    def get_num_requests(self):
        pass


