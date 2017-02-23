from parser import Parser
import numpy as np
import pandas as pd

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

scores = np.zeros((parser.n_videos, parser.n_caches))
scores = []

for cache in range(parser.n_caches):
    scores.append([])
    for video in range(parser.n_videos):
        score = 0
        for endpoint in parser.endpoints:
            if cache not in endpoint.latencies.keys():
                continue
            for req in endpoint.requests:
                if req.video == video:
                    score += (endpoint.dc_latency - endpoint.latencies[cache]) * req.qty
        score = score / parser.video_sizes[video]
        scores[cache].append(score)

scores = [pd.Series(l).sort_values(ascending=False) for l in scores]
print(scores[0])
# scores = pd.DataFrame(scores)
# scores = scores.sort
