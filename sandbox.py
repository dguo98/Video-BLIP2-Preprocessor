import requests
import os
from tqdm import tqdm
import torch
import argparse
#from IPython import embed

if __name__ == "__main__":
    x = torch.Tensor([3]).cuda()  # HACK(demi): gpu utilization
    
    # input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", type=str, default="@spongebob")
    parser.add_argument("--save_dir", type=str, default="spongebob")
    parser.add_argument("--root_dir", type=str, default="/nlp/scr/demiguo/explore/giphy")
    parser.add_argument("--total", type=int, default=85000)
    parser.parse_args()

    
    api_key = '7xEbUQ1LlTFmHP9xZ5TTfvDWR662i4X8'
    
    # create directories
    if not os.path.exists(args.root_dir):
        os.makedirs(args.root_dir)
    download_dir = f"{args.root_dir}/{args.save_dir}"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # download by batches
    for offset in tqdm(range(0, args.total, 25), desc="download data"):
        limit = 25
        url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={args.search}&limit={limit}&offset={offset}'

        response = requests.get(url)
        json_data = response.json()

        for i, gif_data in enumerate(json_data['data']):
            gif_url = gif_data['images']['original']['url']
            gif_id = gif_data['id']
            
            # Fetch tags using the GIF by ID endpoint
            gif_by_id_url = f'https://api.giphy.com/v1/gifs/{gif_id}?api_key={api_key}'
            response = requests.get(gif_by_id_url)
            gif_json_data = response.json()
            
            title = gif_json_data['data'].get('title', [])
            response = requests.get(gif_url, stream=True)

            with open(f'{download_dir}/{gif_id}.gif', 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            with open(f'{download_dir}/{gif_id}.txt', 'w') as f:
                f.write(f"{title}\n")

