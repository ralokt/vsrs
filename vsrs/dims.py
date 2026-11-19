class VsScaleDimsCalculator:
    def __init__(self, square_size):
        self.square_size = square_size

    def _scale(self, dim):
        prod = dim * self.square_size
        scaled = prod // 16
        if prod % 16 >= 8:
            scaled += 1
        return scaled

    def rd_h(self):
        return self._scale(21)

    def rd_w(self):
        return self._scale(11)

    def sml_d(self):
        return self._scale(26)

    def uil_w(self):
        return self._scale(12)

    def uir_w(self):
        return self._scale(12)

    def uit_h(self):
        return self._scale(11)

    def uim_h(self):
        return self._scale(11)

    def uib_h(self):
        return self._scale(12)

    def cr_p(self):
        return self._scale(2)

    def cr_h(self):
        return 2 * self.cr_p() + self.rd_h()

    def cr_w(self):
        return 4 * self.cr_p() + 3 * self.rd_w()

    def rds_h(self):
        return self._scale(14)

    def rds_w(self):
        return self._scale(7)

    def vcrre_w(self):
        return self.cr_w() + self.cr_p() + self.rds_w()


class VsSkinOffsetCalculator(VsScaleDimsCalculator):
    def sq2_y(self):
        return self.square_size

    def rd_y(self):
        return self.sq2_y() + self.square_size + 1

    def sml_y(self):
        return self.rd_y() + self.rd_h() + 1

    def uil_x(self):
        return 0

    def uir_x(self):
        return self.uil_w() + 3

    def uit_y(self):
        return self.sml_y() + self.sml_d() + 1

    def uim_y(self):
        return self.uit_y() + self.uit_h() + 3

    def uib_y(self):
        return self.uim_y() + self.uim_h() + 3

    def skin_h(self):
        return self.uib_y() + self.uib_h()

    def cr_x(self):
        return self.uir_x() + self.uir_w() + 1

    def cr_y(self):
        return self.uit_y()

    def vcrre_x(self):
        return self.cr_x() + self.cr_w() + 3

    def vcrrt_x(self):
        return self.vcrre_x() + 3 * self.rd_w() + 3 * self.cr_p()

    def vcrrt_y(self):
        return self.cr_y() + self.cr_p() + self.rd_h() - self.rds_h()

    def cn_y(self):
        return self.skin_h() + 1

    def rds_y(self):
        return self.cn_y() + self.square_size + 1

    def vsmle_y(self):
        return self.rds_y() + self.rds_h() + 1

    def vsext_h(self):
        return self.vsmle_y() + self.sml_d()
