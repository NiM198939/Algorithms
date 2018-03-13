# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segments: segments.start)
    n = len(segments)
    final_points = []
    initial = list(range(segments[0].start,segments[0].end+1))
    for s in segments:
        l = list(range(s.start,s.end+1))
        intersect = list(set(initial) & set(l))
        if len(intersect)==0:
            final_points.append(initial[len(initial)-1])
            initial = list(l)
        else:
            initial = intersect
    if len(intersect)!=0:
        final_points.append(intersect[len(intersect)-1])  
    else:
        final_points.append(l[len(l)-1])    
    return final_points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')