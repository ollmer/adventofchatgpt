fully_overlapped_pairs = 0

with open('input.txt') as f:
    for l in f:
        str_range1, str_range2 = l.strip().split(',')
        range1_start, range1_end = [int(s) for s in str_range1.split('-')]
        range2_start, range2_end = [int(s) for s in str_range2.split('-')]

        if range1_start <= range2_start and range1_end >= range2_end:
            fully_overlapped_pairs += 1
        elif range2_start <= range1_start and range2_end >= range1_end:
            fully_overlapped_pairs +=1

print(fully_overlapped_pairs)