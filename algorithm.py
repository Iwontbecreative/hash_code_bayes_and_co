from parser import Parser
import numpy as np
import pandas as pd



parser = Parser('data/me_at_the_zoo.in')
parser.parse()


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

mega_string = str(parser.n_caches) + "\n"
for i, cache in enumerate(scores):
    weight = 0
    to_add = []
    for vid in cache.index:
        if not (parser.video_sizes[vid] + weight < parser.cache_size):
            break
        to_add.append(vid)
        weight += parser.video_sizes[vid]
    mega_string += "{} {}\n".format(str(i), " ".join([str(i) for i in to_add]))
with open('test.out', 'w') as out:
    out.write(mega_string)


# scores = pd.DataFrame(scores)
# scores = scores.sort
