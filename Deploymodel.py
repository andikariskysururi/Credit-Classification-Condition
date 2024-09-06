import streamlit as st 
import joblib 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
import pandas as pd 

label_encoder_personal = joblib.load("C:\DeployIntern\LabelEncoder_personal1.pkl")
preprocessing_personal = joblib.load("C:\DeployIntern\preprocessing_personal_pipeline1.pkl")
model_personal = joblib.load("C:\DeployIntern\model_personal1.pkl")

label_encoder_bisnis = joblib.load("C:\DeployIntern\label_encoder_bisnis.pkl")
preprocessing_bisnis = joblib.load("C:\DeployIntern\Preprocessing_bisnis_pipeline.pkl")
model_bisnis = joblib.load("C:\DeployIntern\model_bisnis.pkl")



def personal():
    col1, col2, col3 = st.columns(3)

    with col1:
        ordinal__kecenderungan_untuk_bermasalah_hukum = st.selectbox('Kecenderungan bermasalah hukum', 
                                    options=['Tinggi', 'Sedang', 'Rendah', ' Tidak ada'],index = None)

        ordinal__tingkat_musibah = st.selectbox('Tingkat musibah', 
                                    options=['Tinggi', 'Sedang', 'Rendah'],index = None)
        ordinal__huru_hara = st.selectbox('Huru hara', 
                                    options=['Tinggi', 'Sedang', 'Rendah'], index = None)
        ordinal__kriminalitas =st.selectbox('Kecenderungan kriminalitas', 
                                    options=['Tinggi', 'Sedang', 'Rendah'], index = None)
        ordinal__riwayat_penyakit_berat = st.selectbox('Riwayat penyakit berat', 
                                    options=['Iya','Tidak'], index = None)
        ordinal__konflik_perceraian =st.selectbox('Konflik Perceraian', 
                                    options=['Iya', 'Tidak'], index = None)
        ordinal__Kategori_Penghasilan = st.selectbox('Kategori Penghasilan', 
                                    options=['<1000000', '1000000 - 3000000', '3000000 - 5000000', '5000000 - 7000000',
                                                '7000000 - 10000000','10000000 - 15000000', '15000000 - 30000000','>30000000'], index = None)
        ordinal__Jenjang_Karir_Pekerjaan = st.selectbox('Jenjang karir saat ini', 
                                    options=['Prospektif', 'Stabil', 'Terbatas'], index = None)
        ordinal__Kemungkinan_Kebutuhan_Meningkat = st.selectbox('Kemungkinan kebutuhan meningkat', 
                                options=['Ya', 'Tidak'], index = None)
    with col2:

        ordinal__Peluang_Promosi =st.selectbox('Peluang Promosi', 
                                    options=['peluang promosi terbatas', 'tersedia peluang promosi', 'sedikit peluang promosi'], index = None)
        remainder__beban_tanggungan = st.number_input('Masukkan Nilai Beban Tanggunganmu')
        remainder__Penghasilan = st.number_input('Masukkan Penghasilanmu per bulan')
        remainder__lama_bekerja = st.number_input('Lama Bekerja dalam satuan tahun')
        remainder__pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji = st.selectbox('Jenjang karir saat ini', 
                                    options=['Freelancer', 'Pedagang Kaki Lima', 'Pekerja di Industri Informal',
                                                'Pekerja Garmen','Pekerja Harian Lepas', 'Pekerja Industri Hiburan',
                                                'Pekerja Konstruksi','Pekerja Musiman', 'Pengemudi Taksi/Ojek Online',
                                                'Pengusaha Kecil', 'Penulis Lepas','Seniman/Artis'], index = None)
        if remainder__pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji is not None: 
            remainder__pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji = label_encoder_personal[0].transform(np.array(remainder__pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji).reshape(-1))
        
        remainder__narkoba =st.selectbox('Pernah terjerat narkoba', 
                                    options=['Iya', 'Tidak'], index = None)
        if remainder__narkoba is not None : 
            remainder__narkoba = label_encoder_personal[1].transform(np.array(remainder__narkoba).reshape(-1))
        
        remainder__terkena_kriminalitas_sebagai_korban = st.selectbox('Pernah menjadi korban kriminalitas', 
                                    options=['Iya', 'Tidak'], index = None)
        if remainder__terkena_kriminalitas_sebagai_korban is not None: 
            remainder__terkena_kriminalitas_sebagai_korban = label_encoder_personal[2].transform(np.array(remainder__terkena_kriminalitas_sebagai_korban).reshape(-1))
        
        remainder__jenis_bencana = st.selectbox('Pernah menjadi korban bencana', 
                                    options=['Bencana Alam', 'Bencana Non Alam'], index = None)
        if remainder__jenis_bencana is not None : 
            remainder__jenis_bencana = label_encoder_personal[3].transform(np.array(remainder__jenis_bencana).reshape(-1))
        
        remainder__bencana = st.selectbox('Bencana Alam', 
                                    options=['Bencana', 'Banjir', 'Gempa Bumi', 'Gunung Meletus',
                                                'Kebakaran', 'Perang/Konflik', 'Tanah Longsor', 'Tsunami', 'Wabah Penyakit'], index = None)
        if remainder__bencana is not None : 
            remainder__bencana = label_encoder_personal[4].transform(np.array(remainder__bencana).reshape(-1))
    with col3:

        remainder__perlu_sarjana_gelar = st.selectbox('Punya gelar sarja', 
                                    options=['Iya', 'Tidak'], index = None)
        if remainder__perlu_sarjana_gelar is not None : 
            remainder__perlu_sarjana_gelar = label_encoder_personal[5].transform(np.array(remainder__perlu_sarjana_gelar).reshape(-1))
        remainder__beban_dan_tanggungan = st.selectbox('Beban Tanggungan', 
                                    options=[ 'Rendah','Sedang', 'Tinggi'], index = None)
        if remainder__beban_dan_tanggungan is not None: 
            remainder__beban_dan_tanggungan = label_encoder_personal[6].transform(np.array(remainder__beban_dan_tanggungan).reshape(-1))
            
        remainder__tingkat_musibah= st.selectbox('Potensi terkena musibah', 
                                    options=[ 'Rendah','Sedang', 'Tinggi'], index = None)
        if remainder__tingkat_musibah is not None : 
            remainder__tingkat_musibah = label_encoder_personal[7].transform(np.array(remainder__tingkat_musibah).reshape(-1))
    
        remainder__riwayat_bermasalah_hukum= st.selectbox('ada riwayat masalah hukum', 
                                    options=['Iya', 'Tidak'], index = None)
        if remainder__riwayat_bermasalah_hukum  is not None : 
            remainder__riwayat_bermasalah_hukum = label_encoder_personal[8].transform(np.array(remainder__riwayat_bermasalah_hukum).reshape(-1))
        
        remainder__riwayat_kriminal_anggota_keluarga_inti = st.selectbox('Keluarga inti punya riwayat kriminal', 
                                    options=['Iya', 'Tidak', 'Tidak ada'], index = None)
        if remainder__riwayat_kriminal_anggota_keluarga_inti is not None : 
            remainder__riwayat_kriminal_anggota_keluarga_inti = label_encoder_personal[9].transform(np.array(remainder__riwayat_kriminal_anggota_keluarga_inti).reshape(-1))

        remainder__Pengeluaran_dalam_Sebulan = st.number_input('Masukkan pengeluaran sebulan')
        remainder__total_hutang = st.number_input('Total hutang yang dimiliki')
        remainder__Punya_Bisnis = st.selectbox('Punya Bisnis', 
                                    options=['Punya', 'Tidak punya'], index = None)
        if remainder__Punya_Bisnis is not None : 
            remainder__Punya_Bisnis = label_encoder_personal[10].transform(np.array(remainder__Punya_Bisnis).reshape(-1))
        
        remainder__Bekerja= st.selectbox('Status Bekerja', 
                                    options=['Bekerja', 'Pengangguran'], index = None)
        if remainder__Bekerja is not None : 
            remainder__Bekerja = label_encoder_personal[11].transform(np.array(remainder__Bekerja).reshape(-1))
    daftar_variabel_dict = {
        'kecenderungan_untuk_bermasalah_hukum': ordinal__kecenderungan_untuk_bermasalah_hukum,
        'tingkat_musibah': ordinal__tingkat_musibah,
        'huru_hara': ordinal__huru_hara,
        'kriminalitas': ordinal__kriminalitas,
        'riwayat_penyakit_berat': ordinal__riwayat_penyakit_berat,
        'konflik_perceraian': ordinal__konflik_perceraian,
        'Kategori_Penghasilan': ordinal__Kategori_Penghasilan,
        'Jenjang_Karir_Pekerjaan': ordinal__Jenjang_Karir_Pekerjaan,
        'Kemungkinan_Kebutuhan_Meningkat': ordinal__Kemungkinan_Kebutuhan_Meningkat,
        'Peluang_Promosi': ordinal__Peluang_Promosi,
        'beban_tanggungan': remainder__beban_tanggungan,
        'Penghasilan': remainder__Penghasilan,
        'lama_bekerja': remainder__lama_bekerja,
        'pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji': remainder__pekerjaan_yang_berkecenderungan_untuk_melakukan_transaksi_ingkar_janji,
        'narkoba': remainder__narkoba,
        'terkena_kriminalitas_sebagai_korban': remainder__terkena_kriminalitas_sebagai_korban,
        'jenis_bencana': remainder__jenis_bencana,
        'bencana': remainder__bencana,
        'perlu_sarjana_gelar': remainder__perlu_sarjana_gelar,
        'beban_dan_tanggungan': remainder__beban_dan_tanggungan,
        'tingkat_musibah_(kecelakaan)': remainder__tingkat_musibah,
        'riwayat_bermasalah_hukum': remainder__riwayat_bermasalah_hukum,
        'riwayat_kriminal_anggota_keluarga_inti': remainder__riwayat_kriminal_anggota_keluarga_inti,
        'Pengeluaran_dalam_Sebulan': remainder__Pengeluaran_dalam_Sebulan,
        'total_hutang': remainder__total_hutang,
        'Punya_Bisnis': remainder__Punya_Bisnis,
        'Bekerja': remainder__Bekerja
    }
    daftar_variabel_dict = {k: [v] if not isinstance(v, (list, np.ndarray)) else v for k, v in daftar_variabel_dict.items()}

    df_personal = pd.DataFrame(daftar_variabel_dict)
    ordinal_cols_ = ['kecenderungan_untuk_bermasalah_hukum', 'tingkat_musibah', 'huru_hara',
            'kriminalitas', 'riwayat_penyakit_berat', 'konflik_perceraian',
            'Kategori_Penghasilan', 'Jenjang_Karir_Pekerjaan',
            'Kemungkinan_Kebutuhan_Meningkat', 'Peluang_Promosi']
    result_dict = {
        0: 'Layak',
        1 : 'Tidak Layak'
    }

    if None in df_personal.values :
        st.warning("Masih ada data yang kosong",icon="⚠️")
    else : 
        df_personal_prep = preprocessing_personal.transform(df_personal)
        print(pd.DataFrame(df_personal_prep, columns =preprocessing_personal.get_feature_names_out()).columns)
        print(df_personal_prep)
        print(df_personal)
        result = model_personal.predict(df_personal_prep)
        print(result)
        if result == 0 : 
            result = result_dict[result[0]]
            st.success(f"Status kamu {result} untuk mendapatkan peminjaman kredit")
        else : 
            result = result_dict[result[0]]
            st.warning(f"Status kamu {result} untuk mendapatkan peminjaman kredit",icon="⚠️")
            


def bisnis():
    Status_Perusahaan = st.selectbox("Status perusahaan", options=['Badan Usaha', 'Go Public'], index = None)
    if Status_Perusahaan is not None : 
        Status_Perusahaan = label_encoder_bisnis[0].transform(np.array(Status_Perusahaan).reshape(-1))
    arus_kas = st.selectbox("Arus kas", options=['Negatif' ,'Netral' ,'Positif','Tidak Ada'], index = None)
    sensitivitas_risiko = st.selectbox("Sensitivitas resiko", ['Rendah', 'Sedang', 'Tidak Ada','Tinggi'], index = None)
    potensi_ekonomi = st.selectbox("Potensi ekonomi", ['Rendah', 'Sedang', 'Tidak Ada','Tinggi'], index=None )
    kategori_potensi_ekonomi = st.selectbox("Kategori potensi ekonomi", ['Rendah', 'Sedang', 'Tidak Ada','Tinggi'], index=None )
    sumber_ekonomi	 = st.selectbox("Sumber ekonomi", ['Perindustrian','Perkebunan','Pertambangan','Pertanian','Peternakan','Tidak Ada'], index = None)
    if sumber_ekonomi is not None: 
        sumber_ekonomi = label_encoder_bisnis[1].transform(np.array(sumber_ekonomi).reshape(-1))

    pertumbuhan_ekonomi = st.selectbox("Pertumbuhan ekonomi", ['Rendah', 'Sedang', 'Tinggi'], index = None )
    kategori_tingkat_inflasi = st.selectbox("Kategori tingkat inflasi", ['Hiper', 'Moderat', 'Rendah', 'Tinggi'], index=None )
    potensi_pertumbuhan_usaha = st.selectbox("Potensi pertumbuhan usaha", ['Rendah', 'Sedang', 'Tidak Ada','Tinggi'], index=None )
    kualitas_produk = st.selectbox("Kualitas produk", ['Baik', 'Baik sekali', 'Biasa Saja', 'Buruk', 'Buruk Sekali', 'Tidak Ada' ], index = None)
    reputasi_brand = st.selectbox("Reputasi brand", ['Baik', 'Baik sekali', 'Biasa Saja', 'Buruk', 'Buruk Sekali', 'Tidak Ada'], index = None)
    usia_bisnis = st.number_input("Usia bisnis" )

    CHOICE = [
        'Afganistan', 'Afrika Selatan', 'Albania', 'Aljazair', 'Amerika Serikat', 
        'Andorra', 'Angola', 'Antigua dan Barbuda', 'Arab Saudi', 'Argentina', 
        'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahama', 'Bahrain', 
        'Bangladesh', 'Barbados', 'Belanda', 'Belarus', 'Belgia', 'Belize', 
        'Benin', 'Bhutan', 'Bolivia', 'Bosnia dan Herzegovina', 'Botswana', 
        'Brasil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Ceko', 
        'Chad', 'Chili', 'China', 'Denmark', 'Djibouti', 'Dominika', 'Ekuador', 
        'El Salvador', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 
        'Filipina', 'Finlandia', 'Gabon', 'Gambia', 'Georgia', 'Ghana', 'Grenada', 
        'Guatemala', 'Guinea', 'Guinea Khatulistiwa', 'Guinea-Bissau', 'Guyana', 
        'Haiti', 'Honduras', 'Hongaria', 'India', 'Inggris', 'Irak', 'Iran', 
        'Irlandia', 'Islandia', 'Israel', 'Italia', 'Jamaika', 'Jepang', 'Jerman', 
        'Kamboja', 'Kamerun', 'Kanada', 'Kazakhstan', 'Kenya', 'Kepulauan Marshall', 
        'Kepulauan Solomon', 'Kirgizstan', 'Kiribati', 'Kolombia', 'Komoro', 'Kongo', 
        'Korea Selatan', 'Korea Utara', 'Kosta Rika', 'Kroasia', 'Kuba', 'Kuwait', 
        'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 
        'Lituania', 'Luksemburg', 'Madagaskar', 'Makedonia Utara', 'Maladewa', 
        'Malawi', 'Malaysia', 'Mali', 'Malta', 'Maroko', 'Mauritania', 'Mauritius', 
        'Meksiko', 'Mesir', 'Mikronesia', 'Moldova', 'Monako', 'Mongolia', 
        'Montenegro', 'Mozambik', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Niger', 
        'Nigeria', 'Nikaragua', 'Norwegia', 'Oman', 'Pakistan', 'Palau', 'Panama', 
        'Pantai Gading', 'Papua Nugini', 'Paraguay', 'Peru', 'Polandia', 'Portugal', 
        'Qatar', 'Republik Afrika Tengah', 'Republik Demokratik Kongo', 
        'Republik Dominika', 'Rumania', 'Rusia', 'Rwanda', 'Saint Kitts dan Nevis', 
        'Saint Lucia', 'Saint Vincent dan Grenadines', 'Samoa', 'San Marino', 
        'Sao Tome dan Principe', 'Selandia Baru', 'Senegal', 'Serbia', 'Seychelles', 
        'Sierra Leone', 'Singapura', 'Siprus', 'Slovenia', 'Slowakia', 'Somalia', 
        'Spanyol', 'Sri Lanka', 'Sudan', 'Sudan Selatan', 'Suriname', 'Swedia', 
        'Swiss', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Tidak Ada', 
        'Timor Leste', 'Togo', 'Tonga', 'Trinidad dan Tobago', 'Tunisia', 'Turki', 
        'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraina', 'Uni Emirat Arab', 'Uruguay', 
        'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam'
    ]

    lokasi_customer_luar_negeri = st.selectbox("Lokasi customer LN", CHOICE , index= None)
    if lokasi_customer_luar_negeri is not None : 
        lokasi_customer_luar_negeri = label_encoder_bisnis[2].transform(np.array(lokasi_customer_luar_negeri).reshape(-1))
        
    keunggulan_pesaing_harga_lebih_murah = st.selectbox("Pesaing lebih murah",['Banyak', 'Sedang', 'Sedikit', 'Tidak Ada'], index= None)
    keunggulan_kompetitor_jangkauan_pasar_luas = st.selectbox("Keunggulan kompetisi jangkauan pasar", ['Banyak', 'Sedang', 'Sedikit', 'Tidak Ada'], index = None)
    keunggulan_kompetitor_kualitas_produk_lebih_baik = st.selectbox("Keunggulan kompetisi kualitas produk", [ 'Banyak', 'Sedang', 'Sedikit', 'Tidak Ada'], index = None)
    perilaku_pesaing_yang_inovatif = st.selectbox("Pesaing Inovatif", ['Banyak', 'Sedang', 'Sedikit', 'Tidak Ada'], index = None)
    perilaku_pesaing_yang_konservatif= st.selectbox("Pesaing konservatif", ['Banyak', 'Sedang', 'Sedikit', 'Tidak Ada'], index = None)
    regulasi_perusahaan = st.selectbox("Regulasi perusahaan", ['Iya', 'Tidak', 'Tidak Ada'], index = None)
    resiko_bisnis = st.selectbox("Resiko bisnis", ['Rendah', 'Sedang', 'Tidak Ada', 'Tinggi'], index=None)
    upaya_lingkungan = st.selectbox("Upaya lingkungan", ['Iya', 'Tidak', 'Tidak Ada'], index = None)
    bisnis_yang_sifatnya_adalah_musiman	 = st.selectbox("Bisnis musiman", ['Iya', 'Tidak', 'Tidak Ada'], index = None)
    resiko_daerah_bisnis = st.selectbox("Resiko daerah bisnis", ['Rendah', 'Sedang', 'Tidak Ada', 'Tinggi'], index=None)
    potensi_daerah =st.selectbox("Potensi daerah", ['Rendah', 'Sedang', 'Tidak Ada', 'Tinggi'], index=None)
    dukungan_grup = st.selectbox("Dukungan grup/afiliasi", ['Iya', 'Tidak', 'Tidak Ada'], index=None)

    daftar_variabel_dict = {
        "Status_Perusahaan": Status_Perusahaan,
        "arus_kas": arus_kas,
        "sensitivitas_risiko": sensitivitas_risiko,
        "potensi_ekonomi": potensi_ekonomi,
        "kategori_potensi_ekonomi": kategori_potensi_ekonomi,
        "sumber_ekonomi": sumber_ekonomi,
        "pertumbuhan_ekonomi": pertumbuhan_ekonomi,
        "kategori_tingkat_inflasi": kategori_tingkat_inflasi,
        "potensi_pertumbuhan_usaha": potensi_pertumbuhan_usaha,
        "kualitas_produk": kualitas_produk,
        "reputasi_brand": reputasi_brand,
        "usia_bisnis": usia_bisnis,
        "lokasi_customer_luar_negeri": lokasi_customer_luar_negeri,
        "keunggulan_pesaing_harga_lebih_murah": keunggulan_pesaing_harga_lebih_murah,
        "keunggulan_kompetitor_jangkauan_pasar_luas": keunggulan_kompetitor_jangkauan_pasar_luas,
        "keunggulan_kompetitor_kualitas_produk_lebih_baik": keunggulan_kompetitor_kualitas_produk_lebih_baik,
        "perilaku_pesaing_yang_inovatif": perilaku_pesaing_yang_inovatif,
        "perilaku_pesaing_yang_konservatif": perilaku_pesaing_yang_konservatif,
        "regulasi_perusahaan": regulasi_perusahaan,
        "resiko_bisnis": resiko_bisnis,
        "upaya_lingkungan": upaya_lingkungan,
        "bisnis_yang_sifatnya_adalah_musiman": bisnis_yang_sifatnya_adalah_musiman,
        "resiko_daerah_bisnis": resiko_daerah_bisnis,
        "potensi_daerah": potensi_daerah,
        "dukungan_grup/afiliasi": dukungan_grup
    }

    labelEncode_col = ['Status_Perusahaan', 'sumber_ekonomi', 'lokasi_customer_luar_negeri']
    num_cols = ['usia_bisnis']
    ordinal_col = ['arus_kas', 'sensitivitas_risiko', 'potensi_ekonomi',
        'kategori_potensi_ekonomi', 'pertumbuhan_ekonomi',
        'kategori_tingkat_inflasi', 'potensi_pertumbuhan_usaha',
        'kualitas_produk', 'reputasi_brand',
        'keunggulan_pesaing_harga_lebih_murah',
        'keunggulan_kompetitor_jangkauan_pasar_luas',
        'keunggulan_kompetitor_kualitas_produk_lebih_baik',
        'perilaku_pesaing_yang_inovatif', 'perilaku_pesaing_yang_konservatif',
        'regulasi_perusahaan', 'resiko_bisnis', 'upaya_lingkungan',
        'bisnis_yang_sifatnya_adalah_musiman', 'resiko_daerah_bisnis',
        'potensi_daerah', 'dukungan_grup/afiliasi']
    daftar_variabel_dict = {k: [v] if not isinstance(v, (list, np.ndarray)) else v for k, v in daftar_variabel_dict.items()}

    df_bisnis = pd.DataFrame(daftar_variabel_dict)
    ordinal_cols_ = ['kecenderungan_untuk_bermasalah_hukum', 'tingkat_musibah', 'huru_hara',
                'kriminalitas', 'riwayat_penyakit_berat', 'konflik_perceraian',
                'Kategori_Penghasilan', 'Jenjang_Karir_Pekerjaan',
                'Kemungkinan_Kebutuhan_Meningkat', 'Peluang_Promosi']
    result_dict = {
            0: 'Tidak Layak',
            1 : 'Layak'
        }

    if None in df_bisnis.values :
        st.warning("Masih ada data yang kosong",icon="⚠️")
    else : 
        df_bisnis_prep = preprocessing_bisnis.transform(df_bisnis)
        print(pd.DataFrame(df_bisnis_prep, columns =preprocessing_bisnis.get_feature_names_out()).columns)
        print(df_bisnis_prep)
        print(df_bisnis)
        result = model_bisnis.predict(df_bisnis_prep)
        print(result)
        if result == 0 : 
            result = result_dict[result[0]]
            st.warning(f"Status kamu {result} untuk mendapatkan peminjaman kredit",icon="⚠️")
        else : 
            result = result_dict[result[0]]
            st.success(f"Status kamu {result} untuk mendapatkan peminjaman kredit")

st.image(r"C:\DeployIntern\1519921584364 (1).jpeg")
st.title("CONDITIONAL CREDIT ACCEPTENCE")
type_pred = st.selectbox('Credit Purpose', options=['Personal', 'Bisnis'], index = None)
if type_pred == 'Personal':
    personal()
elif type_pred =="Bisnis" : 
    bisnis()
else : 
    st.warning("Tentukan Credit purpose terlebih dahulu",icon="⚠️")