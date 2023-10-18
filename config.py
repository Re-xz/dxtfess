import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://fadhil:fadhil123@cluster0.jvnx5r6.mongodb.net/?retryWrites=true&w=majority")
db_name = os.getenv("DB_NAME", "fadhil") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001976588675"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001610283560")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1001710331413"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "3"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#ss #aa #CpfBoy #CpfAsk #CpfGirl #CpfSpill #CpfStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Halo Sobat CPF 👋

Kamu harus bergabung di CHANNEL & GROUP Terlebih dahulu untuk mengirim pesan ke @MenfessCPF

Join Ke Channel & Group Kemudian Tekan /start ⤵️
""")
start_msg = os.getenv("START_MSG", """
Halo {mention} 😍

CPF Autopost bot adalah bot autopost, semua pesan yang dikirimkan ke bot ini akan otomatis dikirim ke channel @MenfessCPF, gunakan hastag dibawah untuk mengirim pesan:

#CpfBoy / #CpfGirl : untuk mencari teman, pasangan, partner dll.
#CpfAsk : untuk bertanya.
#CpfSpill : untuk spill sesuatu.
#CpfStory : untuk berbagi cerita/pengalaman.

Contoh :
i have crush on you #CpfSpill
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#CpfBoy / #CpfGirl : untuk mencari teman, pasangan, partner dll.
#CpfAsk : untuk bertanya
#CpfSpill : untuk spill sesuatu
#CpfStory : untuk berbagi cerita/pengalaman.

untuk pertanyaan silahkan gabung @CariParterFwb
""")
