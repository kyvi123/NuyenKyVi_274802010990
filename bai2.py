class SinhVien:
    def __init__(self, ma_sv, ho_ten, ngay_sinh, lop):
        """
        Tạo một đối tượng sinh viên mới.

        Args:
            ma_sv (str): Mã số sinh viên.
            ho_ten (str): Họ và tên sinh viên.
            ngay_sinh (str): Ngày sinh của sinh viên.
            lop (str): Lớp của sinh viên.
        """
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.lop = lop

    def __str__(self):
        return f"Mã SV: {self.ma_sv}, Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Lớp: {self.lop}"

danh_sach_sinh_vien = []

def them_sinh_vien():
    """
    Thêm một sinh viên mới vào danh sách.
    """
    ma_sv = input("Nhập mã sinh viên: ")
    ho_ten = input("Nhập họ tên: ")
    ngay_sinh = input("Nhập ngày sinh: ")
    lop = input("Nhập lớp: ")
    sv_moi = SinhVien(ma_sv, ho_ten, ngay_sinh, lop)
    danh_sach_sinh_vien.append(sv_moi)
    print("Đã thêm sinh viên thành công!")

def xoa_sinh_vien():
    """
    Xóa một sinh viên khỏi danh sách.
    """
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    for i, sv in enumerate(danh_sach_sinh_vien):
        if sv.ma_sv == ma_sv:
            danh_sach_sinh_vien.pop(i)
            print("Đã xóa sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên có mã này!")

def sua_thong_tin():
    """
    Sửa thông tin của một sinh viên trong danh sách.
    """
    ma_sv = input("Nhập mã sinh viên cần sửa: ")
    for sv in danh_sach_sinh_vien:
        if sv.ma_sv == ma_sv:
            sv.ho_ten = input("Nhập họ tên mới: ")
            sv.ngay_sinh = input("Nhập ngày sinh mới: ")
            sv.lop = input("Nhập lớp mới: ")
            print("Đã cập nhật thông tin thành công!")
            return
    print("Không tìm thấy sinh viên có mã này!")

def tim_kiem_sinh_vien():
    """
    Tìm kiếm sinh viên trong danh sách.
    """
    keyword = input("Nhập từ khóa tìm kiếm: ")
    ket_qua = [sv for sv in danh_sach_sinh_vien if keyword.lower() in sv.ho_ten.lower()]
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for sv in ket_qua:
            print(sv)
    else:
        print("Không tìm thấy kết quả!")

def hien_thi_danh_sach():
    """
    Hiển thị danh sách sinh viên.
    """
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên rỗng.")
    else:
        print("Danh sách sinh viên:")
        for sv in danh_sach_sinh_vien:
            print(sv)

while True:
    print("\n--- Quản lý sinh viên ---")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa thông tin")
    print("4. Tìm kiếm sinh viên")
    print("5. Hiển thị danh sách")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn: ")

    if lua_chon == "1":
        them_sinh_vien()
    elif lua_chon == "2":
        xoa_sinh_vien()
    elif lua_chon == "3":
        sua_thong_tin()
    elif lua_chon == "4":
        tim_kiem_sinh_vien()
    elif lua_chon == "5":
        hien_thi_danh_sach()
    elif lua_chon == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")