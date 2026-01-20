# FILE: game/poet.rpy
# ==========================================
# HỆ THỐNG NGÂM THƠ (CƠ CHẾ CALL/RETURN)
# ==========================================

# 1. BIẾN DỮ LIỆU
default tho_hien_tai_hv = ""
default tho_hien_tai_dich = ""

# 2. HÌNH ẢNH (Giữ nguyên)
image icon_giay_sang:
    Text("📜", size=50)
    alpha 0.8
    block:
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.5
        repeat

image bg_giay_tho = Solid("#f7e7ce", xysize=(700, 900))

# ---------------------------------------------------------
# LABEL CHÍNH (GỌI CÁI NÀY LÀ ĐƯỢC)
# ---------------------------------------------------------
label quy_trinh_ngam_tho(hv, dich):
    # 1. Nạp dữ liệu
    $ tho_hien_tai_hv = hv
    $ tho_hien_tai_dich = dich

    # 2. Ẩn giao diện game để tập trung
    window hide dissolve

    # 3. BƯỚC 1: HIỆN NÚT ICON VÀ CHỜ NGƯỜI CHƠI BẤM
    # Lệnh 'call screen' sẽ dừng game lại tại đây cho đến khi nút Return() được bấm
    call screen buoc_1_nut_kich_hoat 

    # 4. BƯỚC 2: HIỆN GIẤY TRẮNG VÀ CHỜ BẤM
    call screen buoc_2_giay_trang

    # 5. BƯỚC 3: HIỆN CHỮ VÀ CHỜ ĐỌC XONG
    call screen buoc_3_hien_chu(tho_hien_tai_hv)

    # 6. BƯỚC 4: HIỆN DỊCH NGHĨA (Trong khung chat)
    window show dissolve
    define tho_ke = Character(None, what_italic=True, what_color="#ffcc99")
    tho_ke "[tho_hien_tai_dich]"

    # 7. KẾT THÚC: QUAY VỀ NƠI ĐÃ GỌI NÓ
    return 

# ---------------------------------------------------------
# CÁC SCREEN HỖ TRỢ (Dùng action Return)
# ---------------------------------------------------------

# SCREEN BƯỚC 1: Nút icon góc màn hình
screen buoc_1_nut_kich_hoat():
    zorder 100
    # Nút bấm
    button:
        align (0.95, 0.05) 
        # Khi bấm, Return() sẽ kết thúc screen này và để code chạy xuống Bước 2
        action Return() 
        
        add "icon_giay_sang"

# SCREEN BƯỚC 2: Tờ giấy trắng
screen buoc_2_giay_trang():
    modal True
    zorder 101
    add Solid("#000000b3")
    add "bg_giay_tho" align (0.5, 0.5) at hien_ra_tu_tu
    text "{i}(Chạm vào giấy để thơ hiện lên){/i}" align(0.5, 0.95) color "#fff" size 25

    button:
        xfill True
        yfill True
        # Khi bấm, kết thúc screen này -> Chạy xuống Bước 3
        action Return()

# SCREEN BƯỚC 3: Hiện chữ
screen buoc_3_hien_chu(noi_dung):
    modal True
    zorder 101
    add Solid("#000000b3")
    add "bg_giay_tho" align (0.5, 0.5)

    frame:
        background None 
        align (0.5, 0.5)
        xmaximum 1000
        text noi_dung:
            font "fonts/DancingScript-VariableFont_wght.ttf"
            size 50 color "#5d4037" text_align 0.5 xalign 0.5 line_spacing 15 slow_cps 45 substitute False

    text "{i}(Chạm để xem dịch nghĩa){/i}" align(0.5, 0.95) color "#fff" size 25

    button:
        xfill True
        yfill True
        # Khi bấm, kết thúc screen này -> Chạy xuống Bước 4
        action Return()

transform hien_ra_tu_tu:
    zoom 0.8 alpha 0.0
    linear 0.5 zoom 1.0 alpha 1.0