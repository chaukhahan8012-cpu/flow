import streamlit as st

def draw_professional_workflow():
    st.header("⚙️ Quy trình Vận hành Hệ thống AgriLoop")
    
    # Sử dụng Graphviz với ngôn ngữ DOT được tinh chỉnh màu sắc
    st.graphviz_chart('''
    digraph G {
        # Cấu hình chung cho toàn sơ đồ
        fontname="Arial";
        compound=true;
        rankdir=LR;  # Vẽ từ trái sang phải
        node [fontname="Arial", shape=box, style="filled, rounded", color="#2E7D32", fontcolor=white];
        edge [fontname="Arial", color="#546E7A", penwidth=1.5];

        # LAYER 1: NGƯỜI DÙNG ĐẦU VÀO (SUPPLY)
        subgraph cluster_input {
            label = "PHÂN HỆ QUẢN LÝ NGUỒN CUNG";
            style = "filled, dashed";
            color = "#E8F5E9";
            fontcolor = "#2E7D32";
            
            F [label="👨‍🌾 Nông dân\\n(Đăng đơn hàng)", fillcolor="#43A047"];
            GPS [label="📍 Định vị GPS\\n& Khối lượng", fillcolor="#43A047"];
        }

        # LAYER 2: BỘ NÃO HỆ THỐNG (CORE AI)
        subgraph cluster_core {
            label = "HỆ THỐNG TRUNG TÂM (AGRILOOP CORE)";
            style = "filled";
            color = "#E3F2FD";
            fontcolor = "#1565C0";
            
            MATCH [label="🤖 Matching Engine\\n(Khớp Cung - Cầu)", fillcolor="#1E88E5"];
            POOL [label="📦 Pooling Algorithm\\n(Ghép chuyến tối ưu)", fillcolor="#1E88E5"];
        }

        # LAYER 3: VẬN TẢI & NHÀ MÁY (OUTPUT)
        subgraph cluster_output {
            label = "PHÂN HỆ LOGISTICS & TIÊU THỤ";
            style = "filled, dashed";
            color = "#FFF3E0";
            fontcolor = "#E65100";
            
            DRIVE [label="🚚 Đội xe AgriLoop\\n(Nhận lộ trình)", fillcolor="#FB8C00"];
            FACT [label="🏭 Nhà máy\\n(Nhận hàng & Số hóa)", fillcolor="#FB8C00"];
        }

        # DÒNG CHẢY DỮ LIỆU
        F -> GPS;
        GPS -> MATCH [label="Data Stream"];
        MATCH -> POOL [label="Tối ưu đơn"];
        POOL -> DRIVE [label="Lệnh điều phối"];
        DRIVE -> FACT [label="Giao hàng"];
        
        # PHẢN HỒI (FEEDBACK LOOP)
        FACT -> F [label="Thanh toán & Truy xuất", style=dotted, constraint=false, color="#00897B"];
    }
    ''')

# Gọi hàm để hiển thị
draw_professional_workflow()