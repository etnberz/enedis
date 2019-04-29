# @Author: Maxime Caïtucoli <mcaitucoli>
# @Date:   2019-04-29T20:02:41+08:00
# @Last modified by:   mcaitucoli
# @Last modified time: 2019-04-29T20:37:18+08:00

from os.path import join, dirname, basename

PROJECT_DIR = dirname(__file__).replace("notebooks/utils", "")

# RAW DATA

TRAIN_INPUT_RAW = join(PROJECT_DIR, "data/raw/training_input_vQrEBcg.csv")
TRAIN_OUTPUT_RAW = join(PROJECT_DIR, "data/raw/training_output_nprXCZM.csv")
TEST_INPUT_RAW = join(PROJECT_DIR, "data/raw/testing_input_jqUOUMs.csv")

# CLEAN DATA

TRAIN_CLEAN = join(PROJECT_DIR, "data/clean/train_clean.csv")
TEST_CLEAN = join(PROJECT_DIR, "data/clean/train_clean.csv")
