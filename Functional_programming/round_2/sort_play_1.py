import glob

def file_size(filename):
    return len(open(filename).read())

conf_f = glob.glob('*.txt')

conf_f.sort(key=file_size)
print conf_f


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': int(size)}

def by_size(one_shoe):
    xx = one_shoe['brand'], one_shoe['size']
    print xx
    return one_shoe['brand'], one_shoe['size']  # this is returning a tuple of two items

shoe_list = [line_to_dict(one_line_shoes)
             for one_line_shoes in open('shoe-data.txt')]

# takes each line, looks for the size k/v and sorts on v
shoe_list.sort(key=by_size)
for s in shoe_list:
    print s


