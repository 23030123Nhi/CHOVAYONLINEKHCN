import streamlit as st

st.title("HỆ THỐNG ĐÁNH GIÁ CHO VAY")

# Nhập dữ liệu
STV = st.number_input("NHẬP SỐ TIỀN MUỐN VAY (TRIỆU ĐỒNG)", min_value=0.0)
TGV = st.number_input("NHẬP THỜI GIAN VAY (SỐ NĂM)", min_value=0.1)
LSV = st.number_input("NHẬP LÃI SUẤT CHO VAY (SỐ THẬP PHÂN)", min_value=0.0, format="%.4f")
TN = st.number_input("NHẬP THU NHẬP HÀNG THÁNG (TRIỆU ĐỒNG/THÁNG)", min_value=0.0)
SNTGD = st.number_input("NHẬP SỐ NGƯỜI TRONG GIA ĐÌNH", min_value=0)

PTMC = st.number_input("NHẬP SỐ TIỀN PHẢI TRẢ CHO KHOẢN VAY CŨ (TRIỆU ĐỒNG)", min_value=0.0)
GTTSDB = st.number_input("NHẬP GIÁ TRỊ TSĐB (TRIỆU ĐỒNG)", min_value=0.1)
TUOI = st.number_input("NHẬP TUỔI KHÁCH HÀNG", min_value=0, max_value=120)

CPSH = 5  # Chi phí sinh hoạt mặc định

if st.button("Đánh giá khoản vay"):

    thu_nhap_kha_dung = TN - SNTGD * CPSH

    if thu_nhap_kha_dung <= 0:
        st.error("Thu nhập khả dụng không hợp lệ. Vui lòng kiểm tra lại dữ liệu.")
    else:
        # Tiền phải trả hàng tháng cho khoản vay mới
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))

        # Chỉ số DTI
        DTI = (PTMC + PTMM) / thu_nhap_kha_dung

        # Chỉ số LTV
        LTV = STV / GTTSDB

        st.subheader("Kết quả đánh giá")
        st.write(f"**DTI:** {DTI * 100:.2f}%")
        st.write(f"**LTV:** {LTV * 100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= TUOI <= 70:
            st.success("✅ ĐƯỢC CHO VAY")
        else:
            st.error("❌ KHÔNG ĐƯỢC CHO VAY")
