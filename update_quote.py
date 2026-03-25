import random
import re

# 25 Türkçe Matin — Yazılım, Motivasyon, Felsefe karışık
QUOTES = [
    # 💻 Yazılım / Teknoloji
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
