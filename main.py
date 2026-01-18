import cv2 as cv
import matplotlib.pyplot as plt


def display_images(original, blurred, msg_left, msg_right):
    fig, axes = plt.subplots(1, 2, figsize=(13, 6))

    axes[0].imshow(original)
    axes[0].set_title(msg_left)
    axes[0].axis('off')

    axes[1].imshow(blurred)
    axes[1].set_title(msg_right)
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

def save_blurred_img(name, img):
    img_bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imwrite(name, img_bgr)

if __name__ == "__main__":
    layers = 2
    kernel_size=(5, 5)
    sigma = 0
    image_path = "Bricks085_512-PNG_Color.png"

    image = cv.imread(image_path)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    assert image is not None, "file could not be read, check with os.path.exists()"

    gaussian_array = []
    laplacian = image_rgb.copy()
    # generate Gaussian pyramid for image
    for i in range(layers):
        #blurred = cv.GaussianBlur(lap, kernel_size, sigma)
        blurred = cv.pyrDown(laplacian)
        gaussian_array.append(blurred)
        #lap = lap - blurred
        upscaled_gaussian = cv.pyrUp(blurred)
        laplacian = laplacian - upscaled_gaussian
        display_images(laplacian, upscaled_gaussian, msg_left="Laplacian", msg_right='Gaussian')
        save_blurred_img(f"blurred_{i}.png", blurred)

    save_blurred_img(f"laplacian.png", laplacian)

    # now reconstruct
    for i in range(layers-1, -1, -1):
        upscaled_gaussian = cv.pyrUp(gaussian_array[i])
        laplacian = laplacian + upscaled_gaussian
        #lap = lap + gp[i]
        display_images(laplacian, image_rgb, msg_left="Restored", msg_right='Origin')

