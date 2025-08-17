
class Paster:
    def __init__(self, inim, outim):
        self.inim = inim
        self.outim = outim

    def paste(self, inbox, outcoords, outdims):
        self.outim.paste(
            self.inim.crop(inbox).resize(outdims),
            outcoords,
        )

    def row(self, count, inyy, indx, indy, outyy, outdx, outdy, gap=True):
        inxx = 0
        outxx = 0
        inyy2 = inyy + indy
        for ii in range(count):
            inbox = (inxx, inyy, inxx + indx, inyy2)
            self.paste(inbox, (outxx, outyy), (outdx, outdy))
            inxx += indx + (1 if gap else 0)
            outxx += outdx + (1 if gap else 0)

    def ui_corners(self, inyy, indy, indx1, indx2, outyy, outdy, outdx1, outdx2):
        self.paste(
            (0, inyy, indx1, inyy + indy),
            (0, outyy),
            (outdx1, outdy),
        )
        self.paste(
            (indx1 + 1, inyy, indx1 + 2, inyy + indy),
            (outdx1 + 1, outyy),
            (1, outdy),
        )
        self.paste(
            (indx1 + 3, inyy, indx1 + 3 + indx2, inyy + indy),
            (outdx1 + 3, outyy),
            (outdx2, outdy),
        )
