from PIL import Image

class CodeBlock:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[None] * self.cols for r in range(self.rows)]
        
    def loadData(self, aList, folding = "ltor"):
        n_symbols = self.cols * self.rows
        assert(len(aList) >= n_symbols)
        
        if folding == "ltor":
            for i in range(n_symbols):
                r,c = i // self.cols, i % self.cols
                self.data[r][c] = aList[i]
        else:
            raise(NotImplementedError())
        return self
    
    def _buildImage(self):
        allWidths, allHeights = zip(*[i.size for row in self.data for i in row])
        cellWidth = min(allWidths)   # may overlap a pixel but looks better than 'max'
        cellHeight = min(allHeights) # same
        size = (self.cols * cellWidth, self.rows * cellHeight)
        print(size)
        im_collage = Image.new("RGB", size)
        for r,row in enumerate(self.data):
            for c,im in enumerate(row):
                im_collage.paste(im, (c * cellWidth, r * cellHeight))
        from io import BytesIO
        b = BytesIO()
        im_collage.save(b, "JPEG")
        return b.getvalue()
    
    def __repr__(self):
        if all([isinstance(o, str) and len(o) == 1 for row in self.data for o in row]):
            result = "\n".join([" ".join(row) for row in self.data])
            return result
        else:
            return self.data.__repr__()
        
    def _repr_jpeg_(self):
        if all([isinstance(o, Image.Image) for row in self.data for o in row]):      
            return self._buildImage()
        else:
            return None
        
################################################################################
#        
# testparams = {"text":alphabet, "width":20, "height":6}
# 
# class CodeBlock(list):
#     def __repr__(self):
#         return "\n".join(self)
# 
# def makeblock(text, width, height):
#     block = []
#     assert(width * height <= len(text))
#     for r in range(height):
#         start = r * width
#         stop = start + width
#         block.append(text[start:stop])
#     return CodeBlock(block)
# 
# makeblock(**testparams)
# 
# def makereverse(text, width, height):
#     return CodeBlock([line[::-1] for line in makeblock(text, width, height)])
# 
# makereverse(**testparams)
# 
# def makezigzag(text, width, height):
#     block = []
#     for r, line in enumerate(makeblock(text, width, height)):
#         block.append(line if (r%2 == 0) else line[::-1])
#     return CodeBlock(block)
# 
# makezigzag(**testparams)
# 
# def makespiral(text, width, height):
#     assert(width * height <= len(text))
#     block = [[" "] * width for i in range(height)]
#     nhoriz,nvert = width, height
#     iterText = iter(text)
#     direction = 0 # 0,1,2,3 = right, down, left, up
#     c,r = -1,0    # start one step outside of the block
#     while nhoriz > 0 and nvert > 0:
#         if direction == 0:
#             for n in range(nhoriz):
#                 c += 1
#                 block[r][c] = iterText.__next__()
#             nvert -= 1
#         elif direction == 1:
#             for n in range(nvert):
#                 r += 1
#                 block[r][c] = iterText.__next__()
#             nhoriz -= 1
#         elif direction == 2:
#             for n in range(nhoriz):
#                 c -= 1
#                 block[r][c] = iterText.__next__()
#             nvert -= 1
#         else:
#             for n in range(nvert):
#                 r -= 1
#                 block[r][c] = iterText.__next__()
#             nhoriz -= 1
#         direction = (direction + 1) % 4
#     block = ["".join(row) for row in block]
#     return CodeBlock(block)
# 
# makespiral(**testparams)