from endpoint import Endpoint, Request

def to_int(list_of_str):
    return [int(i) for i in list_of_str.split(' ')]

class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.n_videos = 0
        self.n_endpoints = 0
        self.n_requests = 0
        self.n_caches = 0
        self.cache_size = 0
        self.endpoints = []
        self.video_sizes = []

    def parse(self):
        with open(self.filename, 'r') as input_f:
            lines = [line.strip('\n') for line in input_f.readlines()]
# Global parameters.
            self.n_videos, self.n_endpoints, self.n_requests, self.n_caches, self.cache_size = to_int(lines[0])
            self.vide_sizes = to_int(lines[1])
# Endpoints
            number_handled = 0
            i = 2
            while number_handled != self.n_endpoints:
                dc_latency, caches = to_int(lines[i])
                i += caches
# Register the latencies for this datacenter.
                latencies = {}
                for j in range(1, 1 + caches):
                    info = to_int(lines[i+j])
                    latencies[info[0]] = info[1]
                self.endpoints.append(Endpoint(number_handled, dc_latency, latencies))
                number_handled += 1
                i += 1

            number_handled = 0
            for j in range(i, self.n_requests+i):
                video, source, qty = to_int(lines[j])
                self.endpoints[source].requests.append(Request(number_handled, video, qty))
