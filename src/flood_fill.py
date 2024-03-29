import collections

Pixel = collections.namedtuple("Pixel", ["row", "col"])


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        original_color = image[sr][sc]

        start_pixel = Pixel(sr, sc)
        cells_to_fill: list[Pixel] = [start_pixel]
        visited = {start_pixel}
        while cells_to_fill:
            current_pixel = cells_to_fill.pop()
            image[current_pixel.row][current_pixel.col] = color
            adjacent_pixel = [
                Pixel(current_pixel.row + 1, current_pixel.col),
                Pixel(current_pixel.row - 1, current_pixel.col),
                Pixel(current_pixel.row, current_pixel.col + 1),
                Pixel(current_pixel.row, current_pixel.col - 1),
            ]
            for pixel in adjacent_pixel:
                if (
                    0 <= pixel.row < m
                    and 0 <= pixel.col < n
                    and image[pixel.row][pixel.col] == original_color
                    and pixel not in visited
                ):
                    visited.add(pixel)
                    cells_to_fill.append(pixel)
        return image
