import streamlit as st

def draw_agri_loop_workflow():
    st.title("Hệ Thống Quản Lý Chuỗi Cung Ứng Phế Phẩm Nông Nghiệp AgriLoop - Luồng Vận Hành")

    # Define a clean Graphviz digraph without icons
    st.graphviz_chart('''
    digraph G {
        fontname="Arial, sans-serif";
        rankdir=LR; // Left to Right workflow
        node [fontname="Arial, sans-serif", shape=box, style="filled, rounded", color="#2E7D32", fontcolor=white];
        edge [fontname="Arial, sans-serif", color="#546E7A", penwidth=1.5];

        # Main entities (nodes)
        A [label="Nông dân", fillcolor="#43A047"];
        B [label="Hệ thống AgriLoop", fillcolor="#1E88E5"];
        C [label="Đội ngũ Tài xế", fillcolor="#FB8C00"];
        D [label="Nhà máy tiêu thụ", fillcolor="#E53935"];

        # Key interactions (edges with labels)
        A -> B [label="Báo có phế phẩm"];
        B -> C [label="Điều phối ghép chuyến"];
        C -> D [label="Giao hàng"];
        D -> A [label="Thanh toán & Số hóa", style=dashed, color="#00897B"];
    }
    ''')

draw_agri_loop_workflow()
