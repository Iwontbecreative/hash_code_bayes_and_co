class Endpoint:
    def __init__(self, index, dc_latency, latencies):
        self.index = index
        self.dc_latency = dc_latency
        self.latencies = latencies
        self.requests = []

class Request:
    def __init__(self, index, video, qty):
        self.index = index
        self.video = video
        self.qty = qty
