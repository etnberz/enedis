# @Author: Maxime Caïtucoli <mcaitucoli>
# @Date:   2019-04-29T20:02:41+08:00
# @Last modified by:   mcaitucoli
# @Last modified time: 2019-04-29T21:01:29+08:00

from os.path import join, dirname, basename

PROJECT_DIR = dirname(__file__).replace("notebooks/utils", "")

# RAW DATA

TRAIN_INPUT_RAW = join(PROJECT_DIR, "data/raw/training_input_vQrEBcg.csv")
TRAIN_OUTPUT_RAW = join(PROJECT_DIR, "data/raw/training_output_nprXCZM.csv")
TEST_INPUT_RAW = join(PROJECT_DIR, "data/raw/testing_input_jqUOUMs.csv")

# CLEAN DATA

TRAIN_MERGED = join(PROJECT_DIR, "data/merged/train_merged.csv")
TEST_MERGED = join(PROJECT_DIR, "data/merged/test_merged.csv")
