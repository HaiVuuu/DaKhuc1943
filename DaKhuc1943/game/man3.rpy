# =========================
# KHAI BÁO NHÂN VẬT & HÌNH
# =========================

define m = Character("Minh", color="#66ccff")
define l = Character("Cậu Long", color="#ff6666")

image bg_man_3       = im.Scale("images/10.png", config.screen_width, config.screen_height)
image bg_authlanding = im.Scale("images/bg.png", config.screen_width, config.screen_height)
image tuyen_mo       = "images/flyer.png"
image cau_long       = "images/long.png"

default flyer = False

# =========================
# MÀN 3: ÁNH SÁNG VÀ BÓNG TỐI
# =========================

label man_3:
    scene bg_authlanding
    with fade

    show text "{size=80}{b}Màn 3{/b}\n{size=55}ÁNH SÁNG VÀ BÓNG TỐI{/size}" at Position(xalign=0.1, yalign=0.5)
    pause
    hide text

    jump man3_story


label man3_story:
    scene bg_man_3
    with dissolve

    "Đêm hội làng rực rỡ đèn màu, tiếng nhạc Tây chát chúa xé toạc bầu không khí tĩnh mịch."
    "Rượu tây, thuốc lá, tiếng cười nói xô bồ trộn lẫn với những điệu nhảy lố lăng giữa sân đình."
    "Những mái nhà tranh tối om im lìm ở đằng xa càng làm đám đông giữa ánh đèn thêm khập khiễng, chới với."

    m "Không khí này... không phải chỉ là vui chơi nữa."
    m "Có cái gì đó rất sai đang diễn ra ở đây."
    m "Mình phải tìm cho ra gốc rễ của cái gọi là 'văn minh' này."

    jump man3_search


# =================
# BƯỚC 1: TÌM MANH MỐI
# =================

label man3_search:

    with dissolve

    "Giữa nền đất đầy rác rượu và giấy gói kẹo, một tờ rơi trắng tinh nổi bật lên khác thường."
    "Gió thổi lật nó lên, để lộ những dòng chữ in đậm, hoa mỹ nhưng lạnh lẽo."

    "Bạn có muốn nhặt tờ rơi không?"

    menu:
        "Nhặt tờ rơi":
            m "Trong đêm hỗn loạn thế này, thứ sạch sẽ quá thường là thứ bẩn nhất."
            m "Để xem trên đó viết gì."
            jump man3_flyer

        "Bỏ qua":
            "Bước đi thêm vài bước, cố phớt lờ tờ giấy nhỏ ấy."
            "Nhưng cảm giác bất an cứ nhói lên như có ai níu áo."
            "Cuối cùng, cậu khựng lại, quay đầu nhìn, rồi quay lại nhặt tờ rơi lên."
            jump man3_flyer


label man3_flyer:

    # Đánh dấu đã nhặt tờ rơi (dùng sau này ở boss)
    $ flyer = True

    scene bg_man_3
    with fade

    # HIỆN ẢNH TỜ RƠI Ở GIỮA MÀN HÌNH
    show tuyen_mo at truecenter
    with dissolve

    "Cần lao vi tiên thủ...\nVô vi thực... 'tân thời'."
    "Những dòng chữ uốn éo, khoác áo 'khai hoá', nhưng giữa hàng chữ là những chỗ nhỏ li ti, in nghiêng mờ: 'làm việc xa quê', 'ký khế ước dài hạn', 'phục vụ chủ Tây'..."

    pause

    hide tuyen_mo
    with fade

    m "Ra là vậy..."
    m "Tuyển phu đi làm 'văn minh' chỉ là cái cớ. Thật ra là bán người, xích chân dân làng vào kiếp nô lệ mới."
    m "Nếu đây là tấm vé đi vào 'ánh sáng' mà bọn chúng rao giảng, thì phía sau chắc chắn là một vực sâu tăm tối."

    jump man3_boss


# =================
# BƯỚC 2: BOSS FIGHT - TRANH LUẬN
# =================

label man3_boss:

    show cau_long at center:
        zoom 1.5
    with dissolve

    l "Nhìn lũ nhà quê các người kìa!"
    l "Ăn mặc quê mùa, nói năng cổ hủ, suốt ngày lo ruộng với khoai."
    l "Phải sống như Tây, vào vũ hội, uống rượu, nghe nhạc mới gọi là người của thời đại chứ!"
    l "Đời có bao nhiêu đâu mà cứ ôm mãi cái đình, cái miếu, cái 'truyền thống' rách nát!"

    m "Nếu chỉ biết say sưa bắt chước người ta mà không hiểu mình là ai..."
    m "Thì đó không phải là văn minh, mà là tự tay chặt đứt rễ của chính mình."

    jump man3_card1


# -------- Thẻ 1 --------

label man3_card1:

    l "Văn hoá truyền thống chỉ là rác rưởi cổ hủ!"
    l "Xoá đi hết đi, quên đi hết đi, sống như Tây cho sướng!"

    m "Phải chọn thẻ bài phản bác."

    menu:
        "[[DÂN TỘC]]":
            jump man3_win1
        "Im lặng":
            jump bad_ending


label man3_win1:

    m "Sai rồi!"
    m "Một dân tộc mất gốc là một dân tộc đã nửa bước ra mồ."
    m "Anh đang chối bỏ tổ tiên, lịch sử, chối bỏ chính những người đã đổ máu để giữ mảnh đất này."
    m "Để làm gì? Để được khen là 'giống Tây' hơn một chút à?"

    l "..."
    l "Ngươi to gan thật."

    jump man3_card2


# -------- Thẻ 2 --------

label man3_card2:

    l "Ta đang mang văn minh và việc làm cho dân nghèo!"
    l "Nhờ ta mà họ được 'xuất ngoại', được ăn ngon, mặc đẹp, thoát khỏi cái làng tù túng này!"

    m "Phải vạch trần bộ mặt thật của hắn."

    menu:
        "[[TỜ RƠI TUYỂN MỘ]]":
            jump man3_win2
        "Cãi bằng cảm xúc":
            jump bad_ending


label man3_win2:

    if flyer:
        m "Văn minh mà anh nói… là cái này sao?"
        m "Những dòng chữ bé tẹo in ở cuối tờ rơi: 'ký khế ước dài hạn', 'phục dịch chủ Tây', 'xa quê không kỳ hạn'..."
        m "Đó không phải là 'việc làm', mà là xiềng xích."
        m "Anh đang bán đứng chính đồng bào mình cho kẻ khác, gọi đó là 'cơ hội'."

    else:
        m "Ta biết những thứ anh rao giảng là giả dối..."
        m "Nhưng ta chưa có bằng chứng để cho mọi người thấy hết bộ mặt thật của anh."

    l "Câm miệng!"
    l "Đồ ranh con không hiểu chuyện người lớn!"

    jump man3_card3


# -------- Thẻ 3 --------

label man3_card3:

    l "Dân đen thì biết gì!"
    l "Chỉ cần cho họ ăn, cho họ chơi, cho họ quên là đủ!"
    l "Tỉnh táo quá làm gì, chỉ chuốc khổ vào thân!"

    m "Đây là đòn cuối cùng..."

    menu:
        "[[ĐẠI CHÚNG]]":
            jump good_ending
        "Bỏ đi":
            jump bad_ending
