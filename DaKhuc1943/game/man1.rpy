# ------------------------------------------
# MÀN 1: CÁI BỤNG VÀ CÁI ĐẦU
# ------------------------------------------

label man_1:
    scene bg san_dinh with dissolve
    show tu_gian_du

    m "Đình làng hỗn loạn quá. Bác Tư đang cầm búa định phá cột đình để bán gỗ."
    m "Mình phải ngăn bác ấy lại. Nhưng nói tay không thì bác ấy không nghe đâu."
    m "Mình cần tìm bằng chứng ở xung quanh đây hoặc ngoài cổng làng."

    # Bắt đầu vòng lặp di chuyển
    jump di_chuyen_san_dinh


# --- LABEL ĐIỀU KHIỂN: SÂN ĐÌNH ---

label di_chuyen_san_dinh:
    # Gọi màn hình Sân Đình.
    # Nếu người chơi click Bác Tư -> Return() -> nhảy sang tranh_luan_bac_tu.
    call screen phong_san_dinh
    jump tranh_luan_bac_tu


# --- LABEL ĐIỀU KHIỂN: CỔNG LÀNG ---

label di_chuyen_cong_lang:
    # Gọi màn hình Cổng Làng.
    # Các nút trong screen sẽ Jump tới nhặt đồ hoặc quay lại sân đình.
    call screen phong_cong_lang
    jump di_chuyen_san_dinh


# ------------------------------------------
# CÁC SỰ KIỆN NHẶT ĐỒ
# ------------------------------------------

label nhat_trat_no:
    scene bg cong_lang
    call screen thong_bao_nhat_do("icon_trat_no", "Trát Đòi Nợ")

    "Bạn nhặt được một tờ giấy nhàu nát."
    m "Đây là... TRÁT ĐÒI NỢ của Lý Trưởng?"
    m "Hắn ghi rõ: 'Tiền bán gỗ đình sẽ sung công quỹ trừ nợ thuế'. Khốn nạn thật!"

    $ inventory.append("trat_no")

    # Nhặt xong thì quay lại cổng làng
    jump di_chuyen_cong_lang


label nhat_bai_vi:
    scene bg san_dinh
    call screen thong_bao_nhat_do("icon_bai_vi", "Mảnh Bài Vị")

    "Bạn nhặt được mảnh gỗ dưới đất."
    m "Trời đất! Đây là bài vị thờ Thần Thành Hoàng mà?"
    m "Bán đình là bán cả tổ tiên sao?"

    $ inventory.append("bai_vi")

    jump di_chuyen_san_dinh


# ------------------------------------------
# TRANH LUẬN (BOSS FIGHT)
# ------------------------------------------

label tranh_luan_bac_tu:
    scene bg san_dinh
    show tu_gian_du_tranh_luan at center

    # Reset điểm niềm tin
    $ trust_score = 3
    show screen hien_thi_niem_tin with dissolve

    tu "Tránh ra! Tao đập hết! Đói lắm rồi!"
    m "Bác Tư! Bác bình tĩnh đã!"

    # --- HIỆP 1: THÁI ĐỘ ---

    tu "Mày là cái thá gì mà ra lệnh cho tao? Đồ ranh con vắt mũi chưa sạch!"

    menu:
        "Bác già rồi mà hồ đồ quá! Phá hoại là có tội đấy!":
            $ trust_score -= 2
            tu "Mày dám hỗn với tao à? Cút ngay!"

        "(Cúi đầu) Cháu đâu dám dạy khôn bác. Cháu sợ bác thiệt thòi nên mới can thôi ạ.":
            $ trust_score += 2
            hide tu_gian_du_tranh_luan
            show tu_boi_roi_tranh_luan
            tu "Hừ... Thiệt thòi cái gì? Bán đi có gạo ăn mà thiệt à?"

    # --- HIỆP 2: ĐỒNG CẢM & BÀI VỊ ---

    tu "Vợ con tao sắp chết đói rồi! Gỗ mục nát thế này giữ làm gì?"

    menu:
        "Cháu hiểu chứ bác. Nhưng đừng vì miếng ăn mà làm bậy.":
            $ trust_score -= 2
            tu "Lại văn vở! Tao nhổ vào lý thuyết của mày!"

        "Đưa [[MẢNH BÀI VỊ]] và nói: Bác định bán cả tổ tiên sao?" if "bai_vi" in inventory:
            $ trust_score += 4
            hide tu_gian_du_tranh_luan
            show tu_boi_roi_tranh_luan
            tu "(Cầm mảnh gỗ)... Tên ông nội tao... Sao lại nằm dưới đất thế này?"
            m "Đấy bác xem, chưa bán mà đã thế này. Bán rồi thì vong linh các cụ đi về đâu?"

    # --- HIỆP 3: CHỐT HẠ & TRÁT NỢ ---

    tu "Nhưng tao cùng đường rồi. Lý Trưởng bảo bán đình xong sẽ xóa nợ cho tao..."

    menu:
        "Lão ấy lừa bác đấy, đừng tin!":
            # Nếu uy tín đủ cao mà không có bằng chứng -> Ending bình thường,
            # ngược lại -> Ending thua.
            if trust_score >= 6:
                jump ket_thuc_binh_thuong
            else:
                jump ket_thuc_thua

        "Đưa bằng chứng [[TRÁT ĐÒI NỢ]]" if "trat_no" in inventory:
            $ trust_score += 5
            m "Bác xem giấy nợ này đi! Lão ấy ghi rõ: 'Tiền bán đình sung công quỹ'. Bác bán xong là mất trắng đấy!"
            jump ket_thuc_thang


# ------------------------------------------
# CÁC KẾT THÚC (ENDINGS)
# ------------------------------------------

label ket_thuc_thua:
    hide tu_boi_roi
    hide tu_boi_roi_tranh_luan
    hide tu_gian_du_tranh_luan
    show tu_gian_du

    tu "Mày nói mồm ai tin? Tránh ra cho tao đập!"
    "Bác Tư gạt phăng tôi ra và vung búa đập mạnh vào cột đình."

    hide screen hien_thi_niem_tin

    "Ngôi đình bị phá hủy. Bác Tư bán gỗ xong vẫn không trả được nợ."
    "Nhưng đó đã là chuyện sau này rồi..."
    "Tôi rời đi với nỗi buồn vô hạn."

    jump man_2


label ket_thuc_binh_thuong:
    hide screen hien_thi_niem_tin
    hide tu_boi_roi_tranh_luan
    hide tu_gian_du_tranh_luan
    hide tu_gian_du
    show tu_boi_roi

    tu "Tao... tao tin mày [ten_mc] ạ. Nhưng không có bằng chứng thì tao không đấu lại Lý Trưởng được."
    tu "Thôi, tao về... Mặc kệ đời ra sao thì ra."

    "Bác Tư bỏ về. Ngôi đình còn đó nhưng lòng người đã ly tán."
    "Mang theo nhiều trắc trở, tôi cũng rời khỏi ngôi đình."

    jump man_2


label ket_thuc_thang:
    hide screen hien_thi_niem_tin
    hide tu_boi_roi_tranh_luan
    hide tu_gian_du_tranh_luan
    hide tu_gian_du
    show tu_vui

    tu "Tiên sư cha nhà nó! Nó định lừa tao à?"
    tu "Cảm ơn mày [ten_mc]! Cũng hên nhờ có mày, tao suýt nữa thì thành tội đồ!"
    m "Không có gì đâu bác. Chúng ta phải giúp nhau lúc khó khăn chứ!"
    tu "Ừ! Tao sẽ không bán đình nữa. Cứ để đó cho con cháu sau này."

    "Bác Tư quyết tâm giữ lại ngôi đình làng."
    m "Thôi cháu còn có việc cháu đi trước nhé bác!"
    tu "Đi đi! Lúc nào rảnh lại ghé chơi với tao nhé!"
    m "Từ xa xa nhìn lại chú Tư, lòng tôi chợt nghĩ đến vài thứ..."

    call quy_trinh_ngam_tho(
        "Ly gia thập niên hề, phụ mẫu sinh biệt,\nThê tử hà kham hề, độc túc cô phòng.\nTuy hữu du điền hề, thuỳ dữ chi thủ,\nLân gia tửu thục hề, thục dữ chi thường.\nBạch phát y môn hề, vọng xuyên thu thuỷ,\nTrĩ tử ức niệm hề, lệ đoạn can trường.\nHồ mã tê phong hề, thượng tri luyến thổ,\nNhân sinh khách cửu hề, ninh vong cố hương.",
        "Mười năm rời nhà, xa mẹ cha, tôi mới hiểu thế nào là nỗi quạnh quẽ. Vợ con ở nhà ai thấu được cảnh mình lẻ loi đất khách. Dù có để lại ruộng vườn tốt tươi, nhưng chẳng còn ai kề cận chăm nom. Hàng xóm làng giềng rượu ngon cũng chẳng còn người cùng nhấp. Mỗi chiều thu, đứng tựa cửa nhìn sương rơi mà lòng trĩu nặng đợi chờ. Nghĩ đến con thơ thương nhớ, chắc nó đã bao lần khóc cạn nước mắt. Ngựa còn nhớ chuồng, hổ còn nhớ núi, huống gì phận người xa xứ như tôi—làm sao quên được quê hương?"
    )

# =========================
# TITLE MÀN 2
# =========================

    # Màn 2
    

    jump man_2
