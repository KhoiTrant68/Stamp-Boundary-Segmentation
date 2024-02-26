import os
import cv2
import numpy as np
from glob import glob
from ellipse import draw_ellipses_custom


def display_image(image_path, num_images):
    for image_path in glob(f"{image_path}/*.jpg")[:num_images]:
        img = cv2.imread(image_path)
        name = image_path.split("/")[-1]
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    images_path = "data/stamp"
    save_path = "results"
    mask_path = "mask"
    display = True
    num_images_display = 3

    files = os.listdir(images_path)

    os.makedirs(save_path, exist_ok=True)
    os.makedirs(mask_path, exist_ok=True)

    images_save_path = os.path.join(save_path, images_path.split("/")[-1])
    os.makedirs(images_save_path, exist_ok=True)

    masks_save_path = os.path.join(mask_path, images_path.split("/")[-1])
    os.makedirs(masks_save_path, exist_ok=True)
    
    for file in files:
        ori_image = cv2.imread(os.path.join(images_path, file))
        mask = np.zeros(ori_image.shape[:2], np.uint8)

        ellipse = draw_ellipses_custom(ori_image)
        result = cv2.ellipse(ori_image, ellipse, (0, 255, 255), 1)
        mask_ellipse = cv2.ellipse(mask, ellipse, (255, 255, 255))
        

        cv2.imwrite(os.path.join(images_save_path, file), result)
        cv2.imwrite(os.path.join(masks_save_path, file), mask_ellipse)



    if display:
        display_image(images_save_path, num_images_display)
        display_image(masks_save_path, num_images_display)


if __name__ == "__main__":
    main()
