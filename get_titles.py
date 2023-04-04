import os
import json
import sys
import numpy
from glob import glob
from tqdm import tqdm
from IPython import embed

if __name__ == "__main__":
    in_path = sys.argv[1]
    print("input directory:", in_path)
    out_path = sys.argv[2]
    print("output_director:", out_path)
    
    f = open(in_path)
    data = json.loads(f.read())
    
    for i in tqdm(range(len(data["data"]))):
        video_data = data["data"][i]
        
        video_path = video_data["video_path"]
        title_path = video_path.replace(".mp4", "_title.txt").replace("mp4","raw")
        title = open(title_path).readlines()
        title = "".join(title).replace("\n", "")
        
        prompt_data = [{"frame_index":0, "prompt": title}]
        video_data["data"] = prompt_data
        data["data"][i] = video_data

    
    json_object = json.dumps(data, indent=4)
    out = open(out_path, "w")
    out.write(json_object)
    out.close()



