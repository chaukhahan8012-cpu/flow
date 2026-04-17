import streamlit as st

def draw_simple_workflow():
    st.header("Quy trình hoạt động của AgriLoop ")
    
    st.graphviz_chart('''
    digraph G {
        rankdir=LR;
        node [fontname="Arial", shape=box, style="filled, rounded", color="#2E7D32", fontcolor=white];
        edge [fontname="Arial", color="#546E7A", penwidth=2];

        # CÁC BÊN THAM GIA
        A [label=" 1. Nông dân\\nBáo có hàng", fillcolor="#43A047"];
        B [label=" 2. Hệ thống AgriLoop\\nTìm người mua & Ghép xe", fillcolor="#1E88E5"];
        C [label=" 3. Tài xế\\nĐến lấy hàng & Giao đi", fillcolor="#FB8C00"];
        D [label=" 4. Nhà máy\\nNhận hàng & Trả tiền", fillcolor="#E53935"];

        # DÒNG CHẠY THỰC TẾ
        A -> B [label="Đăng tin"];
        B -> C [label="Điều xe"];
        C -> D [label="Chở hàng"];
        D -> A [label="Lưu lịch sử & Trả tiền", style=dashed, color="#00897B"];
    }
    ''')
    
    # Giải thích bằng lời văn "bình thường"
    st.write("### Giải thích đơn giản:")
    st.write("**Bước 1:** Nông dân thấy có vỏ trấu, rơm rạ thì lên app báo: 'Tui có hàng ở đây'.")
    st.write("**Bước 2:** App AgriLoop tự tìm xem nhà máy nào đang cần, sau đó xếp các ông nông dân ở gần nhau vào cùng một chuyến xe cho rẻ tiền xăng.")
    st.write("**Bước 3:** Tài xế nhận lệnh, chạy theo bản đồ app chỉ để gom hàng cho nhanh.")
    st.write("**Bước 4:** Hàng đến nhà máy, nhà máy quét mã xác nhận và tiền được chuyển về cho nông dân.")
