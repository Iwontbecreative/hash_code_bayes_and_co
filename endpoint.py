class Endpoint:
    def __init__(self, dc_latency, latencies):
        self.dc_latency = dc_latency
        self.latencies = latencies

class Request:
    def __init__(self, video, source, dest):
        self.video = video
        self.source = source
        self.dest = dest
