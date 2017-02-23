from parser import Parser

parser = Parser('data/me_at_the_zoo.in')
parser.parse()

video = 0
cache = 0
score = 0
# for endpoint in parser.endpoints:
    # diff_lat = -1
    # if cache in endpoint.latencies.keys():
        # cache_lat = endpoint.latencies[cache]
        # diff_lat = endpoint.dc_latency - cache_lat
        # for req in parser.requests:
            # if req.video == video and req.source == endpoint.index:
                # score += diff_lat * req.qty

# print(score)


for req in parser.requests:
