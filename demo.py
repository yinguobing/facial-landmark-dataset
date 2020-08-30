import cv2
from tqdm import tqdm

from fmd.wflw import WFLW
from fmd.mark_dataset.util import draw_marks

DATASET_DIR = "/home/robin/data/facial-marks/wflw/WFLW_images"

if __name__ == "__main__":
    # Construct a dataset.
    ds = WFLW(is_train=True, name="wflw_train")

    # Populate the dataset with essential data, and see what we have got.
    ds.populate_dataset(DATASET_DIR)
    print(ds)

    # Randomly pick a sample and show the result.
    random_sample = ds.pick_one()
    lucky_image = random_sample.read_image()
    draw_marks(lucky_image, random_sample.marks)
    cv2.imshow("Preview", lucky_image)
    cv2.waitKey()

    # Loop through the dataset and show all the samples.
    for sample in tqdm(ds):
        image = sample.read_image()
        draw_marks(image, sample.marks)
        draw_marks(image, sample.get_key_marks(), color=(255, 0, 0))
        cv2.imshow("Preview", image)
        if cv2.waitKey(500) == 27:
            break
