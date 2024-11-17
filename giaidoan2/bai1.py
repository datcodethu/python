def gop_thong_tin(ten, **kwargs):
    return {'ten': ten, **kwargs}

# Ví dụ kiểm tra
print(gop_thong_tin("Mai", tuoi=30, nghe_nghiep="Bac si"))
# Kết quả mong muốn: {'ten': 'Mai', 'tuoi': 30, 'nghe_nghiep': 'Bac si'}
