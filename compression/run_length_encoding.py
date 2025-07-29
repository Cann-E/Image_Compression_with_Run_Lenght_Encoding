from dip import *

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        hei, wid = binary_image.shape
        flat = []
        for i in range(hei):
            for j in range(wid):
                flat.append(binary_image[i][j])

        rle_code = []
        prev = flat[0]
        count = 1
        for k in range(1, len(flat)):
            if flat[k] == prev:
                count += 1
            else:
                rle_code.append((prev, count))
                prev = flat[k]
                count = 1
        rle_code.append((prev, count))

        return rle_code

    def decode_image(self, rle_code, height , width):
        """
        Reconstruct the original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """

        flat = []
        for val, count in rle_code:
            flat.extend([val]*count)
        image = zeros((height, width), uint8)
        for i in range(height):
            for j in range(width):
                image[i][j] = flat[i * width + j]

        return image
