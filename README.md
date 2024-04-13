# Hướng dẫn chạy code:
## B1: Mở terminal thực hiện lệnh `cd` đến folder chứa file `main.py` của chương trình.
* ### Ví dụ: folder `ai-path-searching` ở ổ đĩa C, nhập như sau: `cd C:\ai-path-searching`
## B2: Nhập vào termial `pip install pygame` => Enter.
## B3: Nhập vào terminal `python main.py` => Enter.
* ### Câu lệnh trên mặc định sẽ chạy thuật toán `BFS`.
* ### Để thay đổi thuật toán, chẳng hạn như thuật toán `A*`, thay đổi dòng lệnh thành `python main.py --algo A*`.
* ### Tương tự với các thuật toán `DFS` và `UCS`.
* ### Nếu muốn thay đổi map, vào file `main.py` (dòng 11) và thay đổi tên file input.
* ### Nếu chỉ thao tác trên terminal, để đổi map thì cần đặt lại tên map đó là `input.txt`.
* ### Trường hợp có thêm điểm đón, cần nhập tọa độ từ 3 điểm trở lên với 2 điểm đầu là điểm bắt đầu và điểm kết thúc.
* ### Lưu ý: Tọa độ các điểm trên map không được vượt quá giới hạn không gian map.