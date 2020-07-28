import os
import argparse
from multiprocessing.dummy import Pool as ThreadPool

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                  
		os.makedirs(path)
        
def get_parser():
    parser = argparse.ArgumentParser(description='multi run')
    parser.add_argument('--list', type=str, help='list file path')
    parser.add_argument('--root', type=str, help='image root directory')
    parser.add_argument('--out', type=str, help='out directory')
    parser.add_argument('--model', type=str, help='model')
    parser.add_argument('--show', type=int, default=1, help='show frequency')
    return parser.parse_args()

def process(line):
    args = get_parser()
    image_name_1 = line.strip(' \n').split(' ')[0]
    image_name_2 = line.strip(' \n').split(' ')[1]
    mkdir(os.path.join(args.out, image_name_1.split('/')[0]))
    out_name = os.path.join(args.out, image_name_1.split('.')[0] + '.flo')
    image_name_1 = os.path.join(args.root, image_name_1)
    image_name_2 = os.path.join(args.root, image_name_2)
    os.system('python run.py --model ' + args.model + ' --first '+ image_name_1 \
        + ' --second ' + image_name_2 + ' --out ' + out_name)
    print(line.strip(' \n').split(' ')[0])
	
def main():
    args = get_parser()
    with open(args.list) as f:
        pair_list = f.readlines()
    pool = ThreadPool()
    pool.map(process, pair_list)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
