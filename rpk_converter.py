import json
import logging
import os
import shutil
import time
import zipfile

import pandas as pd

from anki_collection_writer import AnkiCollectionWriter

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class RpkConverter:
    def __init__(self,
                 file_path: str,
                 out_dir: str,
                 sqlite_path: str
                 ):
        self.rpk_file_path = file_path
        self.sqlite_path = sqlite_path
        self.filename = os.path.splitext(os.path.split(self.rpk_file_path)[1])[0]

        self.out_dir = out_dir
        # temp files directory labeled for concurrent
        local_time = time.strftime("%S%M%H%d%m%y", time.localtime())
        self.tmp_dir = f"{out_dir}/temp{local_time}"
        self.rpk_tmp_dir = f"{self.tmp_dir}/rpk"
        self.apkg_tmp_dir = f"{self.tmp_dir}/apkg"
        os.mkdir(self.tmp_dir)
        os.mkdir(self.rpk_tmp_dir)
        os.mkdir(self.apkg_tmp_dir)

        self.media_files_path = f"{self.rpk_tmp_dir}/resources"

        self.cards_df = None
        self.carts_df = None
        self.tpls_df = None

    def read_rpk(self):
        assert os.path.exists(self.rpk_file_path), f"File not exists: {self.rpk_file_path}"
        assert zipfile.is_zipfile(self.rpk_file_path), f"Not valid rpk file: {self.rpk_file_path}"
        logging.info("Reading from rpk file")
        zipf = zipfile.ZipFile(self.rpk_file_path, "r", zipfile.ZIP_DEFLATED)
        zipf.extractall(self.rpk_tmp_dir)
        zipf.close()

    def load_rpk_json(self):
        logging.info("Loading rpk json")
        with open(f"{self.rpk_tmp_dir}/data/cards.json") as f:
            obj = json.load(f)

        self.cards_df = pd.DataFrame(obj)
        self.cards_df.set_index("cid", inplace=True)

        # df[df['cid'] == df.iloc[0]['related_cid']]

        with open(f"{self.rpk_tmp_dir}/data/cats.json") as f:
            obj = json.load(f)

        self.carts_df = pd.DataFrame(obj)
        self.carts_df.set_index("aid", inplace=True)

        with open(f"{self.rpk_tmp_dir}/data/tpls.json") as f:
            obj = json.load(f)

        self.tpls_df = pd.DataFrame(obj)
        self.tpls_df.set_index("tid", inplace=True)

    def write_to_sqlite(self):
        logging.info("Writing to sqlite3")
        cw = AnkiCollectionWriter(self.filename, self.sqlite_path,
                                  cats_df=self.carts_df, cards_df=self.cards_df, tpls_df=self.tpls_df)
        cw.clear_old_rows()

        cw.insert_col_table()
        cw.insert_notes_table()

    def convert_media_files(self):
        logging.info("Converting media files")
        media_list = os.listdir(self.media_files_path)
        media_dict = {}
        for i in range(len(media_list)):
            filename = media_list[i]
            os.rename(f"{self.media_files_path}/{filename}", f"{self.media_files_path}/{i}")
            media_dict[f"{i}"] = filename
        json.dump(media_dict, open(f"{self.apkg_tmp_dir}/media", "w"))

    def pack_apkg(self):
        logging.info("Packing into apkg file")
        zipf = zipfile.ZipFile(f"{self.out_dir}/{self.filename}.apkg", 'w', zipfile.ZIP_DEFLATED)
        zipf.write(f"{self.apkg_tmp_dir}/media", "media")
        zipf.write(self.sqlite_path, "collection.anki2")
        for media_file in os.listdir(self.media_files_path):
            zipf.write(f"{self.media_files_path}/{media_file}", media_file)
        zipf.close()
        done_message = f"The conversion is done. The output file is saved in {self.out_dir}/{self.filename}.apkg."
        logging.info(done_message)
        print(done_message)

    def clear_tmp_files(self):
        logging.info("Deleting temp files")
        error_message = "Delete temp files failed. Please delete them manually."
        try:
            shutil.rmtree(self.tmp_dir)
        except:
            logging.error(error_message)
            print(error_message)
