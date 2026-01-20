# Thêm vào đầu file script.rpy
transform zoom_vao_cua_mieu:
    # --- TRẠNG THÁI BẮT ĐẦU ---
    align (0.5, 0.5) 
    zoom 1.0 
    
    # --- HIỆU ỨNG ZOOM (Chạy trong 2.5 giây) ---
    # easein: Zoom nhanh dần rồi chậm lại (mượt hơn linear)
    # zoom 3.5: Phóng to 3.5 lần
    # align (0.85, 0.55): Di chuyển tâm điểm vào ngôi nhà bên phải
    easein 2.5 zoom 3.5 align (0.85, 0.7)