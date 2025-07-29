from dip import *

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        
        label_img = image.copy()
        height, width = image.shape
        label = 1
        regions = {}
        visited = set()

        for i in range(height):
            for j in range(width):
                
                if label_img[i][j] == 255 and (i, j) not in visited:
                    queue = [(i, j)]
                    regions[label] = []

                    while queue:
                        x, y = queue.pop(0)
                        if (x, y) in visited:
                            continue

                        visited.add((x, y))
                        label_img[x][y] = 128  
                        regions[label].append((x, y))

                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                nx, ny = x + dx, y + dy
                                if (
                                    0 <= nx < height and
                                    0 <= ny < width and
                                    label_img[nx][ny] == 255 and
                                    (nx, ny) not in visited
                                ):
                                    queue.append((nx, ny))

                    label += 1

        return regions

    def compute_statistics(self, region):
        stats = {}
        for region_id, pixels in region.items():
            area = len(pixels)
            x_sum = sum(p[1] for p in pixels)
            y_sum = sum(p[0] for p in pixels)
            cx = int(x_sum / area)
            cy = int(y_sum / area)
            stats[region_id] = {"center": (cx, cy), "area": area}
            print(f"{region_id}: ({cx}, {cy}), {area}")
        return stats

    def mark_image_regions(self, image, stats):
        
        color_img = zeros((image.shape[0], image.shape[1], 3), dtype=uint8)

       
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                val = image[i][j]
                color_img[i][j] = [val, val, val]  

        for region_id, data in stats.items():
            x, y = data["center"]
            area = data["area"]

            
            putText(color_img, "*", (x, y), FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

            
            putText(color_img, f"{region_id}", (x + 3, y - 5), FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 1)

            
            putText(color_img, f"{area}", (x + 3, y + 10), FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 1)

        return color_img



