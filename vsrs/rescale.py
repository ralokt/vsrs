from PIL import Image
from .dims import VsSkinOffsetCalculator
from .paster import Paster


def rescale(inim, outpx, bgc):
    inpx = inim.width // 9
    incalc = VsSkinOffsetCalculator(inpx)
    outcalc = VsSkinOffsetCalculator(outpx)
    outim = Image.new(
        "RGB",
        (outpx * 9, outcalc.skin_h()),
        bgc,
    )
    paster = Paster(inim, outim)

    # squares
    paster.row(9, 0, inpx, inpx, 0, outpx, outpx, ingap=0, outgap=0)
    paster.row(8, inpx, inpx, inpx, outpx, outpx, outpx, ingap=0, outgap=0)

    # timer numbers
    paster.row(
        11,
        incalc.rd_y(),
        incalc.rd_w(),
        incalc.rd_h(),
        outcalc.rd_y(),
        outcalc.rd_w(),
        outcalc.rd_h(),
    )

    # smiley states
    paster.row(
        5,
        incalc.sml_y(),
        incalc.sml_d(),
        incalc.sml_d(),
        outcalc.sml_y(),
        outcalc.sml_d(),
        outcalc.sml_d(),
    )

    # ui edges/corners
    paster.ui_corners(
        incalc.uit_y(),
        incalc.uit_h(),
        incalc.uil_w(),
        incalc.uir_w(),
        outcalc.uit_y(),
        outcalc.uit_h(),
        outcalc.uil_w(),
        outcalc.uir_w(),
    )
    paster.ui_corners(
        incalc.uit_y() + incalc.uit_h() + 1,
        1,
        incalc.uil_w(),
        incalc.uir_w(),
        outcalc.uit_y() + outcalc.uit_h() + 1,
        1,
        outcalc.uil_w(),
        outcalc.uir_w(),
        middle=False,
    )
    paster.ui_corners(
        incalc.uim_y(),
        incalc.uim_h(),
        incalc.uil_w(),
        incalc.uir_w(),
        outcalc.uim_y(),
        outcalc.uim_h(),
        outcalc.uil_w(),
        outcalc.uir_w(),
    )
    paster.ui_corners(
        incalc.uim_y() + incalc.uim_h() + 1,
        1,
        incalc.uil_w(),
        incalc.uir_w(),
        outcalc.uim_y() + outcalc.uim_h() + 1,
        1,
        outcalc.uil_w(),
        outcalc.uir_w(),
        middle=False,
    )
    paster.ui_corners(
        incalc.uib_y(),
        incalc.uib_h(),
        incalc.uil_w(),
        incalc.uir_w(),
        outcalc.uib_y(),
        outcalc.uib_h(),
        outcalc.uil_w(),
        outcalc.uir_w(),
    )

    # timer
    xx = incalc.cr_x()
    yy = incalc.cr_y()
    inbox = (xx, yy, xx + incalc.cr_w(), yy + incalc.cr_h())
    outcoords = (outcalc.cr_x(), outcalc.cr_y())
    outdims = (outcalc.cr_w(), outcalc.cr_h())
    paster.paste(inbox, outcoords, outdims)
    paster.row(
        3,
        incalc.cr_y() + incalc.cr_p(),
        incalc.rd_w(),
        incalc.rd_h(),
        outcalc.cr_y() + outcalc.cr_p(),
        outcalc.rd_w(),
        outcalc.rd_h(),
        inxx=incalc.cr_x() + incalc.cr_p(),
        outxx=outcalc.cr_x() + outcalc.cr_p(),
        ingap=incalc.cr_p(),
        outgap=outcalc.cr_p(),
    )

    # bg pixel
    xx = incalc.cr_x() + incalc.cr_w() + 1
    yy = incalc.cr_y()
    inbox = (xx, yy, xx + 1, yy + 1)
    outcoords = (outcalc.cr_x() + outcalc.cr_w() + 1, outcalc.cr_y())
    outdims = (1, 1)
    paster.paste(inbox, outcoords, outdims)

    return outim
