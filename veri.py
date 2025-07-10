import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_and_save_sp500_tickers(save_dir='data', filename='sp500_tickers_correct.csv'):
    """
    slickcharts.com adresinden S&P 500 hisse senedi SEMBOLLERİNİ (ticker) çeker
    ve belirtilen konuma bir CSV dosyası olarak kaydeder.
    """
    print("Slickcharts'tan S&P 500 sembolleri çekilmeye başlanıyor...")
    
    url = 'https://www.slickcharts.com/sp500'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Web sayfasına başarıyla erişildi.")
    except requests.exceptions.RequestException as e:
        print(f"HATA: Web sayfasına erişilemedi: {e}")
        return False

    soup = BeautifulSoup(response.text, 'html.parser')
    tickers = []
    table = soup.find('table', class_='table table-hover table-borderless table-sm')
    
    if not table:
        print("HATA: Sayfa içinde S&P 500 tablosu bulunamadı.")
        return False
        
    # Tablonun satırlarında dön (ilk satır başlık, o yüzden atla)
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) > 2: # Satırda en az 3 hücre olduğundan emin ol
            # --- ÖNEMLİ DÜZELTME BURADA ---
            # Şirket Adı (cells[1]) YERİNE, Hisse Sembolü (cells[2]) alınıyor.
            ticker = cells[2].text.strip()
            tickers.append(ticker)
            
    if not tickers:
        print("UYARI: Tablo bulundu ancak hiçbir hisse senedi sembolü çekilemedi.")
        return False
        
    print(f"Başarıyla {len(tickers)} adet hisse senedi sembolü (ticker) çekildi.")
    
    df = pd.DataFrame(tickers, columns=['Symbol'])
    
    os.makedirs(save_dir, exist_ok=True)
    full_path = os.path.join(save_dir, filename)
    
    try:
        df.to_csv(full_path, index=False)
        print(f"Veri başarıyla '{full_path}' dosyasına kaydedildi.")
        return True
    except Exception as e:
        print(f"HATA: Dosya kaydedilirken bir sorun oluştu: {e}")
        return False

if __name__ == '__main__':
    scrape_and_save_sp500_tickers()