import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_image(image_path, n_clusters=5):
    """
    Performs K-means clustering for image segmentation.

    Args:
        image_path: Path to the input image.
        n_clusters: The desired number of segments (clusters).

    Returns:
        The segmented image as a NumPy array, or None if an error occurs.
    """
    try:
        # Load the image using OpenCV
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not load image from {image_path}")
            return None

        # Convert the image to RGB color space
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Reshape the image to a 2D array of pixels
        pixels = img.reshape((-1, 3))

        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)  # random_state for reproducibility
        kmeans.fit(pixels)

        # Get the cluster centers (colors)
        centers = np.uint8(kmeans.cluster_centers_)

        # Assign each pixel to its closest cluster center
        segmented_image = centers[kmeans.labels_].reshape(img.shape)

        return segmented_image

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
image_path = image_path = '/Users/animesh/dip_hci/K-Means Clustering/img.webp' #This line is still needed to specify the image file name.
segmented_img = segment_image(image_path, n_clusters=8) #Try different numbers of clusters

if segmented_img is not None:
    plt.imshow(segmented_img)
    plt.title('Segmented Image')
    plt.show()
    cv2.imwrite('/Users/animesh/dip_hci/K-Means Clustering/segmented_image.jpg', cv2.cvtColor(segmented_img, cv2.COLOR_RGB2BGR))
