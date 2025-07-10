/hisse-tahmin-projesi/
├── data/
│   ├── sp500_tickers_correct.csv   # S&P 500 sembollerini içeren dosya
│   └── [hisse_senedi_verileri].csv # AAPL.csv, MSFT.csv gibi veri setleri
│
├── models/
│   └── [kaydedilmis_modeller].joblib  # Eğitim sonrası kaydedilen .joblib dosyaları
│
├── notebooks/
│   ├── 1_XGBoost_Train.ipynb         # XGBoost modeli için eğitim ve deney dosyası
│   ├── 2_RandomForest_Train.ipynb    # Random Forest modeli için eğitim ve deney dosyası
│   ├── 3_MLP_Train.ipynb             # MLP modeli için eğitim ve deney dosyası
│   │
│   ├── XGBoost_Test.ipynb            # Kayıtlı XGBoost modelleri için test dosyası
│   ├── RandomForest_Test.ipynb       # Kayıtlı RF modelleri için test dosyası
│   └── MLP_Test.ipynb                # Kayıtlı MLP modelleri için test dosyası
│
├── scrape_sp500.py                     # S&P 500 listesini çeken script
└── README.md                           # Bu dosya

Kurulum
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

git clone 
conda create -n hisse_tahmin python=3.10
conda activate hisse_tahmin
pip install -r requirements.txt



Testing
modelleri test etmek için notebook dosyasından test edilmek istenen modeli seçin örneğin xgboost_test sonrasında test etmek istediğiniz modeli seçmek için
aşağıdaki kısımları mevcut modellere göre değiştirin.Mevcut modelleri models dizininin altında görebilirsiniz.

STOCK_TICKER_TO_TEST = 'AES' # Modelin eğitildiği hisse senedi
SUBSET_TO_TEST = 'Tum_Ozellikler'
K_TO_TEST = 5
WINDOW_TO_TEST = 3


500 hisse sendi için eğittim için hem train sürem çok uzun oldu hem de çok yer kapladı (80gb) . Bu yüzden sadece AAPL hisse senedi için olanları yükleyeceğim ama hepsi için çalışıyor sistem her bir hisse sendininn ayrı ayrı alınmasının daha doğru olacağını düşündüğüm için bu şekilde yaptım ama train sürem çok uzadı ve bilgisayar hafızam yetmedi hatta bu yüzden RF tree dosyasında bir hata var.
