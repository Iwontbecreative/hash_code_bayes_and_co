from endpoint_stat import Endpoint, Request, Cache

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
        self.requests = []
        self.cache_list = []

    def parse(self):
        with open(self.filename, 'r') as input_f:
            lines = [line.strip('\n') for line in input_f.readlines()]
# Global parameters.
            self.n_videos, self.n_endpoints, self.n_requests, self.n_caches, self.cache_size = to_int(lines[0])
            self.video_sizes = to_int(lines[1])
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

    def store_requests(self):
        for i in range(self.n_endpoints):
            self.requests.extend(self.endpoints[i].requests)


    def compute_cache(self):
        created_caches = []

        for i in range(self.n_endpoints):
            for cache_id in self.endpoints[i].latencies.keys():
                if cache_id in created_caches:
                    j = 0
                    while self.cache_list[j].index != cache_id :
                        j += 1
                    self.cache_list[j].endpoints.append(self.endpoints[i])
                else:
                    self.cache_list.append(Cache(cache_id))
                    created_caches.append(cache_id)
                    self.cache_list[len(self.cache_list) - 1].endpoints.append(self.endpoints[i])
