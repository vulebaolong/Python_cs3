# # input(" nhập họ tên")
# print("hello world")
# product= []
# listSV = [
#     {
#         "maSv": 1,
#         "tenSv": "Vũ Lê Bảo Long",
#         "diemToan": 10,
#         "diemVan": 8,
#         "diemHoa": 7,
#     },
#     {
#         "maSv": 2,
#         "tenSv": "Vũ Lê Bảo Long 2",
#         "diemToan": 5,
#         "diemVan": 9,
#         "diemHoa": 4,
#     },
#     {
#         "maSv": 3,
#         "tenSv": "Vũ Lê Bảo Long 3",
#         "diemToan": 7,
#         "diemVan": 4,
#         "diemHoa": 8,
#     },
#     {
#         "maSv": 4,
#         "tenSv": "Vũ Lê Bảo Long 4",
#         "diemToan": 3,
#         "diemVan": 5,
#         "diemHoa": 7,
#     },
#     {
#         "maSv": 5,
#         "tenSv": "Vũ Lê Bảo Long 5",
#         "diemToan": 7,
#         "diemVan": 4,
#         "diemHoa": 8,
#     },
# ]

# # Trung bình lớn hơn 5
# for sv in listSV:
#     diemSV = (sv["diemToan"] + sv["diemVan"] + sv["diemHoa"]) /3
#     print(diemSV)

# # điểm hoá dưới 5
# for sv in listSV:
#     if sv["diemToan"] < 5:
#         print("điểm hoá dưới 5", diemSV)


# # lặp
# for item in product:
#     print(item["name"])

# # thêm vào danh sách
# product.append({"id": 2, "name": "abc"})
# print("thêm vào danh sách", product)

# # xoá id 2
# product = [item for item in product if item["id"] != 2]
# print("xoá id 2", product)

# # cập nhật
# for item in product:
#     if item["id"] == 1:
#         item["name"] = "Samsung"
# print("cập nhật", product)


# OOP
# class NhanVien:
#     def __init__(self, maNhanVien, luongCoBan, heSoLuong):
#         self.maNhanVien = maNhanVien
#         self.luongCoBan = luongCoBan
#         self.heSoLuong = heSoLuong

#     def tinhLuong(self):
#         return self.luongCoBan * self.heSoLuong

#     def hienThiThongTin(self):
#         return f"""Mã nhân viên: {self.maNhanVien}"""


# nhanvien = NhanVien(123, 2000000, 2)
# print(nhanvien.hienThiThongTin())


# class GiamDoc(NhanVien):
#     def __init__(self, maNhanVien, luongCoBan, heSoLuong, tienThuong):
#         super().__init__(maNhanVien, luongCoBan, heSoLuong)
#         self.tienThuong = tienThuong

#     def layTienThuong(self):
#         return self.tienThuong

#     # ghi đè
#     def tinhLuong(self):
#         return super().tinhLuong() + self.tienThuong


# giamdoc = GiamDoc(2, 1000, 2, 200)
# print(giamdoc.tinhLuong())

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc():
        return

class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = khoaHoc

    def dangKyKhoaHoc(self):
        return self.khoaHoc
    
    def hienThiKhoaHoc(self):
        return self.khoaHoc
    
khoaHoc1 = KhoaHoc(123, "Javascript", "online", 1000)
khoaHoc2 = KhoaHoc(123, "Python", "ofline", 2000)
long = HocVien(456, "vulebaolong", "14/3/2000", khoaHoc1)
long = HocVien(457, "longbaolevu", "14/3/2000", khoaHoc1)

# đăng ký khoá học
long.dangKyKhoaHoc(khoaHoc1)
long.hienThiKhoaHoc(khoaHoc1)



    



