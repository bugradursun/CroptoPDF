from bs4 import BeautifulSoup

html_content = """
            <div class="stl_view">
                <div class="stl_05 stl_06">
                    <div class="stl_01" style="left:22.6365em;top:2.0979em;">
                        <span class="stl_07 stl_08 stl_09" style="word-spacing:0.001em;">DEPO REZERV BELGESİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:7.8154em;">
                        <span class="stl_10 stl_08 stl_11" style="word-spacing:0.0623em;">FATURA </span>
                        <span class="stl_12 stl_08 stl_11">TARİHİ: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:30.2183em;top:7.8342em;">
                        <span class="stl_13 stl_08 stl_14">B</span>
                        <span class="stl_15 stl_08 stl_09" style="word-spacing:0.0005em;">ELGE NO: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:9.5863em;">
                        <span class="stl_12 stl_08 stl_11" style="word-spacing:0.0004em;">DÜZENLEME TARİHİ: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:11.1929em;">
                        <span class="stl_16 stl_08 stl_17" style="word-spacing:0.0001em;">SATICI BİLGİLERİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:18.5175em;top:13.4723em;">
                        <span class="stl_18 stl_19 stl_20">SAHİPLİK &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:18.5175em;top:14.214em;">
                        <span class="stl_18 stl_19 stl_09">ORANI &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:7.7033em;top:13.8432em;">
                        <span class="stl_18 stl_19 stl_09" style="word-spacing:0.0001em;">AD SOYAD / ÜNVAN &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:21.8517em;top:13.8432em;">
                        <span class="stl_18 stl_19 stl_20" style="word-spacing:0.0002em;">TCKN / VKN</span>
                        <span class="stl_18 stl_19 stl_20" style="word-spacing:0.9212em;">&nbsp;</span>
                        <span class="stl_18 stl_19 stl_21">ADRES &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:38.3em;top:13.8432em;">
                        <span class="stl_18 stl_19 stl_09" style="word-spacing:0.0004em;">VERGİ DAİRESİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:38.55em;top:15.9473em;">
                        <span class="stl_18 stl_19 stl_20" style="word-spacing:0.0003em;">Gİ DAİRESİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.6667em;top:14.214em;">
                        <span class="stl_18 stl_19 stl_20">İŞLEM &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.6667em;top:14.9557em;">
                        <span class="stl_18 stl_19 stl_17">NO &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:26.5093em;top:15.943em;">
                        <span class="stl_22 stl_19 stl_20">8</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:17.6838em;">
                        <span class="stl_16 stl_08 stl_17" style="word-spacing:0.0001em;">ALICI BİLGİLERİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:21.45em;top:19.5923em;">
                        <span class="stl_18 stl_19 stl_20">SAHİPLİK &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:41.4017em;top:19.5923em;">
                        <span class="stl_18 stl_19 stl_20">VERGİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:41.4017em;top:20.334em;">
                        <span class="stl_18 stl_19 stl_09">DAİRESİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.6667em;top:19.9632em;">
                        <span class="stl_18 stl_19 stl_20">İŞLEM &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.6667em;top:20.7048em;">
                        <span class="stl_18 stl_19 stl_17">NO &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:7.7017em;top:19.9632em;">
                        <span class="stl_18 stl_19 stl_09" style="word-spacing:0.0001em;">AD SOYAD / ÜNVAN &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:24.7842em;top:19.9632em;">
                        <span class="stl_18 stl_19 stl_20" style="word-spacing:0.0002em;">TCKN / VKN</span>
                        <span class="stl_18 stl_19 stl_20" style="word-spacing:0.9212em;">&nbsp;</span>
                        <span class="stl_18 stl_19 stl_21">ADRES &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:21.45em;top:20.334em;">
                        <span class="stl_18 stl_19 stl_09">ORANI &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.9167em;top:22.4382em;">
                        <span class="stl_18 stl_19 stl_17">300 &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:25.0342em;top:22.4382em;">
                        <span class="stl_18 stl_19 stl_17">6420391954 &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:41.6525em;top:22.4382em;">
                        <span class="stl_18 stl_19 stl_20">Y</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:24.6746em;">
                        <span class="stl_16 stl_08 stl_21" style="word-spacing:0.0008em;">ÜRÜN BİLGİLERİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:11.4358em;top:26.3279em;">
                        <span class="stl_16 stl_08 stl_23">A023 &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:28.5246em;">
                        <span class="stl_24 stl_08 stl_09" style="word-spacing:0em;">ÜRÜN KODU</span>
                        <span class="stl_12 stl_08 stl_09" style="word-spacing:0em;">: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:30.1871em;">
                        <span class="stl_12 stl_08 stl_23" style="word-spacing:-0.0005em;">ÜRÜN TÜRÜ: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:31.8504em;">
                        <span class="stl_12 stl_08 stl_11" style="word-spacing:-0.0001em;">ÜRÜN TİPİ: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:33.5079em;">
                        <span class="stl_12 stl_08 stl_11" style="word-spacing:0.0004em;">HASAT YILI: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:35.1596em;">
                        <span class="stl_12 stl_08 stl_09">DEPO: &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:12.615em;top:35.1588em;">
                        <span class="stl_12 stl_08 stl_20">A</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:36.5771em;">
                        <span class="stl_16 stl_08 stl_17" style="word-spacing:0.0005em;">İŞLEM BİLGİLERİ &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:8.2633em;top:38.3196em;">
                        <span class="stl_12 stl_08 stl_25" style="word-spacing:0.0007em;">İŞLEM MİKTARI &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:20.8008em;top:38.3196em;">
                        <span class="stl_12 stl_08 stl_09" style="word-spacing:0.0008em;">BİRİM FİYAT (TL/KG) &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:35.6342em;top:38.3196em;">
                        <span class="stl_12 stl_08 stl_11" style="word-spacing:0.0007em;">İŞLEM TUTARI &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:40.7833em;top:39.7371em;">
                        <span class="stl_12 stl_08 stl_20">2</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:41.2004em;">
                        <span class="stl_26 stl_08 stl_27">KDV &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:35.7525em;top:43.0949em;">
                        <span class="stl_28 stl_08 stl_11" style="word-spacing:-0.0006em;">Hesaplanan </span>
                        <span class="stl_29 stl_08 stl_21">KDV &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:14.0733em;top:44.4788em;">
                        <span class="stl_12 stl_08 stl_20">L</span>
                    </div>
                    <div class="stl_01" style="left:27.6558em;top:44.4788em;">
                        <span class="stl_12 stl_08 stl_20">1</span>
                    </div>
                    <div class="stl_01" style="left:40.9858em;top:44.4788em;">
                        <span class="stl_12 stl_08 stl_20">2</span>
                    </div>
                    <div class="stl_01" style="left:4.5833em;top:46.2221em;">
                        <span class="stl_16 stl_08 stl_11" style="word-spacing:-0.0004em;">NET TUTAR &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:40.0525em;top:47.9646em;">
                        <span class="stl_12 stl_08 stl_20" style="word-spacing:0.0005em;">NET TUTAR &nbsp;</span>
                    </div>
                    <div class="stl_01" style="left:40.0758em;top:49.3821em;">
                        <span class="stl_12 stl_08 stl_20">2</span>
                    </div>
                </div>
            </div>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the relevant elements and update their text content
fatura_tarihi = soup.find('span', {'class': 'stl_12 stl_08 stl_11', 'style': 'word-spacing:0.0623em;'})
if fatura_tarihi:
    fatura_tarihi.string = '11/01/2022'

belge_no = soup.find('span', {'class': 'stl_15 stl_08 stl_09', 'style': 'word-spacing:0.0005em;'})
if belge_no:
    belge_no.string = '22/05/2022'

islem_no = soup.find('span', {'class': 'stl_18 stl_19 stl_17'})
if islem_no:
    islem_no.string = '14'

# Save the modified HTML
with open('modified_html12.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
