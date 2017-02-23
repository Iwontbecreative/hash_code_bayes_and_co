from parser import Parser
import numpy as np
import pandas as pd
from glob import glob


for filename in glob('data/*.in'):
    parser = Parser(filename)
    parser.parse()
    print('Wroking with file {}'.format(filename))


    scores = np.zeros((parser.n_videos, parser.n_caches))
    scores = []

    for cache in range(parser.n_caches):
        scores.append([])
        for video in parser.videos:
            score = 0
            for req in video.requests:
                dc_lat = parser.endpoints[req.source].dc_latency
                lat = parser.endpoints[req.source].latencies.get(cache, 0)
                score += (dc_lat - lat) * req.qty
            score = score / parser.video_sizes[video.index]
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
    with open('{}.out'.format(filename), 'w') as out:
        out.write(mega_string)

# scores = pd.DataFrame(scores)
# scores = scores.sort
