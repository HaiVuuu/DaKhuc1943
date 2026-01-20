# ==========================================
# PHẦN 1: KHAI BÁO (INIT)
# ==========================================

# 1.1. Khai báo Nhân vật
define m   = Character("[ten_mc]", color="#c8ffc8")   # Nhân vật chính
define tu  = Character("Bác Tư",     color="#a6a6a6") # Bác nông dân
define dan = Character("Dân làng",   color="#ffffff")
define boi = Character("Thầy Bói Ba", color="#ffb142")

# 1.2. Khai báo Biến số (Variables)
default ten_mc       = "Minh"     # Tên mặc định
default trust_score  = 0          # Điểm niềm tin
default inventory    = []         # Túi đồ
default da_noi_chuyen_voi_thay = False 
default da_dung_gao_nuoc        = False

# 1.3. Khai báo Hình ảnh (Backgrounds)

# Dùng luôn kích thước màn hình game (giả sử options.rpy đã set 1920x1080)
image bg_giay_tho  = im.Scale("images/to_giay.png", config.screen_width, config.screen_height)
image bg cong_lang = im.Scale("images/cong_lang.png", config.screen_width, config.screen_height)
image bg san_dinh  = im.Scale("images/dinh_lang.png", config.screen_width, config.screen_height)
image bg mieu_tho  = im.Scale("images/mieu_tho.png", config.screen_width, config.screen_height)
image bg authlanding = im.Scale("images/bg.png", config.screen_width, config.screen_height)

image bg mieu_tho_ben_ngoai = im.Scale("images/mieu_tho.png", config.screen_width, config.screen_height)
image bg mieu_tho_ben_trong = im.Scale("images/mieu_tho_ben_trong.png", config.screen_width, config.screen_height)


# --- Nhân vật (Sprites) ---

# Bác Tư Giận (Dùng khi tranh luận gay gắt)
image tu_gian_du:
    "images/chu_tu_gian_du.png"
    zoom 0.5
    align (0.5, 0.6)

# Bác Tư Buồn/Bối Rối
image tu_boi_roi:
    "images/chu_tu_that_vong.png"
    zoom 0.5
    align (0.5, 0.6)

# Bác Tư Vui/Quyết tâm
image tu_vui:
    "images/chu_tu_binh_tinh.png"
    zoom 0.5
    align (0.5, 0.6)

# Bác Tư đứng im ở sân đình (NPC)
image tu_dung_im:
    "images/chu_tu_gian_du.png"
    zoom 0.3
    yalign 1.0

# Hiệu ứng hover sáng lên
image tu_hover:
    "images/chu_tu_gian_du.png"
    zoom 0.5
    yalign 1.0
    matrixcolor BrightnessMatrix(0.2)

image tu_boi_roi_tranh_luan:
    "images/chu_tu_that_vong.png"
    zoom 0.5
    yalign 1.0

image tu_gian_du_tranh_luan:
    "images/chu_tu_gian_du.png"
    zoom 0.5
    yalign 1.0


# --- Vật phẩm (Icons) ---

image icon_trat_no:
    "images/trat_no.png"
    size (100, 100)

image icon_bai_vi:
    "images/bai_vi.png"
    size (100, 100)

image icon_chum_vai:
    "images/chumvai.png"
    size (200, 200)

image icon_gao_nuoc:
    "images/gao_nuoc.png"
    size (100, 100)

image icon_thuoc_phien:
    "images/Thuoc.png"
    size (100, 100)

image icon_tuyen_mo:
    "images/flyer.png"
    size (100, 100)


# --- Thầy bói ---

image boi_tung_kinh:
    "images/thay_cung.png"
    size (400, 600)

image boi_hover:
    "images/thay_cung.png"
    matrixcolor BrightnessMatrix(0.2)

image boi_gian:
    "images/thay_cung_gian_du.png"
    zoom 0.4
    xalign 0.5
    yalign 0.5

image boi_du_do:
    "images/thay_cung_du_do.png"
    zoom 0.4
    xalign 0.5
    yalign 0.5

image boi_so_hai:
    "images/thay_cung_so_hai.png"
    zoom 0.4
    xalign 0.5
    yalign 0.5


# ==========================================
# PHẦN 2: CỐT TRUYỆN CHÍNH (STORY)
# ==========================================

label start:
    # =========================
    # 1) MÀN HÌNH AUTH LANDING
    # =========================
    scene bg authlanding
    with fade

    show text "{size=80}{b}DẠ KHÚC 1943{/b}\n{size=55}NGỌN ĐUỐC LÀNG VỌNG{/size}" at Position(xalign=0.1, yalign=0.5)
    # Người chơi bấm chuột / Enter để qua
    pause

    hide text
    with dissolve

    # =========================
    # 2) RESET BIẾN & NHẬP TÊN
    # =========================
    $ inventory   = []
    $ trust_score = 0

    scene bg authlanding
    with fade

    show text "{size=80}{b}DẠ KHÚC 1943{/b}\n{size=55}NGỌN ĐUỐC LÀNG VỌNG{/size}" at Position(xalign=0.1, yalign=0.5)
    # Người chơi bấm chuột / Enter để qua

    # Nhập tên
    "Trước khi bắt đầu, hãy cho tôi biết tên của bạn."
    python:
        ten_mc = renpy.input("Tên của bạn là gì?", length=10).strip() or "Minh"

    # Màn 1
    scene bg authlanding
    with fade

    show text "{size=80}{b}Màn 1{/b}\n{size=55}CÁI BỤNG & CÁI ĐẦU{/size}" at Position(xalign=0.1, yalign=0.5)
    # Người chơi bấm chuột / Enter để qua
    pause

    hide text
    with dissolve

    # --- MỞ ĐẦU ---
    scene bg cong_lang with fade
    "Năm 1943... Làng Vọng chìm trong gió bấc lạnh buốt."
    m "Ba năm rồi mình mới về lại làng. Cảnh vật xơ xác quá..."
    m "Mọi người đi đâu hết rồi nhỉ? Sao chỉ thấy gió lạnh thổi qua cổng làng?"

    call quy_trinh_ngam_tho(
        "Cửu nguyệt thâm thu hề, tứ dã phi sương.\n Thiên cao thuỷ hạc hề, hàn nhạn bi thương.\n Tối khổ nhung biên hề, nhật dạ bàng hoàng.\n Phi kiên chấp nhuệ hề, cốt lật sa cương.",
        "Tiết thu tháng chín chừ bốn phía mờ sương.\n Trời cao nước khô chừ cái nhạn bi thương.\n Lính thú khổ thay chừ ngày đêm bàng hoàng.\n Mặc giáp cầm gươm chừ sương trắng gò hoang"
    )

    window hide dissolve
    # Chuyển sang Màn 1
    jump man_1

# ==========================================
# HIỆU ỨNG NHẬN VẬT PHẨM (ITEM GET)
# ==========================================

transform phong_to_giua_man_hinh:
    align (0.5, 0.5)
    zoom 0.0
    alpha 0.0
    easein_back 0.5 zoom 6.0 alpha 1.0 

screen thong_bao_nhat_do(hinh_anh_vat_pham, ten_vat_pham):
    modal True
    zorder 200
    
    add Solid("#000000b3")

    add hinh_anh_vat_pham:
        at phong_to_giua_man_hinh

    text "[ten_vat_pham]":
        align (0.5, 0.75)
        size 45
        color "#ffeb3b"
        outlines [(2, "#000", 0, 0)]

    text "(Chạm vào màn hình để tiếp tục)":
        align (0.5, 0.9)
        size 25
        color "#aaa"

    button:
        xfill True
        yfill True
        action Return()


# --- Screen: Sân Đình ---
screen phong_san_dinh():
    add "bg san_dinh"

    # 1. BÁC TƯ (Click để nói chuyện)
    imagebutton:
        idle "tu_gian_du"
        hover "tu_hover"
        align (0.5, 1.2)
        action Return()

    # 2. Vật phẩm: Bài vị (Chỉ hiện nếu chưa nhặt)
    if "bai_vi" not in inventory:
        imagebutton:
            idle "icon_bai_vi"
            xpos 400
            ypos 750
            action Jump("nhat_bai_vi")

    # 3. Nút đi ra cổng làng
    textbutton "<< ĐI RA CỔNG LÀNG":
        align (0.05, 0.25)
        text_size 30
        text_color "#ffffffff"
        action Jump("di_chuyen_cong_lang")

    text "Gợi ý: Click vào Bác Tư để nói chuyện.":
        align (0.5, 0.95)
        size 20
        color "#aaa"


# --- Screen: Cổng Làng ---
screen phong_cong_lang():
    add "bg cong_lang"

    if "trat_no" not in inventory:
        imagebutton:
            idle "icon_trat_no"
            xpos 1150
            ypos 800
            action Jump("nhat_trat_no")

    textbutton "VÀO SÂN ĐÌNH >>":
        align (0.95, 0.25)
        text_size 30
        text_color "#ffffffff"
        action Jump("di_chuyen_san_dinh")


# --- Screen: Thanh Niềm Tin ---
screen hien_thi_niem_tin():
    frame:
        align (0.5, 0.05)
        xsize 300

        hbox:
            spacing 20
            text "NIỀM TIN:":
                size 15
                color "#ff9f43"
            bar value AnimatedValue(trust_score, range=10.0):
                yalign 0.5
                xsize 150
            text "[trust_score]/10":
                size 15
                color "#fff"


# --- Screen: Phòng miếu thờ (bên trong) ---
screen phong_mieu_tho():
    add "bg mieu_tho_ben_trong"

    imagebutton:
        idle "boi_tung_kinh"
        hover "boi_hover"
        align (0.5, 0.6)
        action If(
            da_noi_chuyen_voi_thay == False,
            Jump("hoi_thoai_dau_tien"),
            If(
                len(inventory) > 0,
                Jump("tranh_luan_cuoi_cung"),
                Jump("ket_thuc_m2_bi_duoi")
            )
        )

    if da_noi_chuyen_voi_thay:

        if "gao_nuoc" not in inventory:
            imagebutton:
                idle "icon_chum_vai"
                xpos 1
                ypos 600
                action Jump("nhat_gao_nuoc")

        if "thuoc_phien" not in inventory:
            imagebutton:
                idle "icon_thuoc_phien"
                xpos 1250
                ypos 600
                action Jump("nhat_thuoc_phien")

    if not da_noi_chuyen_voi_thay:
        text "Gợi ý: Lại gần nói chuyện với Thầy Bói.":
            align (0.5, 0.95)
            size 20
            color "#aaa"
    else:
        text "Gợi ý: Thầy đã cảnh giác. Hãy lén tìm bằng chứng quanh đây.":
            align (0.5, 0.95)
            size 20
            color "#ff0"

# =========================
# HELPER: HIỆN TÊN MÀN
# =========================

label show_man_title(man_name, subtitle):
    scene bg_authlanding
    with fade

    $ full_text = "{size=70}{b}%s{/b}\n{size=40}%s{/size}" % (man_name, subtitle)

    show text full_text at truecenter
    pause 3.0
    hide text

    return