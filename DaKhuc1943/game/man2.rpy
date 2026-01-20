# ==========================================
# MÀN 2: THUỐC TIÊN HAY THUỐC ĐỘC? (REWORK)
# ==========================================

label man_2:
    # --- GIAI ĐOẠN 1: QUAN SÁT ---

    scene bg authlanding
    with fade

    show text "{size=80}{b}Màn 2{/b}\n{size=55}THUỐC TIÊN HAY THUỐC ĐỘC{/size}" at Position(xalign=0.1, yalign=0.5)
    # Người chơi bấm chuột / Enter để qua
    pause
    hide text

    scene bg mieu_tho_ben_ngoai with fade

    # Reset biến cho màn chơi mới
    $ inventory = []
    $ da_noi_chuyen_voi_thay = False
    $ da_dung_gao_nuoc = False

    m "Chia tay Bác Tư, tôi đi về phía gốc đa đầu làng."
    m "Từ xa, tôi đã thấy khói hương nghi ngút và tiếng lầm rầm khấn vái."
    m "Đó là Miếu Thờ của Thầy Bói Ba. Nghe nói dạo này dân làng tin ông ta lắm."
    m "Nhiều người đang quỳ lạy bên ngoài, vẻ mặt ai cũng thất thần, mê muội."
    m "Nhìn cảnh người dân mê muội quỳ lạy, lòng tôi đau như cắt."
    "Tôi bất giác nhớ đến câu thơ của cụ Phan Bội Châu..."

    call quy_trinh_ngam_tho(
        "Sinh nhược đồng nô lệ,\nTử diệc vi quỷ hùng.\nTuyệt lân đê mi cốt,\nVị cảm sỉ sài lang.",
        "Sống mà như nô lệ,\nChết cũng làm quỷ hùng.\nThương thay xương mi thấp,\nChưa dám thẹn sài lang."
    )

    m "Có chuyện gì mà họ sùng bái thế nhỉ? Tôi quyết định đi vào trong xem sao."
    window hide

    # Zoom vào cửa miếu (hiệu ứng bạn đã định nghĩa ở nơi khác)
    show bg mieu_tho_ben_ngoai at zoom_vao_cua_mieu

    # Dừng đúng thời gian hiệu ứng
    $ renpy.pause(2.5, hard=True)

    # Chuyển sang cảnh bên trong
    scene bg mieu_tho_ben_trong with fade
    window show

    m "Bên trong miếu, mùi hương trầm nồng nặc làm tôi thấy hơi choáng váng."

    show boi_tung_kinh at center

    boi "Nam mô... Thiên địa chứng giám..."
    boi "Uống nước này vào... Bệnh tật tiêu tan... Quên hết sầu đau..."

    "Tôi hỏi những người dân quanh đó thì được biết đây là Thầy Bói Ba, thầy pháp nổi tiếng trong vùng."
    "Thầy Bói Ba đang ngồi giữa điện, tay cầm phất trần, miệng lầm rầm khấn vái. Người dân quỳ rạp xung quanh như những con chiên ngoan đạo."
    "Mình nên lại gần xem hắn đang làm trò gì."
    window hide dissolve

    # Lúc này chưa tìm đồ được, phải nói chuyện trước
    call screen phong_mieu_tho


# ------------------------------------------
# GIAI ĐOẠN 2: CÁM DỖ & CHẤT VẤN
# ------------------------------------------

label hoi_thoai_dau_tien:
    hide boi_tung_kinh
    show boi_gian at center

    boi "Kẻ nào đấy? Nhìn mặt mũi sáng sủa mà sao thần sắc u ám thế kia?"

    hide boi_gian
    show boi_du_do at center
    boi "Con trai, lại đây thầy xem nào. Có phải cuộc đời ngoài kia quá khổ sở không?"

    "Đầu óc bạn muội đi phần nào vì mùi hương trầm. Bạn cảm thấy hơi choáng váng."

    menu:
        "Dạ... con cảm thấy mệt mỏi quá thầy ạ...":
            boi "Phải rồi... Thời buổi loạn lạc, người khôn thì ít, kẻ ác thì nhiều."
            boi "Đất nước lâm nguy, ai nấy đều lao vào tranh giành quyền lực, tiền bạc..."
            boi "Thấy thiên hạ lầm than, thần tiên trên trời cũng đau lòng."
            boi "Ta được các vị tiên nhân hiển thánh trên trời cử xuống trần gian cứu độ chúng sinh."
            boi "Để làm dịu đi nỗi đau thế nhân, thần đã ban cho ta 'thuốc tiên' giúp con người quên hết sự đời."
            boi "Đến đây với thầy. Thầy sẽ ban 'thuốc tiên' giúp con quên hết sự đời."

            menu:
                "Vâng, con muốn quên hết...":
                    jump ket_thuc_gia_nhap_giao_phai

                "??? chuyện gì thế này ???":
                    m "Không! Mình đang nghĩ cái gì thế này? Tỉnh táo lại đi [ten_mc]!"
                    m "Làm sao trên đời có thứ 'thuốc tiên' giúp quên hết sự đời chứ?"
                    jump chat_van_thay_boi

        "Thầy đang cho người dân uống cái gì thế?":
            jump chat_van_thay_boi


label chat_van_thay_boi:
    m "Thầy đang cho họ uống cái gì? Tại sao ai uống xong cũng lờ đờ, vô hồn thế kia?"

    boi "Con trai à, con nhìn nhầm rồi. Đó không phải là vô hồn, đó là sự 'Thanh Thản'."
    boi "Ngoài kia là gì? Là sưu cao thuế nặng, là vợ con đói khát, là đòn roi của Tây, Nhật..."
    boi "Còn ở đây, uống bát nước này vào, họ quên hết đau đớn, họ thấy mình đang ở chốn bồng lai tiên cảnh."
    boi "Ta lấy đi nỗi đau của họ, ban cho họ nụ cười. Chẳng phải ta đang làm phúc sao?"

    menu:
        "Nhưng đó là hạnh phúc giả tạo! Tỉnh lại họ sẽ còn khổ hơn!":
            boi "Hạnh phúc giả mà sướng còn hơn là thực tế mà khổ đau, con ạ."
            boi "Con muốn họ tỉnh lại để làm gì? Để nhìn thấy cái bụng lép kẹp của con mình à? Để khóc lóc van xin bọn cai lệ à?"
            boi "Con ép họ đối mặt với thực tại tàn khốc, trong khi ta cho họ một giấc mơ đẹp."
            boi "Vậy ta là Bồ Tát, hay con mới là kẻ tàn nhẫn đây?"

            menu:
                "Đừng ngụy biện! Dân tộc cần tỉnh táo để đấu tranh, không phải ngủ mê!":
                    jump thay_boi_lat_mat

                "Nghe cũng... có lý... (Sắp bị thao túng)":
                    m "(Khoan đã... mình đang bị cuốn theo lời hắn... Không! Thuốc phiện là thuốc độc!)"
                    m "Không! Giấc mơ đẹp đến mấy cũng là thuốc độc! Thầy đang giết mòn họ!"
                    jump thay_boi_lat_mat

        "Thầy đang đầu độc họ thì có! Cái này gây nghiện, khiến họ phụ thuộc vào thầy!":
            boi "Con gọi là nghiện, ta gọi là 'Đức Tin'."
            boi "Họ cần nơi nương tựa tinh thần. Ta cho họ chỗ dựa."
            boi "Con còn trẻ, con hăng máu, con muốn thay đổi thế giới. Nhưng những người già yếu này, họ chỉ cần một giấc ngủ ngon thôi."
            boi "Sao con nỡ tước đi niềm an ủi cuối cùng của họ?"

            m "Sự an ủi bằng thuốc phiện sao? Đó là tội ác!"
            jump thay_boi_lat_mat


label thay_boi_lat_mat:
    hide boi_du_do
    show boi_gian at center

    boi "Hừ! Rượu mời không uống muốn uống rượu phạt!"
    boi "Ta đã cố giảng giải đạo lý cho ngươi, nhưng tâm ngươi quá u tối, bị tà ma ngoại đạo ám rồi!"
    boi "Ở lại đây chỉ làm vấy bẩn sự thanh tịnh của các tín đồ ta!"

    dan "Đúng đấy! Thầy đang cứu khổ cứu nạn mà mày dám cãi à?"
    dan "Cút đi! Đừng để tao nhìn thấy mày!"

    boi "Nghe thấy chưa? Chúng sinh không cần cái 'tỉnh táo' của ngươi! Cút ngay!"

    hide boi_gian with moveoutright

    "Tôi bị đám đông cuồng tín đẩy dúi dụi ra góc sân."
    m "Đáng sợ thật... Hắn không chỉ đầu độc thân xác mà còn đầu độc cả tư tưởng của họ."
    m "Hắn biến cái ác thành cái thiện, biến thuốc độc thành thuốc thánh."
    m "Nếu không có bằng chứng vạch trần cái thứ 'thuốc tiên' kia, thì không ai tin mình cả."
    window hide

    # Mở khóa tìm đồ
    $ da_noi_chuyen_voi_thay = True

    # Quay lại màn hình tìm kiếm
    call screen phong_mieu_tho


# ------------------------------------------
# CÁC KẾT THÚC CỦA GIAI ĐOẠN CÁM DỖ
# ------------------------------------------

label ket_thuc_gia_nhap_giao_phai:
    scene bg mieu_tho_ben_trong with fade

    "Tôi quỳ xuống trước mặt Thầy Bói Ba. Mùi hương trầm làm đầu óc tôi mụ mị đi."
    "Thầy đưa cho tôi một bát nước đen ngòm. Tôi uống cạn."

    "Ngọt... và êm ru..."
    "Mọi lo toan về đất nước, về gia đình bỗng tan biến."

    "BAD ENDING: LINH HỒN LẠC LỐI"
    return


# ------------------------------------------
# GIAI ĐOẠN 3: TÌM BẰNG CHỨNG & TRANH LUẬN
# ------------------------------------------

label nhat_gao_nuoc:
    call screen thong_bao_nhat_do("icon_gao_nuoc", "Gáo Nước Bẩn")

    "Bạn lén múc một ít nước từ chum lên xem."
    m "Mùi gì kinh khủng thế này, hôi quá."
    m "Nước này chắc chắn không phải nước Thánh rồi."

    $ inventory.append("gao_nuoc")

    call screen phong_mieu_tho


label nhat_thuoc_phien:
    call screen thong_bao_nhat_do("icon_thuoc_phien", "Gói Thuốc Phiện")

    "Bạn phát hiện một gói giấy nhỏ giấu kín sau bát hương."
    m "Đây là... thuốc phiện đen! Hèn gì dân làng nghiện đến thế!"

    $ inventory.append("thuoc_phien")

    call screen phong_mieu_tho


# ==========================================
# TRANH LUẬN MÀN 2
# ==========================================

label tranh_luan_cuoi_cung:
    scene bg mieu_tho_ben_trong
    hide boi_du_do
    hide boi_so_hai
    show boi_gian at center

    # Reset cho vòng lặp tranh luận
    $ trust_score = 4
    $ da_dung_gao_nuoc = False
    $ so_lan_cai_cun = 0

    show screen hien_thi_niem_tin with dissolve

    jump hiep_3_loop_logic


label hiep_3_loop_logic:

    # --- GIỚI HẠN CÃI CÙN ---
    if so_lan_cai_cun >= 3:
        jump ket_thuc_m2_bi_duoi

    # --- LỜI THOẠI THEO TÌNH HUỐNG ---
    if so_lan_cai_cun == 0 and da_dung_gao_nuoc == False:
        boi "Ngươi vẫn chưa đi à? Muốn vạch mặt ta thì đưa bằng chứng đây! Đừng làm mất thời gian của các tín đồ!"
    elif so_lan_cai_cun > 0:
        hide boi_gian
        hide boi_so_hai
        show boi_du_do
        boi "Sao? Vẫn chưa chịu thôi à? Cố bới móc mà không ra gì thì mau xin lỗi thần linh đi!"
    else:
        boi "Hừ! Còn gì nữa không? Hay chỉ có mấy trò vu khống vặt vãnh này?"

    menu:
        "Đưa bằng chứng [[GÁO NƯỚC BẨN]]" if "gao_nuoc" in inventory and not da_dung_gao_nuoc:
            $ trust_score += 1
            $ da_dung_gao_nuoc = True

            m "Thầy đừng lảng tránh! Hãy nhìn bát nước này xem!"
            m "Nước đen ngòm, bốc mùi hôi thối nồng nặc. Thầy bảo đây là 'Nước Thánh' chữa bệnh sao?"
            m "Người khỏe uống vào còn nôn thốc nôn tháo, huống chi người bệnh!"
            
            hide boi_du_do
            hide boi_so_hai
            show boi_gian
            
            boi "Hừ! Đồ phàm phu tục tử! Ngươi chỉ nhìn thấy cái vỏ bề ngoài!"
            boi "Màu đen là màu của các vị thuốc quý ngâm 7 7 49 ngày!"
            boi "Cái mùi hôi đó là do thảo mộc bốc lên, có tác dụng thanh lọc cơ thể!"
            boi "Ma quỷ kị nhất là mùi hương này! Chỉ có người trong nghề mới biết thôi!"
            boi "Còn cái vị đắng? Ha! Thuốc đắng giã tật! Ngươi không hiểu y lý thì nên câm miệng!"

            dan "Ờ ha..."
            dan "Thuốc bắc cũng đen đen hôi hôi thế mà..."
            dan "Chắc thầy nói đúng..."

            m "(Chết tiệt! Hắn mồm mép quá. Mình cần bằng chứng không thể chối cãi được!)"
            jump hiep_3_loop_logic

        "Đưa bằng chứng [[GÓI THUỐC PHIỆN]]" if "thuoc_phien" in inventory:
            $ trust_score += 10

            with vpunch
            m "Thầy nói đó là thuốc bắc à? Vậy thầy giải thích thế nào về CÁI NÀY?"
            m "Một gói THUỐC PHIỆN đen sì, dẻo quánh tôi tìm thấy thầy giấu kỹ sau bàn thờ!"

            hide boi_gian
            hide boi_du_do
            show boi_so_hai

            boi "Cái... cái gì... Sao ngươi tìm thấy..."

            m "Bà con nhìn kỹ đi! Tại sao uống vào lại thấy lâng lâng? Tại sao không uống thì vật vã?"
            m "Là do NGHIỆN! Hắn đang biến bà con thành con nghiện để trục lợi!"

            dan "Trời ơi... Thảo nào..."
            jump ket_thuc_m2_thang

        "Tôi... tôi thấy thầy gian lắm!" if "thuoc_phien" not in inventory:
            $ so_lan_cai_cun += 1

            if so_lan_cai_cun == 1:
                $ trust_score -= 2

                m "Nhìn mặt thầy gian lắm! Chắc chắn thầy làm trò mờ ám!"
                show boi_gian
                boi "Ha ha ha! Tâm sinh tướng! Tâm ngươi đen tối nên nhìn ai cũng thấy gian!"
                boi "Không có bằng chứng thì đừng có ngậm máu phun người!"
                m "Đợi đấy! Tôi biết thầy có trò gì đó mờ ám, chỉ là tôi chưa chứng minh được thôi!"
                jump hiep_3_loop_logic

            elif so_lan_cai_cun == 2:
                $ trust_score -= 2

                m "Tôi thề là hắn lừa đảo! Trực giác của tôi không sai đâu!"
                dan "Cậu này nói năng lung tung quá! Không có bằng chứng mà cứ buộc tội người ta."
                dan "Xuống đi! Đừng làm mất thời gian của chúng tôi!"
                boi "Thấy chưa? Lòng dân là ý trời! Ngươi liệu hồn mà xéo đi!"
                jump hiep_3_loop_logic


# --- CÁC KẾT THÚC MÀN 2 ---

label ket_thuc_m2_bi_duoi:
    show boi_gian
    with vpunch

    boi "CÂM MỒM! Sự kiên nhẫn của ta có giới hạn!"
    boi "Người đâu! Đánh đuổi thằng phá hoại này ra khỏi làng cho ta!"

    dan "Đánh nó! Đánh nó!"

    scene bg mieu_tho_ben_ngoai with vpunch
    "Tôi bị đám đông giận dữ lôi xềnh xệch ra khỏi miếu và ném xuống nền đất lạnh lẽo."

    m "Đau quá... Họ u mê quá rồi, nói lý lẽ không lại."
    m "Mình đã thất bại trong việc vạch trần tên lừa đảo này."
    m "Nhưng không thể bỏ cuộc được. Mình phải gỡ gạc lại ở đó!"

    hide screen hien_thi_niem_tin
    window hide

    jump man_3


label ket_thuc_m2_thang:
    hide screen hien_thi_niem_tin

    with vpunch

    "Thầy Bói Ba mặt cắt không còn giọt máu, vứt cả quạt, bỏ chạy thục mạng ra khỏi miếu."
    hide boi_so_hai with moveoutright

    dan "Cảm ơn cậu! Hóa ra bấy lâu nay chúng tôi bị lừa tiền mất tật mang!"
    dan "Về thôi bà con ơi, về lo làm ăn chứ cúng bái gì nữa!"

    "Dân làng dần tản ra về. Ngôi miếu trở lại vẻ vắng lặng, tiêu điều vốn có của nó."

    m "Tôi đứng một mình giữa sân miếu, nhìn những tàn tích của gói thuốc phiện và gáo nước bẩn."
    m "Một kẻ buôn thần bán thánh đã bị vạch trần. Một thắng lợi nhỏ nhoi..."

    scene bg mieu_tho_ben_ngoai with dissolve
    "Bước ra khỏi miếu, nhìn thấy những người dân mê muội vẫn còn quỳ bái"
    "Gió bấc lại thốc vào mặt lạnh buốt. Ngoài kia, cờ Nhật và cờ Pháp vẫn bay phấp phới trên cổng làng."

    m "Diệt được một tên thầy bói, nhưng giặc ngoại xâm vẫn còn đó. Đồng bào vẫn đói khổ, lầm than."
    m "Chí làm trai thời loạn, nợ nước chưa trả xong, nghĩ đến người xưa mà thấy thẹn trong lòng..."

    call quy_trinh_ngam_tho(
        "Nam nhi vị liễu công danh trái,\nTu thính nhân gian thuyết Vũ hầu.",
        "Công danh nam tử còn vương nợ,\nLuống thẹn tai nghe chuyện Vũ hầu."
    )

    m "Không được tự mãn. Cuộc chiến thực sự vẫn còn ở phía trước."
    m "Nghe nói tối nay Cậu Long tổ chức đại tiệc 'Văn Minh' ở sân đình. Phải đến đó ngay!"
    m "Đó có thể là nơi nọc độc văn hóa đang lan tràn mạnh nhất."

    jump man_3
