# skip BLIP
SEARCH="@spongebob"
SAVE="spongebob"
ROOT_DIR=/nlp/scr/demiguo/explore/giphy
SAVE_DIR=${ROOT_DIR}/${SAVE}
TOTAL=85000

# retrieve gif and txt
python retrieve.py --search ${SEARCH} --save_dir ${SAVE} --root_dir ${ROOT_DIR} --total ${TOTAL}

# convert to mp4
python convert_mp4.py ${SAVE_DIR}/raw ${SAVE_DIR}/mp4

# process blip
MP4_DIR=${SAVE_DIR}/mp4
python preprocess_hack.py --video_directory ${MP4_DIR} --config_name ${SAVE} --config_save_name ${SAVE}

cp train_data/${SAVE}.json ${SAVE_DIR}/

# clean json
OLD_JSON=${SAVE_DIR}/${SAVE}

echo ${OLD_JSON}
python clean_json.py ${OLD_JSON}.json ${OLD_JSON}_clean.json

# title/keywords
python get_keywords.py ${OLD_JSON}.json ${OLD_JSON}_keyword.json

python get_titles.py ${OLD_JSON}.json ${OLD_JSON}_title.json

# 
