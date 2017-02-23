from parser import Parser
import numpy as np
import pandas as pd
from glob import glob


def update_latencies(cache, to_add):
    for end in parser.endpoints:
        if cache in end.latencies.keys():
            for vid in to_add:
                end.video_lat[vid] = end.latencies[cache]

for filename in glob('data/*.in'):
    parser = Parser(filename)
    parser.parse()
    print('Wroking with file {}'.format(filename))


    for end in parser.endpoints:
        end.video_lat = [end.dc_latency] * parser.n_videos

    scores = []
    mega_string = str(parser.n_caches) + "\n"

    for cache in range(parser.n_caches):
        scores.append([])
        for video in parser.videos:
            score = 0
            for req in video.requests:
                dc_lat = parser.endpoints[req.source].video_lat[video.index]
                lat = parser.endpoints[req.source].latencies.get(cache, 0)
                score += (dc_lat - lat) * req.qty
            score = score / parser.video_sizes[video.index]
            scores[cache].append(score)
        scores[cache] = pd.Series(scores[cache]).sort_values(ascending=False)

        weight = 0
        to_add = []
        for vid in scores[cache].index:
            if not (parser.video_sizes[vid] + weight < parser.cache_size):
                break
            to_add.append(vid)
            weight += parser.video_sizes[vid]
        mega_string += "{} {}\n".format(str(cache), " ".join([str(i) for i in to_add]))

        update_latencies(cache, to_add)

    with open('{}.out'.format(filename), 'w') as out:
        out.write(mega_string)

# scores = pd.DataFrame(scores)
# scores = scores.sort
