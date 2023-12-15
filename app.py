import streamlit as st
import pandas as pd
import joblib
import streamlit as st

# Streamlit uygulamasını oluşturun
st.title("Televizyon Fiyat Tahmini Uygulaması")
ekran_boyutlari=pd.read_csv("Ekran_Boyutu.csv")
cozunurlukler=pd.read_csv("Cozunurluk.csv")
goruntu_kaliteleri=pd.read_csv("Goruntu_Kalitesi.csv")
garanti_tipleri=pd.read_csv("Garanti_Tipi.csv")
teknolojiler=pd.read_csv("Goruntuleme_Teknolojisi.csv")

model = joblib.load('tvs_decision_tree_model.pkl')
gb_model=joblib.load("tvs_gradient_boosting_model.pkl")

def ekran_index(Ekran_Boyutu):
    index= int(ekran_boyutlari[ekran_boyutlari["Ekran_Boyutu"]==Ekran_Boyutu].index.values)
    return index
def garantiTİp_index(Garanti_Tipi):
    index= int(garanti_tipleri[garanti_tipleri["Garanti_Tipi"]==Garanti_Tipi].index.values)
    return index
def teknolojiler_index(Goruntuleme_Teknolojisi):
    index= int(teknolojiler[teknolojiler["Goruntuleme_Teknolojisi"]==Goruntuleme_Teknolojisi].index.values)
    return index
def cozunurluk_index(Cozunurluk):
    index= int(cozunurlukler[cozunurlukler["Cozunurluk"]==Cozunurluk].index.values)
    return index
def goruntuKalite_index(Goruntu_Kalitesi):
    index= int(goruntu_kaliteleri[goruntu_kaliteleri["Goruntu_Kalitesi"]==Goruntu_Kalitesi].index.values)
    return index
def Smart_TV(Smart_TV):
    if Smart_TV =="Var":
        return 0
    else:
        return 1
    
def Dahili_uydu_alici(Dahili_uydu_alici):
    if Dahili_uydu_alici =="Var":
        return 0
    else:
        return 1


    

ekran_boyutu = ["Bilinmiyor", "orta ekranlar", "kucuk ekranlar", "buyuk ekranlar", "cok buyuk ekranlar"]
dahili_uydu_alici = ["Var", "Yok"]
garanti_tipi = ["Altus Garantili", "Arelik Garantili", "Awox Garantili", "Axen Garantili", "Beko Garantili",
                "Bilinmiyor", "Bilkom Garantili", "Dijitsu Garantili", "Grundig Garantili", "LG TR Garantili",
                "Next Garantili", "Onvo Garantili", "Philips TR Garantili", "Profilo Garantili", "Regal Garantili",
                "Resmi Distribtr Garantili", "Samsung TR Garantili", "Skytech Garantili", "Sony Eurasia Garantili",
                "Sunny Garantili", "Sunny Garantili", "Telefunken Garantili", "Telenova Garantili", "Vestel Garantili", "thalat Garantili"]
goruntu_kalitesi = ["4K Ultra HD", "8K Ultra HD", "Full HD", "Bilinmiyor", "HD Ready"]
goruntuleme_teknolojisi = ["Bilinmiyor", "DLED", "LED", "OLED", "QLED", "QNED"]
smart_tv = ["Var", "Yok"]
cozunurluk = ["1280 x 720", "1366 x 768", "1920 x 1080", "3840 x 2160", "4096 x 2160", "7680 x 4320", "Bilinmiyor"]



# Giriş formunu oluşturun
st.sidebar.header("Girdiler")
# Giriş alanlarını ekleyin (Örneğin: st.sidebar.slider, st.sidebar.text_input)
# Her bir özelliğe uygun girdileri oluşturun
ekran_boyutu = st.sidebar.selectbox("Ekran Boyutu Seçin", ekran_boyutu)
dahili_uydu_alici = st.sidebar.selectbox("Dahili Uydu Alıcı Seçin", dahili_uydu_alici)
garanti_tipi = st.sidebar.selectbox("Garanti Tipi Seçin", garanti_tipi)
goruntuleme_teknolojisi = st.sidebar.selectbox("Görüntüleme Teknolojisi Seçin", goruntuleme_teknolojisi)
goruntu_kalitesi = st.sidebar.selectbox("Görüntü Kalitesi Seçin", goruntu_kalitesi)
smart_tv = st.sidebar.selectbox("Smart-TV Var mı?", smart_tv)
cozunurluk = st.sidebar.selectbox("Çözünürlük Seçin", cozunurluk)

def create_prediction_value(Dahili_uydu_alici,Ekran_Boyutu,Garanti_Tipi,Goruntu_Kalitesi,Goruntuleme_Teknolojisi,Smart_TV,Cozunurluk):
    res=pd.DataFrame(data=
                    {'Dahili_uydu_alici':[Dahili_uydu_alici],'Ekran_Boyutu':[Ekran_Boyutu],
                    'Garanti_Tipi':[Garanti_Tipi],'Goruntu_Kalitesi':[Goruntu_Kalitesi],
                     'Goruntuleme_Teknolojisi':[Goruntuleme_Teknolojisi],
                    'Smart_TV':[Smart_TV],'Cozunurluk':[Cozunurluk]})
    return res


    
# Tahmin yapmak için bir düğme ekleyin
if st.sidebar.button("Fiyatı Tahmin Et"):
# Regresyon modelinizi kullanarak tahmin yapın
    # Tahmin yapın
    predict_value=create_prediction_value(Dahili_uydu_alici(dahili_uydu_alici),ekran_index(ekran_boyutu),garantiTİp_index(garanti_tipi),
               goruntuKalite_index(goruntu_kalitesi), teknolojiler_index(goruntuleme_teknolojisi),Smart_TV(Smart_TV),
                                      cozunurluk_index(cozunurluk))
    def predict_models(res):
        return "Decision Tree Result: "+str(int(model.predict(res))).strip('[]')+" TL"
    def predict_models2(res):
        return "Grand Boosting  Result: "+str(int(gb_model.predict(res))).strip('[]')+" TL"

    #predict_models(predict_value)
    #tahmin_fiyat = model.predict([[dahili_uydu_alici, ekran_boyutu, garanti_tipi,goruntu_kalitesi,goruntuleme_teknolojisi,smart_tv,cozunurluk]])

    
    # Sonucu ekrana yazdırın
    st.header("Tahmin Edilen Fiyat")
    st.write(predict_models(predict_value))
    st.write(predict_models2(predict_value))

