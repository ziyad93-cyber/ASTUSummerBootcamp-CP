class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        for row in image:
            for j in range((n + 1) // 2):
                row[j], row[n - 1 - j] = row[n - 1 - j] ^ 1, row[j] ^ 1
        return image
