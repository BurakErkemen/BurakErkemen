import random
import re

# 25 Türkçe Matin — Yazılım, Motivasyon, Felsefe karışık
QUOTES = [
    # 💻 Yazılım / Teknoloji
        {
        "text": "Kodun okunabilirliği, performansından önce gelir.",
        "author": "Robert C. Martin",
        "emoji": "📖"
    },
    {
        "text": "Önce çalıştır, sonra optimize et.",
        "author": "Anonim",
        "emoji": "⚡"
    },
    {
        "text": "En iyi geliştiriciler, en çok hata yapan ama en hızlı öğrenenlerdir.",
        "author": "Anonim",
        "emoji": "📈"
    },
    {
        "text": "Teknoloji araçtır; farkı yaratan zihindir.",
        "author": "Anonim",
        "emoji": "🧠"
    },
    {
        "text": "Bir problemi çözmeden önce onu doğru tanımla.",
        "author": "Anonim",
        "emoji": "🎯"
    },
    {
        "text": "Kod yazmak sanattır; refactor etmek ustalıktır.",
        "author": "Anonim",
        "emoji": "🎨"
    },
    {
        "text": "Zor görünen şeyler, yeterince bölündüğünde kolaylaşır.",
        "author": "Anonim",
        "emoji": "🧩"
    },
    {
        "text": "Motivasyon geçicidir, disiplin kalıcıdır.",
        "author": "Anonim",
        "emoji": "🏋️"
    },
    {
        "text": "Bugün yaptığın seçimler, yarının versiyonunu belirler.",
        "author": "Anonim",
        "emoji": "🔄"
    },
    {
        "text": "Küçük ilerlemeler, büyük sonuçların temelidir.",
        "author": "Anonim",
        "emoji": "📊"
    },
    {
        "text": "Sürekli öğrenmeyen geliştirici, yavaş yavaş silinir.",
        "author": "Anonim",
        "emoji": "🧯"
    },
    {
        "text": "En iyi yatırım, kendine yaptığın yatırımdır.",
        "author": "Warren Buffett",
        "emoji": "💰"
    },
    {
        "text": "Düşünmeden yazılan kod, okunmadan silinir.",
        "author": "Anonim",
        "emoji": "🗑️"
    },
    {
        "text": "Her cevap yeni sorular doğurur.",
        "author": "Anonim",
        "emoji": "❓"
    },
    {
        "text": "Zamanını yönetemeyen, hayatını yönetemez.",
        "author": "Anonim",
        "emoji": "⏳"
    },
    {
        "text": "Bilgi güçtür, ama uygulama gerçek güçtür.",
        "author": "Anonim",
        "emoji": "🔋"
    },
    {
        "text": "Yazılım dünyasında tek sabit şey değişimdir.",
        "author": "Anonim",
        "emoji": "🌐"
    },
    {
        "text": "İyi bir geliştirici problemi çözer, harika bir geliştirici problemi önler.",
        "author": "Anonim",
        "emoji": "🛡️"
    },
    {
        "text": "Karmaşıklık, genellikle yanlış bir yaklaşımın sonucudur.",
        "author": "Anonim",
        "emoji": "🌀"
    },
    {
        "text": "Bir şeyi öğretmek, onu iki kez öğrenmektir.",
        "author": "Anonim",
        "emoji": "🎓"
    },
    {
        "text": "Her büyük yazılım, önce hayal edilmiştir. Sonra tasarlanmış, sonra debuglanmıştır.",
        "author": "Anonim",
        "emoji": "💻"
    },
    {
        "text": "İyi kod, iyi bir şiir gibidir — okunması zahmetsiz, anlaşılması aydınlatıcıdır.",
        "author": "Anonim",
        "emoji": "📝"
    },
    {
        "text": "Basit tutmak, karmaşıklaştırmaktan çok daha zordur.",
        "author": "Steve Jobs",
        "emoji": "💡"
    },
    {
        "text": "Programlama düşünmeyi öğretir. Düşünmeyi öğrenen her şeyi çözebilir.",
        "author": "Steve Jobs",
        "emoji": "🧠"
    },
    {
        "text": "Hata yapmak insani; hataları sessizce geçmek ise yazılımcıya özgüdür.",
        "author": "Anonim",
        "emoji": "🐛"
    },
    {
        "text": "Tekrar kullanılabilir kod yazmak, geleceğe mektup göndermek gibidir.",
        "author": "Anonim",
        "emoji": "♻️"
    },
    {
        "text": "Bir problemi çözmenin en iyi yolu, onu daha küçük problemlere bölmektir.",
        "author": "Anonim",
        "emoji": "🔍"
    },

    # 🚀 Motivasyon / Başarı
    {
        "text": "Başarı, her gün tekrar ettiğin küçük disiplinlerin toplamıdır.",
        "author": "Jim Rohn",
        "emoji": "🚀"
    },
    {
        "text": "Gelecek, hayallerinin güzelliğine inananlarındır.",
        "author": "Eleanor Roosevelt",
        "emoji": "🌟"
    },
    {
        "text": "Başarısızlık, daha akıllıca bir deneme için fırsattır.",
        "author": "Henry Ford",
        "emoji": "💪"
    },
    {
        "text": "En uzun yolculuk bile tek bir adımla başlar.",
        "author": "Lao Tzu",
        "emoji": "👣"
    },
    {
        "text": "Yapabildiğini düşün ya da yapamayacağını — ikisinde de haklısın.",
        "author": "Henry Ford",
        "emoji": "🎯"
    },
    {
        "text": "Büyük şeyler, konfor alanından çıkmakla başlar.",
        "author": "Anonim",
        "emoji": "🔥"
    },
    {
        "text": "Dün en iyi günündü derken bugünü kaçırma.",
        "author": "Anonim",
        "emoji": "⏰"
    },

    # 🧠 Felsefe / Hayat
    {
        "text": "Tek bildiğim şey, hiçbir şey bilmediğimdir.",
        "author": "Sokrates",
        "emoji": "🤔"
    },
    {
        "text": "İnsan, yaptıklarının toplamından ibarettir.",
        "author": "Aristoteles",
        "emoji": "🏛️"
    },
    {
        "text": "Değişemeyen tek şey değişimin kendisidir.",
        "author": "Heraklitos",
        "emoji": "🌊"
    },
    {
        "text": "Merak, bilginin anasıdır.",
        "author": "Anonim",
        "emoji": "🔭"
    },
    {
        "text": "Öğrendikçe öğrenecek çok şeyin olduğunu fark edersin.",
        "author": "Anonim",
        "emoji": "📚"
    },
    {
        "text": "Bir insanı tanımak istiyorsan, ona güç ver ve izle.",
        "author": "Abraham Lincoln",
        "emoji": "👁️"
    },
    {
        "text": "Sabır, her şeyin ilacıdır.",
        "author": "Mevlana",
        "emoji": "🌿"
    },
    {
        "text": "Ne kadar bilirsen bil, söylediklerin karşındakinin anlayabildiği kadardır.",
        "author": "Mevlana",
        "emoji": "💬"
    },
    {
        "text": "Bugünü iyi yaşa; dün bir rüya, yarın ise bir hayaldir.",
        "author": "Kalidasas",
        "emoji": "🌅"
    },
    {
        "text": "Akıl yürütmek, doğru soruları sormakla başlar.",
        "author": "Anonim",
        "emoji": "❓"
    },
    {
        "text": "Mükemmellik bir hedef değil, sürekli bir yolculuktur.",
        "author": "Anonim",
        "emoji": "🎓"
    },
        # 🔥 Hardcore Developer / Teknik
    {
        "text": "Premature optimization is the root of all evil — ama hiç optimize etmemek de ayrı bir felaket.",
        "author": "Anonim",
        "emoji": "⚙️"
    },
    {
        "text": "State yönetimi zor değildir; yanlış state yönetimi her şeyi zorlaştırır.",
        "author": "Anonim",
        "emoji": "🧵"
    },
    {
        "text": "Abstraction doğru yerde güçtür, yanlış yerde kabustur.",
        "author": "Anonim",
        "emoji": "🧱"
    },
    {
        "text": "Coupling arttıkça özgürlük azalır.",
        "author": "Anonim",
        "emoji": "🔗"
    },
    {
        "text": "Test yazmıyorsan, sadece umut ediyorsun.",
        "author": "Anonim",
        "emoji": "🧪"
    },
    {
        "text": "Code review, egoyu değil kaliteyi geliştirmek içindir.",
        "author": "Anonim",
        "emoji": "👀"
    },
    {
        "text": "Good architecture, kötü kararların etkisini sınırlar.",
        "author": "Anonim",
        "emoji": "🏗️"
    },

    # 😂 Mizahi / Reddit tarzı
    {
        "text": "Çalışıyorsa dokunma… ama neden çalıştığını da öğren.",
        "author": "Anonim",
        "emoji": "😅"
    },
    {
        "text": "Bu kodu ben mi yazdım yoksa düşmanım mı emin değilim.",
        "author": "Anonim",
        "emoji": "🤨"
    },
    {
        "text": "Stack Overflow olmasaydı, yazılım sektörü %50 daha yavaş olurdu.",
        "author": "Anonim",
        "emoji": "📚"
    },
    {
        "text": "Bir bug’ı düzeltirsin, üç tane yeni spawn olur.",
        "author": "Anonim",
        "emoji": "👾"
    },
    {
        "text": "Debug süresi, yazma süresinden her zaman daha uzundur.",
        "author": "Anonim",
        "emoji": "🐞"
    },
    {
        "text": "Kod yazarken tanrı gibisin, debug yaparken dedektif.",
        "author": "Anonim",
        "emoji": "🕵️"
    },
    {
        "text": "Dün yazdığın kodu bugün anlamıyorsan, gelişmişsin demektir.",
        "author": "Anonim",
        "emoji": "🧠"
    },

    # ⚡ Kısa Punchline (README için ideal)
    {
        "text": "Önce doğruyu yap, sonra hızlı yap.",
        "author": "Anonim",
        "emoji": "⚡"
    },
    {
        "text": "Az kod, çok değer.",
        "author": "Anonim",
        "emoji": "📉"
    },
    {
        "text": "Basit > Karmaşık",
        "author": "Anonim",
        "emoji": "✔️"
    },
    {
        "text": "Öğrenmek = Tekrar + Hata",
        "author": "Anonim",
        "emoji": "🔁"
    },
    {
        "text": "Bugün öğren, yarın üret.",
        "author": "Anonim",
        "emoji": "🚀"
    },
    {
        "text": "Kod konuşur.",
        "author": "Anonim",
        "emoji": "💬"
    },
    {
        "text": "Disiplin > Motivasyon",
        "author": "Anonim",
        "emoji": "🏁"
    }
]

def update_readme():
    quote = random.choice(QUOTES)

    new_block = (
        f"<!-- QUOTE_START -->\n"
        f"> {quote['emoji']} *\"{quote['text']}\"*\n"
        f">\n"
        f"> — **{quote['author']}**\n"
        f"<!-- QUOTE_END -->"
    )

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    updated = re.sub(
        r"<!-- QUOTE_START -->.*?<!-- QUOTE_END -->",
        new_block,
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ Matin güncellendi: {quote['emoji']} \"{quote['text'][:50]}...\"")

if __name__ == "__main__":
    update_readme()
