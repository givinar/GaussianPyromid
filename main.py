import cv2 as cv
import numpy as np
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


def calculate_image_stats_detailed(image):
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Not RGB image")

    height, width, channels = image.shape

    results = {}
    channel_names = ['R', 'G', 'B']

    for i, name in enumerate(channel_names):
        channel = image[:, :, i]

        mean_val = np.mean(channel)
        variance_val = np.var(channel)
        std_val = np.std(channel)
        min_val = np.min(channel)
        max_val = np.max(channel)

        results[name] = {
            'mean': mean_val,
            'variance': variance_val,
            'std': std_val,
            'min': min_val,
            'max': max_val,
            'range': max_val - min_val
        }

    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    overall_mean = np.mean(gray_image)
    overall_variance = np.var(gray_image)

    return {
        'channels': results,
        'overall': {
            'mean': overall_mean,
            'variance': overall_variance,
            'size': f"{width}x{height}",
            'pixels': width * height
        }
    }

def print_stats(stats, msg):
    print("=" * 60)
    print(msg)
    for channel, values in stats['channels'].items():
        print(f"{channel} channels:")
        print(f"  Mean: {values['mean']:.2f}")
        print(f"  Variance: {values['variance']:.2f}")
        print(f"  std: {values['std']:.2f}")
        print(f"  Range: {values['min']} - {values['max']}\n")

    print(f"\nCommon stats (in grayscale):")
    print(f"  Mean: {stats['overall']['mean']:.2f}")
    print(f"  Variance: {stats['overall']['variance']:.2f}")
    print("="*60)


def plot_rgb_histograms(image, bins=256, range=(0, 256)):
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Not RGB image")

    r_channel = image[:, :, 0]
    g_channel = image[:, :, 1]
    b_channel = image[:, :, 2]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].imshow(image if len(image.shape) == 3 else image, cmap='gray')
    axes[0, 0].set_title("Current image")
    axes[0, 0].axis('off')

    axes[0, 1].hist(r_channel.ravel(), bins=bins, range=range,
                    color='red', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title("R channel (Red)")
    axes[0, 1].set_xlabel("Value of pixel")
    axes[0, 1].set_ylabel("Frequency")
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].hist(g_channel.ravel(), bins=bins, range=range,
                    color='green', alpha=0.7, edgecolor='black')
    axes[1, 0].set_title("G channel (Green)")
    axes[1, 0].set_xlabel("Value of pixel")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].hist(b_channel.ravel(), bins=bins, range=range,
                    color='blue', alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('B channel (Blue)')
    axes[1, 1].set_xlabel("Value of pixel")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    r_hist = np.histogram(r_channel, bins=bins, range=range)
    g_hist = np.histogram(g_channel, bins=bins, range=range)
    b_hist = np.histogram(b_channel, bins=bins, range=range)

    return r_hist, g_hist, b_hist

if __name__ == "__main__":
    layers = 1
    kernel_size=(5, 5)
    sigma = 0
    image_path = "Bricks085_512-PNG_Color.png"

    image = cv.imread(image_path)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    assert image is not None, "file could not be read, check with os.path.exists()"

    stats = calculate_image_stats_detailed(image_rgb)
    print_stats(stats, "Original image:")
    plot_rgb_histograms(image_rgb)

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
        #display_images(laplacian, upscaled_gaussian, msg_left="Laplacian", msg_right='Gaussian')
        save_blurred_img(f"blurred_{i}.png", blurred)

        stats = calculate_image_stats_detailed(blurred)
        print_stats(stats, f"Blurred image {i}:")
        plot_rgb_histograms(blurred)

    save_blurred_img(f"laplacian.png", laplacian)
    stats = calculate_image_stats_detailed(laplacian)
    print_stats(stats, "Laplacian:")
    plot_rgb_histograms(laplacian)

    # now reconstruct
    for i in range(layers-1, -1, -1):
        upscaled_gaussian = cv.pyrUp(gaussian_array[i])
        laplacian = laplacian + upscaled_gaussian
        #lap = lap + gp[i]
        display_images(laplacian, image_rgb, msg_left="Restored", msg_right='Origin')

