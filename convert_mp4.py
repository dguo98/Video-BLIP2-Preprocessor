import os
import sys
import numpy
import argparse
from glob import glob
from tqdm import tqdm

if __name__ == "__main__":
    in_dir = sys.argv[1]
    print("input directory:", in_dir)
    out_dir = sys.argv[2]
    print("output_director:", out_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    gifs = glob(f"{in_dir}/*.gif")
    for gif_path in tqdm(gifs, total=len(gifs)):
        mp4_path = gif_path.replace("gif", "mp4")
        os.system(f"ffmpeg -i {gif_path} -f mp4 {mp4_path}")
        os.system(f"mv {mp4_path} {out_dir}/")

