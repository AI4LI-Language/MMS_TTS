# Fine-tuning mô hình MMS-TTS

## Tham khảo từ github repo sau

Finetuning mô hình VITS: https://github.com/ylacombe/finetune-hf-vits


## 🗒️ Giới thiệu mô hình
Dự án này thực hiện fine-tuning mô hình MMS-TTS (Massively Multilingual Speech - Text to Speech) với mục tiêu chuyển đổi giọng đọc từ tiếng Việt miền Nam sang tiếng Việt miền Bắc.
Ngoài ra, mô hình có khả năng chỉnh sửa đầu ra như:

Làm giọng đọc nhanh hơn, chậm hơn.

Điều chỉnh âm lượng tiếng to hơn, nhỏ hơn.

Em đã sử dụng kiến trúc **MMS-TTS-vie** được tích hợp trong HuggingFace Transformers để tiến hành huấn luyện, giúp sinh ra giọng đọc tự nhiên, rõ ràng và mượt mà.

🏛️ Về kiến trúc:

*VITS*: Kết hợp giữa Autoencoder biến thể, GAN (Generative Adversarial Networks) và Normalizing Flows, cho phép mô hình sinh âm thanh có chất lượng cao, đồng thời tự động hóa cả quá trình duration prediction và acoustic modeling.

*Discriminator*: Một thành phần GAN giúp đánh giá và cải thiện chất lượng sinh âm thanh.

* **Dữ liệu huấn luyện**: Hiện tại vẫn đang tìm một bộ dữ liệu có kích cỡ vừa phải, phân biệt rõ giọng bắc, giọng nam, giọng đàn ông, giọng phụ nữ giao tiếp bằng Tiếng Việt nhưng chưa có

* **Mục tiêu**: Chuyển đổi giọng nói tiếng Việt chuẩn miền Nam thành giọng miền Bắc tự nhiên hơn.

## Nghiên cứu liên quan
[Link bài báo gốc mô hình MMS-TTS công bố tại Facebook AI Research (FAIR)](https://arxiv.org/pdf/2305.13516 "Link PDF arxiv")

[Link bài báo gốc kiến trúc VITS công bố tại ICML 2021](https://arxiv.org/pdf/2106.06103 "Link PDF arxiv")


##  Hướng dẫn cài đặt
1. Clone repository:
````
git clone https://https://github.com/nhawtanhy/Text_To_Speech.git
````

2. Cài đặt các thư viện yêu cầu:
````
pip install -r requirements.txt
````

3. Chạy lệnh fine-tuning (Hiện chưa chạy được do chưa có data và chưa config)
````
python train_vits.py --config_file config.json
````

## Theo dõi quá trình huấn luyện

## Demo mô hình base MMS-TTS
Một File streamlit đơn giản được tạo ra để thử nghiệm mô hình MMS-TTS-vie base ở trên HuggingFace, 

Màn hình Demo:
![Screenshot (255)](https://github.com/user-attachments/assets/6eeac109-b249-4202-a397-9088a290a437)

[Video Demo](https://drive.google.com/drive/folders/1huEukyhhdalVE8B7zKaW_qYAuKajILRK?usp=sharing) 
